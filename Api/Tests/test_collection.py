import requests
import json
import jsonpath
import os

baseUrl = "http://0.0.0.0:8008"


def test_get_collection_data():
    path = "/collection"
    response = requests.get(url=baseUrl + path)
    responseJson = json.loads(response.text)
    assert response.status_code == 200


def test_post_collection():
    file = open(os.path.abspath("Api/TestData/CollectionPayload.json"), "r")
    path = "/collection"
    inputData = json.loads(file.read())
    inputData["name"] = "raheel"
    response = requests.post(url=baseUrl + path, json=inputData)
    responseJson = json.loads(response.text)
    assert response.status_code == 200 #should be 201
    assert jsonpath.jsonpath(responseJson, '$.name')[0] == inputData["name"]
    id = jsonpath.jsonpath(responseJson, '$.id')[0]
    response = requests.delete(url=baseUrl + path + '/' + id)
    assert response.status_code == 200 #should be 204
