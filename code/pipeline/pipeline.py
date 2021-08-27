from code.pipeline.get_road_network import get_road_network
from code.pipeline.json_to_atom_files import map2atom, trajectory2atom
from code.util.util import ensure_dir
from code.pipeline.atom_to_json import map2json, trajectory2json, output2json
import json
import os

def to_atom(config):
    """
    generate atom file
    :param config:
    :return:
    """
    ensure_dir('./data/atom_data/' + config.get('map_file', ''))

    """
    step 1: from map to road network (from osm to json)
    """

    get_road_network(config)

    """
    step 2: from road network and trajectory to atom
    """
    geo_id = map2atom(config)
    trajectory2atom(config, geo_id)

    """
    step3: generate config from a template and extra_info
    """
    json_obj = json.load(open('./sample/config.json', 'r'))
    json_obj['info'] = config.get('extra_info', dict())
    json.dump(json_obj, open('./data/atom_data/' + config.get('map_file') + '/config.json', 'w'))


def atom2json(config):

    """
    generate geojson from atom file
    :param config:
    :return:
    """

    ensure_dir('./data/json/' + config.get('atom_file', ''))

    """
    step 1: generate map
    """
    map2json(config)

    """
    step2: generate trajectory
    """
    trajectory2json(config)

    """
    step3: generate output
    """
    if os.path.exists('./data/atom_data/' + config.get('atom_file', '') + '/' + config.get('atom_file', '') + '.out'):
        output2json(config)
