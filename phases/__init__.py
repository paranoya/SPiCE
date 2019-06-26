from . import basic
from . import GasSpecies
from .dust import Dust

def select_phase(name):
    available_phases = {
        "simple": basic.Phase,
        "multiphase": basic.MultiphaseMedium,
        "ionized_hydrogen": GasSpecies.Ionized_Hydrogen,
        "neutral_hydrogen": GasSpecies.Neutral_Hydrogen,
        "molecular_hydrogen": GasSpecies.Molecular_Hydrogen,
        "dust": Dust,
    }

    return available_phases[name]
