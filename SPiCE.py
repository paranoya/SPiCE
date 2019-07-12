#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Self-consistent Photo-ionisation and Chemical Evolution (SPiCE)

Created on Tue Mar 26 11:56:10 2019

@author: yago
"""

from __future__ import print_function, division

import argparse
import yaml
import numpy as np

from matplotlib import pyplot as plt

import settings
import phases
import processes


__version__ = "0.0.1-alpha"


def get_class(base_module, class_name):
    selected_class = base_module
    for name in class_name.split('.'):
        selected_class = selected_class.__dict__[name]
    return selected_class


# -----------------------------------------------------------------------------
class Model(phases.basic.MultiphaseMedium):

    def read_config_file(self, name):
        print(name)
        with open(name, "r") as settings_file:
            user_settings = yaml.safe_load(settings_file)
        self.context = settings.validate(user_settings)

    def __init__(self, config_file):
        if config_file is None:
            config_file = 'model.yml.example'
        self.read_config_file(config_file)

        self.phases = {}
        for phase_name in self.context['phases']:
            phase = self.context['phases'][phase_name]
            self.phases[phase_name] = phases.registry[phase['type']](self, phase['params'])

        self.processes = {}
        for process_name in self.context['processes'].keys():
            process = self.context['processes'][process_name]
            self.processes[process_name] = processes.registry[process['type']](self, process['params'])

        self.integrator = self.context['integrator']
        self.run()

    def run(self):
        print(self.integrator)
        self.time_Gyr = [self.integrator['initial_time_Gyr']]
        while self.time_Gyr[-1] < self.integrator['final_time_Gyr']:
            current_time_Gyr = self.time_Gyr[-1]
            for phase in self.phases.values():
                phase.reset_timestep()
            for process in self.processes.values():
                process.compute_derivatives()
            timesteps_Gyr = [self.integrator['final_time_Gyr'] - current_time_Gyr]
            for phase in self.phases.values():
                timesteps_Gyr.append(phase.get_timestep_Gyr())
            timestep_Gyr = np.nanmax([np.nanmin(timesteps_Gyr),
                                     self.integrator['minimum_timestep_Gyr']])
            for phase in self.phases.values():
                phase.update_mass(timestep_Gyr)
            self.time_Gyr.append(current_time_Gyr + timestep_Gyr)

    def update_derivatives(self, term):
        print("This should not happen!")
        raise(-1)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="SPiCE",
        description="Command line tools for the SPiCE chemical evolution code.",
    )
    parser.add_argument("-v", "--version", action="version", version=__version__)
    parser.add_argument("--config", metavar="FILENAME", help="configuration file to use containing model initial params")

    args = parser.parse_args()

    model = Model(args.config)

    print("\nMasses:")
    for phase in model.phases.keys():
        print(' ', phase, model[phase].params, model.m(phase))

    print("\nProcesses:")
    for process in model.processes.keys():
        print(' ', process, model.processes[process].tau_Gyr)

#    plt.plot(model.time_Gyr, model['gas'].mass_history_Msun, 'b-')
#    plt.plot(model.time_Gyr, model['stars'].mass_history_Msun, 'r-')
