import requests
from multiprocessing import Pool

def query(x):
    response = requests.get("http://query-server.us-west-2.elasticbeanstalk.com/map/pokemon?east=-73.99837592515519&south=40.74279758800707&north=40.74847928621097&west=-74.00130489739945")

p = Pool(20)
p.map(query, range(100))

