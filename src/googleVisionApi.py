import io
import os

from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson

class GoogleVisionApi:
    def __init__(self):
        # Instantiates the image annotation client
        self.client = vision.ImageAnnotatorClient()
        self.requestsCache = {}
        
    def request(self, imagePath):
        # Writes image to memory
        with io.open(imagePath, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)

        # Label detection in loaded image 
        self.requestsCache[imagePath] = self.client.document_text_detection(image=image)

        response = self.requestsCache[imagePath]
        jsonText = MessageToJson(response)

        return jsonText

    def clear(self,requestName):
        if requestName in self.requestsCache:
            del self.requestsCache[requestName]

    def clearAll(self):
        self.requestsCache = {}

