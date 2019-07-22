from . import basic
from . import Recombination
from . import MoleculeFormation

registry = {
        "timescale_constant": basic.Constant_timescale,
        "H_recombination": Recombination.Hydrogen_Recombination,
        "H2_formation": MoleculeFormation.MolecularHydrogen_Formation,
        }
