from base import Base
class WebHook(Base):
	def create(self,request={}):
		return self.request("POST","/hook",{"callback" : request['callback'],"category" : request['category'],"address" : request['address']})
	
	def list(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10			
		return self.request("GET","/hook",{"offset" : request['offset'],"limit" : request['limit']})
		
		
	def get(self,request={}):
		return self.request("GET","/hook/" + str(request['hook_id']))

	def delete(self,request={}):
		return self.request("POST","/hook/" + str(request['hook_id']) + "/delete")
	
	
	def listResponse(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/hook/response",{"offset" : request['offset'],"limit" : request['limit']})			
			
	
	def getResponse(self,request={}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
	
		return self.request("GET","/hook/" + str(request['hook_id']) + "/response",{"offset" : request['offset'],"limit" : request['limit']})			


# wb = WebHook('B1zZARyW1d2FdqWxPUpB79izHmtAc2Az693WF9DD')
# print(wb.get({      "hook_id" : 1}))