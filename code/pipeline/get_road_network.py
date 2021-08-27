"""
from jjh
"""

import xml.etree.ElementTree as xml
import json
import os


def get_road_network(config):
    # Allow these types of streets to be represented in the network by an edge.
    way_types = ["motorway", "trunk", "primary", "secondary", "tertiary", "unclassified", "residential", "service",
                 "living_street"]

    path_to_file = os.path.abspath("./data/raw_data/" + config.get('map_file') + '.osm')
    root = xml.parse(path_to_file).getroot()
    ways = root.findall("way")
    nodes = root.findall("node")
    ID2Node = {}
    count = 0
    for node in nodes:
        count += 1
        ID2Node[node.attrib["id"]] = [[float(node.attrib["lat"]), float(node.attrib["lon"])], count]
    roads = []
    for way in ways:
        way_tags = way.findall("tag")
        flag_high = 0
        flag_one = "no"
        prop = []
        for way_tag in way_tags:
            if way_tag.attrib["k"] =="highway" and way_tag.attrib["v"] in way_types:
                flag_high = 1
            if way_tag.attrib["k"] =="oneway" and way_tag.attrib["v"] == "yes":
                flag_one = "yes"
        if flag_high == 0:
            continue
        prop.append(flag_one)
        cor = []
        nds = way.findall("nd")
        for nd in nds:
            cor.append(ID2Node[nd.attrib["ref"]][0])
        from_nd = ID2Node[nds[0].attrib["ref"]][1]
        to_nd = ID2Node[nds[-1].attrib["ref"]][1]
        prop.append(cor)
        prop.append(from_nd)
        prop.append(to_nd)
        roads.append(prop)

    roadJson = {}
    roadJson["type"] = "FeatureCollection"
    roadJson["name"] = "edges"
    roadJson["crs"] = {}
    roadJson["crs"]["type"] = "name"
    roadJson["crs"]["properties"] = {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}
    roadJson["features"] = []
    count = 0
    for road in roads:
        count += 1
        temp = {
            "type": "Feature",
            "properties": {
                "id": count,
                "class": "LNLink",
                "oneway": road[0],
                "from": road[2],
                "to":road[3]
            },
            "geometry": {
                "type": "LineString",
                "coordinates": [point[::-1] for point in road[1]]
            }
        }
        roadJson["features"].append(temp)
    with open("data/cache/" + config.get('map_file') + ".json", "w") as f:
        json.dump(roadJson, f, indent=4)



