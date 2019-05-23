#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:56:10 2019

@author: yago
"""

from __future__ import print_function, division

import argparse, yaml

import SPiCE
import settings
import phases
from phases import select_phase
import processes

__version__ = "0.0.1-alpha"

# -----------------------------------------------------------------------------
class Model(phases.basic.MultiphaseMedium):

    def __init__(self, context):
        self.phases = {}
        for phase_name in context['phases'].keys():
            phase = context['phases'][phase_name]
            self.phases[phase_name] = select_phase(phase['type'])(phase['params'])

        self.processes = {}
        for process_type in context['processes'].keys():
            process = context['processes'][process_type]
            process_name = process['name']
            self.processes[process_type] = processes.registry.select_process(process_type, process_name)
            self.processes[process_type].init(process['params'])

    def update_derivatives(self, term):
        print("This should not happen!")
        raise(-1)


def main():
    parser = argparse.ArgumentParser(
        prog="SPiCE",
        description="Command line tools for the SPiCE chemical evolution code.",
    )
    parser.add_argument("-v", "--version", action="version", version=SPiCE.__version__)
    parser.add_argument("--config", metavar="FILENAME", help="configuration file to use containing model initial params")

    args = parser.parse_args()

    user_settings = {}
    if args.config != None : user_settings = read_config_file(args.config)

    context = settings.validate(user_settings)

    model = Model(context)

    print("\nMasses:")
    for phase in model.phases.keys():
        print(' ', phase, model[phase].params, model.m(phase))

    print("\nProcesses:")
    for process in model.processes.keys():
        print(' ', process, model.processes[process].tau)

def read_config_file(name):
    with open(name, "r") as settings_file:
        user_settings = yaml.safe_load(settings_file)
    return user_settings


if __name__ == "__main__":
    main()
