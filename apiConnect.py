import requests
import json

def connectGiphy():
    baseurl= "http://api.giphy.com/v1/gifs/"
    api_key= "dc6zaTOxFJmzC"
    query = "funny cat"
    limit="1"
    baseurl= baseurl+"search?"+query+"api_key="+api_key+"limit="+limit
    response=makeConnection(baseurl)
    output=retriveData(response)
    return output




def makeConnection(baseurl):
    s=requests.Sesssion()
    result =s.get(baseurl)
    result=result.json()
    return result;

def retriveData(response):
    data = response["data"]
    images = data["images"]
    image= images["fixed_height"]

    output = {
        "url":image["url"]
    }

    return output