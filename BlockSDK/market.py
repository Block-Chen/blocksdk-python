from BlockSDK.base import Base
class Market(Base):
	def getExchanges(self, request = {}):
		return self.request("GET","/market/exchanges")		
	
	def getTrades(self, request = {}):
		if not('from' in request) or not request['from']:
			request['from'] = None
		if not('to' in request) or not request['to']:
			request['to'] = "USD"
       
		return self.request("GET","/market/trades/" + str(request['block']),{"from" : request['from'],"to": request['to']})
    
  def getRates(self, request = {}):
       
		return self.request("GET","/market/rates/" + str(request['from']),{"to" : request['to'],"from_amount": request['from_amount']})
    
  def getExchangeTrades(self, request = {}):
		if not('from' in request) or not request['from']:
			request['from'] = None
		if not('to' in request) or not request['to']:
			request['to'] = "USD"
       
		return self.request("GET","/market/trades/" + str(request['exchage_id']),{"from" : request['from'],"to": request['to']})
    
  def getExchangeRates(self, request = {}):
		if not('to' in request) or not request['to']:
			request['to'] = "USD"
       
		return self.request("GET","/market/rates/" + str(request['exchage_id']) + "/" + str(request['from']),{"to" : request['to'],"from_amount": request['from_amount']})
