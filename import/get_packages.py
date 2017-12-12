import os
import json
from urllib import request

DATA_PATH = os.getenv('DATA_PATH', 'data')

AMS_CATALOG_URL = "https://api.data.amsterdam.nl/catalogus/api/3"

ALL_PACKAGES = f"{AMS_CATALOG_URL}/action/package_search?facet.field=%5B%22groups%22,%22res_format%22,%22organization%22%5D&fq=&rows=1000&sort=name+asc&start=0" #noqa
PACKAGE_LIST = f"{AMS_CATALOG_URL}/action/package_list"
PACKAGE_URL = f"{AMS_CATALOG_URL}/action/package_show?id="

request.urlretrieve(ALL_PACKAGES, f"{DATA_PATH}/packages.json")
request.urlretrieve(PACKAGE_LIST, f"{DATA_PATH}/package_list.json")

with open("data/packages.json") as json_data:
    d = json.load(json_data)
    for package in d['result']['results']:
        request.urlretrieve(
            f"{PACKAGE_URL}{package['id']}",
            f"data/{package['id']}.json")
