from . import basic
from .dust import Dust

def select_phase(name):
    available_phases = {
        "simple": basic.Phase,
        "multiphase": basic.MultiphaseMedium,
        "dust": Dust,
    }

    return available_phases[name]
