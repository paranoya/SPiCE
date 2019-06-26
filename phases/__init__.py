from . import basic
from . import GasSpecies
from . import example
from . import GasSpecies

registry = {
        "basic": basic.Phase,
        "multiphase": basic.MultiphaseMedium,
        "ionized_hydrogen": GasSpecies.Ionized_Hydrogen,
        "neutral_hydrogen": GasSpecies.Neutral_Hydrogen,
        "molecular_hydrogen": GasSpecies.Molecular_Hydrogen,
        "dust": example.dust.Dust,
    }

    return available_phases[name]
