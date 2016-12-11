import math
import json

import s2sphere
from mock_pgoapi import mock_pgoapi as pgoapi 

import boto3

SQS_QUEUE_NAME = "awseb-e-zmr2vxgc3a-stack-AWSEBWorkerQueue-1AKITUM6YYGLX"

def break_down_area_to_cell(north, south, west, east):
    """ Return a list of s2 cell id"""
    result = []

    region = s2sphere.RegionCoverer()
    region.min_level = 15
    region.max_level = 15
    p1 = s2sphere.LatLng.from_degrees(north, west)
    p2 = s2sphere.LatLng.from_degrees(south, east)

    cell_ids = region.get_covering(s2sphere.LatLngRect.from_point_pair(p1, p2))
    result += [cell_id.id() for cell_id in cell_ids]
    print result

    return result

def get_position_from_cell_id(cell_id):
    cell = s2sphere.CellId(id_ = cell_id).to_lat_lng()

    return (math.degrees(cell._LatLng__coords[0]), math.degrees(cell._LatLng__coords[1]), 0)

def parse_pokemons_from_response(response_dict):
    return response_dict["responses"]["GET_MAP_OBJECTS"]["map_cells"][0]["catchable_pokemons"]

def scan_point(cell_id):
    """ Return pokemons in cell_id """
    api = pgoapi.PGoApi()

    position = get_position_from_cell_id(cell_id)
    cell_ids = [cell_id]
    response_dict = api.get_map_objects(latitude =position[0], 
					longitude = position[1], 
					since_timestamp_ms = [0], 
					cell_id = cell_ids)
    # 3. Parse output
    return parse_pokemons_from_response(response_dict)


def scan_area(north, south, west ,east):
    result  = []
    # 1. Find all points to scan in this area
    cell_ids = break_down_area_to_cell(north, south, west ,east)

    work_queue = boto3.resource('sqs', region_name='us-west-2').get_queue_by_name(QueueName=SQS_QUEUE_NAME)

    # 2.Scan current area
    for cell_id in cell_ids:
        #        result += scan_point(cell_id) 
        work_queue.send_message(MessageBody=json.dumps({"cell_id":cell_id}))
    # 4. Deliver pokemon location
    return result 

if __name__ == "__main__":
    print json.dumps(scan_area(41, 40.79, -74, -73.99), indent=2)
