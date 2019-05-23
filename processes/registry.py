from . import star_formation

available_processes = {
    "star_formation": {
        "constant": star_formation.constant_efficiency,
    }
}

def select_process(process_type, selection):
    return available_processes[process_type][selection]