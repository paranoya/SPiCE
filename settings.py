"""
Default settings and initial parameters

All the values set here can be overwritten via a config input file: settings.yml

"""

default = {
    'initial_gas_mass': 1.0,              # in solar masses
    'initial_stellar_mass': 0.0,          # in solar masses
    'tau_SF': 1,                          # in Gyrs
    'initial_time': 0.0,                  # in Gyr
    'final_time':  13.7,                  # inGyr
    'integrator_relative_accuracy': 1e-6, # Maximum error accepted for the integration
    'imf': "kroupa",                      # Initial mass function
    'binary_star_rates': 0.40,            # Fraction of binary systems
    'dtd_sn': "rlp",                      # Delay Time Distribution for supernova rates
    'phases': {},
    'processes': {}
}

valid_values = {
    'imf': ['salpeter', 'starburst', 'chabrier', 'ferrini', 'kroupa', 'miller_scalo', 'maschberger'],
    'dtd_sn': ['rlp', 'mdvp'], # rlp = Ruiz-Lapuente, mdvp = Mannucci, Della Valle, Panagia (2006)
    'phases': ['ionized_hydrogen', 'neutral_hydrogen', 'molecular_hydrogen'],
}

def validate(params):
    params = {**default, **params}
    for param in valid_values.keys():
        if params[param] not in valid_values[param]:
            print(f'Provided value for {param} is incorrect.')
            print(f'  Valid values for {param} are: {valid_values[param]}')
            print(f'  Using default value: {default[param]}')
            params[param] = default[param]

    return params
