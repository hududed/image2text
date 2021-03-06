import io
import os

from google.cloud import vision
from google.cloud.vision import types
from google.protobuf.json_format import MessageToJson

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = '/Users/hud/Documents/img2txt/src/credential.json'


# from google.oauth2 import service_account

# credentials = service_account.Credentials.from_service_account_file(
#     '/Users/hud/Documents/img2txt/src/credential.json')

class GoogleVisionApi:
	def __init__(self):
		# Instantiates a client
		self.client = vision.ImageAnnotatorClient()
		self.requestsCache = {}
	
	def request(self, imagePath):
		# Loads the image into memory
		with io.open(imagePath, 'rb') as image_file:
		    content = image_file.read()

		image = types.Image(content=content)

		# Performs label detection on the image file
		self.requestsCache[imagePath] = self.client.document_text_detection(image=image)

		response = self.requestsCache[imagePath]
		jsonText = MessageToJson(response)

		return jsonText

	def clear(self,requestName):
		if requestName in self.requestsCache:
			del self.requestsCache[requestName]

	def clearAll(self):
		self.requestsCache = {}

