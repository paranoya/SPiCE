from . import basic
# from . import GasGenerics
from . import StarGenerics
from . import GasSpecies
from . import example


registry = {
    "basic": basic.Phase,
    "multiphase": basic.MultiphaseMedium,
    "star": StarGenerics.Star, #PLACEHOLDER!
    "ionized_hydrogen": GasSpecies.Ionized_Hydrogen,
    "neutral_hydrogen": GasSpecies.Neutral_Hydrogen,
    "molecular_hydrogen": GasSpecies.Molecular_Hydrogen,
    "dust": example.dust.Dust,
}
