"""
Default settings and initial parameters

All the values set here can be overwritten via a config input file: settings.yml

"""

default = {
    'imf': "kroupa",                      # Initial mass function
    'binary_star_rates': 0.40,            # Fraction of binary systems
    'dtd_sn': "rlp",
    'integrator': {
            'initial_time_Gyr': 0.0,
            'final_time_Gyr': 13.7,
            'relative_accuracy': 1.0e-6,
            'minimum_timestep_Gyr': 1.0e-6
            },
    'phases': {},
    'processes': {}
}

valid_values = {
    'imf': ['salpeter', 'starburst', 'chabrier', 'ferrini', 'kroupa', 'miller_scalo', 'maschberger'],
    'dtd_sn': ['rlp', 'mdvp'], # rlp = Ruiz-Lapuente, mdvp = Mannucci, Della Valle, Panagia (2006)
    #'phases': ['ionized_hydrogen', 'neutral_hydrogen', 'molecular_hydrogen'],
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
