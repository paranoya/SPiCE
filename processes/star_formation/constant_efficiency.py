#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:30:28 2019

@author: yago
"""

tau = 3.  # gas depletion time, in Gyr


def init(params):
    global tau
    tau = float(params['tau_SF'])


def compute_derivatives():
    SFR = gas.mass()/tau
    gas.update_derivatives(-SFR)
    stars.update_derivatives(SFR)
