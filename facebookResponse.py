def makeImageResponse(result):
    message=[]
    data={
      "attachment": {
        "type": "image",
        "payload": {
          "url": result["url"]
        }
      }
    }
    message.append(data)

    return message