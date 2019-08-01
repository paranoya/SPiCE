from . import basic
from . import Recombination
from . import MoleculeFormation
from . import Ionization

registry = {
        "timescale_constant": basic.Constant_timescale,
        "H_recombination": Recombination.Hydrogen_Recombination,
        "H2_formation": MoleculeFormation.MolecularHydrogen_Formation,
        "basic_photoionization": Ionization.Basic_Photoionization,
        }
