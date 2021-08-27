import json

import pandas as pd


def map2json(config):
    """

    :param config:
    :return:
    """
    path = './data/atom_data/' + config.get('atom_file', '') + '/'
    geo_file = pd.read_csv(path + config.get('atom_file', '') + '.geo')
    rel_file = pd.read_csv(path + config.get('atom_file', '') + '.rel')

    json_obj = {
        "type": "FeatureCollection",
        "name": "road network",
        "features": None
    }
    features_list = []
    for index, row in rel_file.iterrows():
        feature_obj = {
            "type": "Feature",
            "properties": {
                "rel_id": row[0],
                "from": row[2],
                "to": row[3]
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    eval(geo_file.loc[row[2]][2]),
                    eval(geo_file.loc[row[3]][2])
                ]
            }
        }
        features_list.append(feature_obj)

    json_obj["features"] = features_list
    json.dump(json_obj, open('./data/json/' + config.get('atom_file') + '/road_network.json', 'w'), indent=4)


def trajectory2json(config):
    """

    :param config:
    :return:
    """
    # get files
    path = './data/atom_data/' + config.get('atom_file', '') + '/'
    geo_file = pd.read_csv(path + config.get('atom_file', '') + '.geo')
    dyna_file = pd.read_csv(path + config.get('atom_file', '') + '.dyna')
    usr_file = pd.read_csv(path + config.get('atom_file', '') + '.usr')

    # init json_obj
    json_obj = {
        "type": "FeatureCollection",
        "name": "road network",
        "features": None
    }

    # init features_list_dct
    features_list_dct = {}
    for index, row in usr_file.iterrows():
        features_list_dct[row[0]] = list()


    for index, row in dyna_file.iterrows():
        features_list_dct[row[3]].append(eval(geo_file.loc[row[4]][2]))

    feature_lst = list()
    for key, value in features_list_dct.items():
        feature = {
            "type": "Feature",
            "properties": {
                "usr_id": int(key),
            },
            "geometry": {
                "type": "MultiPoint",
                "coordinates": value
            }
        }
        feature_lst.append(feature)
    json_obj["features"] = feature_lst
    json.dump(json_obj, open('./data/json/' + config.get('atom_file') + '/trajectory.json', 'w'), indent=4)


def output2json(config):
    """

    :param config:
    :return:
    """

    # load files
    path = './data/atom_data/' + config.get('atom_file', '') + '/'
    out_file = pd.read_csv(path + config.get('atom_file', '') + '.out')
    rel_file = pd.read_csv(path + config.get('atom_file', '') + '.rel')
    geo_file = pd.read_csv(path + config.get('atom_file', '') + '.geo')
    json_obj = {
        "type": "FeatureCollection",
        "name": "road network",
        "features": None
    }
    features_list = []
    for index, row in out_file.iterrows():
        feature_obj = {
            "type": "Feature",
            "properties": {

            },
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    eval(geo_file.loc[rel_file.loc[row[0]][2]][2]),
                    eval(geo_file.loc[rel_file.loc[row[0]][3]][2])
                ]
            }
        }
        features_list.append(feature_obj)

    json_obj["features"] = features_list
    json.dump(json_obj, open('./data/json/' + config.get('atom_file') + '/out.json', 'w'), indent=4)
