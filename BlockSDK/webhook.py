from BlockSDK.base import Base
class WebHook(Base):
	def create(self,request={}):
		return self.request("POST","/hooks",{"callback_url" : request['callback_url'],"symbol" : request['symbol'],"address" : request['address']})
	
	def list(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10			
		return self.request("GET","/hooks",{"offset" : request['offset'],"limit" : request['limit']})
		
		
	def get(self,request={}):
		return self.request("GET","/hooks/" + str(request['hook_id']))

	def delete(self,request={}):
		return self.request("DELETE","/hooks/" + str(request['hook_id']))
	
	
	def getResponses(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/hooks/responses",{"offset" : request['offset'],"limit" : request['limit']})			
			
	
	def getHookResponses(self,request={}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
	
		return self.request("GET","/hooks/" + str(request['hook_id']) + "/responses",{"offset" : request['offset'],"limit" : request['limit']})			


# wb = WebHook('B1zZARyW1d2FdqWxPUpB79izHmtAc2Az693WF9DD')
# print(wb.get({      "hook_id" : 1}))
