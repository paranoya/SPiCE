#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:59:28 2019

@author: yago
"""

from __future__ import print_function, division
import numpy as np

current_state = np.array([])
derivatives = np.array([])


def init(parameters):
    global current_state, derivatives
    current_state = np.array([float(parameters.get('initial_stellar_mass'))])
    derivatives = np.zeros_like(current_state)


def mass():
    return current_state[0]


def update_derivatives(term):
    global derivatives
    derivatives += term


# -----------------------------------------------------------------------------
#                                                    ... Paranoy@ Rulz! ;^D
# -----------------------------------------------------------------------------
