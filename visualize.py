"""
to visualize Map Matching task
"""
import os
import json
from code.pipeline.pipeline import atom2json

if __name__ == '__main__':
    config = json.load(open('code/config/vis_config.json', 'r'))
    # print(config)

    """
    step 1: prepare atom file
        add atom file's name to vis_config.json, 
        make sure the files are in data/atom_data folder
    """
    if not os.path.exists('./data/atom_data/' + config.get('atom_file') + '/config.json'):
        raise ValueError('atom file %s not found.' % config.get('atom_file', ''))

    """
    step 2: convert to json file
    """
    atom2json(config)
