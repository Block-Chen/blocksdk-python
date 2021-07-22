from BlockSDK.base import Base
class Market(Base):
	def getExchanges(self, request = {}):
		return self.request("GET","/market/exchanges")		

	def getAssets(self, request = {}):
		return self.request("GET","/market/assets")		

	def getAsset(self, request = {}):
		return self.request("GET","/market/assets/" + request['asset_id'])		

	def getOhlcvLast(self, request = {}):
		return self.request("GET","/market/ohlcv/latest",request)		

	def getOhlcvHistory(self, request = {}):
		return self.request("GET","/market/ohlcv/history/" + request['symbol'],request)		
	
	def getExchangeOhlcvLast(self, request = {}):
		return self.request("GET","/market/ohlcv/" + request['exchage_id'] + "/latest",request)		
	
	def getExchangeOhlcvHistory(self, request = {}):
		return self.request("GET","/market/ohlcv/" + request['exchage_id'] + "/history/" + request['symbol'],request)		
	
	def getTrades(self, request = {}):
		if not('from' in request) or not request['from']:
			request['from'] = None
		if not('to' in request) or not request['to']:
			request['to'] = "USD"
       
		return self.request("GET","/market/trades/",{
		    "from" : request['from'],
		    "to": request['to']
		})
    
    	def getRates(self, request = {}):
       
		return self.request("GET","/market/rates/" + request['from'],{
		    "to" : request['to'],
		    "from_amount": request['from_amount']
		})
    
   	 def getExchangeTrades(self, request = {}):
		if not('from' in request) or not request['from']:
			request['from'] = None
		if not('to' in request) or not request['to']:
			request['to'] = "USD"
       
		return self.request("GET","/market/trades/" + request['exchage_id'],{
		    "from" : request['from'],
		    "to": request['to']
		})
    
   	 def getExchangeRates(self, request = {}):
		if not('to' in request) or not request['to']:
			request['to'] = "USD"
       
		return self.request("GET","/market/rates/" + str(request['exchage_id']) + "/" + str(request['from']),{
		    "to" : request['to'],
		    "from_amount": request['from_amount']
		})
