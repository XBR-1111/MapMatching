"""
to generate atom file for Map Matching task
"""
import json
import os
from code.pipeline.pipeline import to_atom


if __name__ == '__main__':
    config = json.load(open('code/config/atom_config.json', 'r'))
    # print(config)

    """
    step 1: prepare map
        download map from https://www.openstreetmap.org/
        put the osm file in data folder
    """
    if not os.path.exists('./data/raw_data/' + config.get('map_file', '') + '.osm'):
        raise ValueError('map file %s not found.' % config.get('map_file', ''))

    """
    step 2: prepare trajectory  (.traj)
        csv file, put it in data folder.
    """
    for file_name in config.get('trajectory_files', []):
        if not os.path.exists('./data/raw_data/' + file_name + '.traj'):
            raise ValueError('trajectory file %s not found.' % file_name)

    """
    step 3: generate atom file 
    """
    to_atom(config)

    """
    step 4: prepare ground truth (.route) with the help of visualization
        csv file, put it in data folder.
    """
