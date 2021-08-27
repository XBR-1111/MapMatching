"""
from zjf
"""
import json
import pandas as pd
import numpy as np


def map2atom(config):

    file_name = config.get('map_file', '')
    with open('./data/cache/' + file_name + '.json', 'r') as load_f:
        load_dict = json.load(load_f)
        # for feature in load_dict["features"]:
        #     print(feature)

    geo = open('./data/atom_data/' + file_name + '/' + file_name + '.geo', "w")
    geo.write("geo_id, type, coordinate\n")
    rel = open('./data/atom_data/' + file_name + '/' + file_name + '.rel', "w")
    rel.write("rel_id,type,origin_id,destination_id\n")

    i = 0
    j = 0
    intersection_dct = dict()

    for feature in load_dict["features"]:

        # set one way
        if feature["properties"]["oneway"] == "yes":
            oneway = True
        else:
            oneway = False

        # set from, to
        from_no, to_no = feature["properties"]["from"], feature["properties"]["to"]

        coordinates = feature["geometry"]["coordinates"]
        prev_geo_id = None

        for index, location in enumerate(coordinates):
            # if first loc
            if index == 0:
                if from_no in intersection_dct.keys():
                    prev_geo_id = intersection_dct[from_no]
                else:
                    prev_geo_id = i
                    intersection_dct[from_no] = i
                    geo.write(str(i) + ',Point,"' + str(location) + '"\n')
                    i += 1
            # if inter loc, link it to prev
            elif index < len(coordinates) - 1:
                geo.write(str(i) + ',Point,"' + str(location) + '"\n')
                rel.write(str(j) + ',geo,' + str(prev_geo_id) + ',' + str(i) + '\n')
                j += 1
                if not oneway:
                    rel.write(str(j) + ',geo,' + str(i) + ',' + str(prev_geo_id) + '\n')
                    j += 1
                prev_geo_id = i
                i += 1
            # if the final loc, link it to prev
            else:
                if to_no in intersection_dct.keys():
                    geo_id = intersection_dct[to_no]
                    rel.write(str(j) + ',geo,' + str(prev_geo_id) + ',' + str(geo_id) + '\n')
                    j += 1
                    if not oneway:
                        rel.write(str(j) + ',geo,' + str(geo_id) + ',' + str(prev_geo_id) + '\n')
                        j += 1
                else:
                    geo_id = i
                    intersection_dct[to_no] = i
                    geo.write(str(i) + ',Point,"' + str(location) + '"\n')
                    rel.write(str(j) + ',geo,' + str(prev_geo_id) + ',' + str(geo_id) + '\n')
                    j += 1
                    if not oneway:
                        rel.write(str(j) + ',geo,' + str(geo_id) + ',' + str(prev_geo_id) + '\n')
                        j += 1
                    i += 1
    geo.close()
    rel.close()
    return i


def trajectory2atom(config, geo_id):
    file_name = config.get('map_file', '')
    file_names = config.get('trajectory_files', '')
    usr = open('./data/atom_data/' + file_name + '/' + file_name + '.usr', "w")
    geo = open('./data/atom_data/' + file_name + '/' + file_name + '.geo', "a")
    dyna = open('./data/atom_data/' + file_name + '/' + file_name + '.dyna', "w")

    usr.write('usr_id\n')
    dyna.write('dyna_id,type,time,entity_id,location')
    trajectory_extra_columns = config.get('trajectory_extra_columns', [])
    for column in trajectory_extra_columns:
        dyna.write(',' + column)
    dyna.write('\n')

    usr_id = 0
    dyna_id = 0

    for traj_file_name in file_names:

        # usr
        usr.write(str(usr_id) + '\n')

        traj = pd.read_csv('./data/raw_data/' + traj_file_name + '.traj')

        for index, line in traj.iterrows():
            lon, lat, time = float(line[0]), float(line[1]), line[2]
            if np.isnan(time):
                time = ''
            geo.write(str(geo_id) + ',Point,"' + str([lon, lat]) + '"\n')

            dyna.write(str(dyna_id) + ',trajectory,' + str(time) + ',' + str(usr_id) + ',' + str(geo_id))
            for column in trajectory_extra_columns:
                dyna.write(',' + str(line[column]))
            dyna.write('\n')

            dyna_id += 1
            geo_id += 1

        usr_id += 1

    usr.close()
    dyna.close()
    geo.close()
