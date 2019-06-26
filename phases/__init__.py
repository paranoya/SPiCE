from . import basic
from . import example

registry = {
        "basic": basic.Phase,
        "multiphase": basic.MultiphaseMedium,
        "dust": example.dust.Dust,
        }
