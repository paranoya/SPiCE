from . import basic

class Dust(basic.Phase):

    def default_settings(self):
        return {
            'current_mass': 0.,
            'dm_dt': 0.,
            'sticky_coeficient': 0.7,
            'sn_fraction_out_super_bubbles': 0.678,
            'molecular_cloud_density': 5000,
        }