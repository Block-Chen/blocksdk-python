from datetime import date, datetime, timedelta
import requests 
import json

class Base:
	def __init__(self, api_token):
		self.api_token = api_token

	def request(self,method,path,data = {}):
		url = "https://api.blocksdk.com/v2" + path 

		if method == "GET" and len(data) > 0:
			url += "?"
			for key in data.keys():
				value = data[key];
				if value == True: 
					url += key + "=true&"
				elif value == False:
					url += key + "=false&"
				else:
					url += key+ "=" + str(value) + "&"
		
		if method == "POST":
			response = requests.post(url = url, json = data, headers = { 'Content-Type': 'application/json','x-api-key': self.api_token}) 
		else:
			response = requests.get(url = url, headers = { 'Content-Type': 'application/json','x-api-key': self.api_token}) 
		
		try: 
			body = response.json()
		except:
			body = {}
	
		if method == "POST":
			try:
				body = json.loads(response.text)
			except:
				converted_json = response.text.replace(':','":')
				converted_json1 = converted_json.split('{\n')
				for i in range(len(converted_json1)):
					if converted_json1[i] != '': 
						json2 = converted_json1[i].split('":')[0].split(' ')[-1]
						converted_json = converted_json.replace(json2,'"' + json2)
				body = json.loads(converted_json)
						
		if response.headers:
			headers = response.headers
		else:
			headers = {}
		
		if response.status_code:
			status = response.status_code
		else:
			status = 0
		
		headers.update({'statusCode' : status})
		try:
			body.update({'HTTP_HEADER': headers})
		except:
			body = { i : body[i] for i in range(0, len(body) ) }
			body.update({'HTTP_HEADER': headers})
		
		#result_row = body['HTTP_HEADER'];
		# for key in result_row.keys():
		# 	if not result_row[key]:
		# 		if key == "statusCode":
		# 			result_row[key] = 0
		#body['HTTP_HEADER'] = result_row;
		
		return body

baseInstance = Base('B1zZARyW1d2FdqWxPUpB79izHmtAc2Az693WF9DD')
#print(baseInstance.getUsage({'start_date': '','end_date': ''}))
# print(baseInstance.getHashType({'hash':'000000000000000089d2938df30be807844feea4c3340ad32873bb1b692b7f1a'}))
