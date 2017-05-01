import requests
import json
from random import randint

def connectGiphy(queries,number):
    baseurl= "http://api.giphy.com/v1/gifs/"
    api_key= "dc6zaTOxFJmzC"
    query = queries
    limit=number
    baseurl= baseurl+"search?q="+query+"&api_key="+api_key+"&limit="+limit
    response=makeConnection(baseurl)
    output=retriveGiphyData(response)
    return output




def makeConnection(baseurl):
    s=requests.Session()
    result =s.get(baseurl)
    result=result.json()
    print(str(result))
    return result

def retriveGiphyData(response):
    data = response["data"]
    num =randint(0,len(data)-1)
    data= data[num]
    images = data["images"]
    image= images["fixed_height"]
    output = {
        "url":image["url"]
    }
    return output