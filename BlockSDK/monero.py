from BlockSDK.base import Base
class Monero(Base):	
	def getBlockChain(self,request = {}):
		return self.request("GET","/xmr/info")
		
	def getBlock(self,request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/xmr/blocks/" + str(request['block']) + "",{
			"rawtx" : request['rawtx'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def getMemPool(self,request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/xmr/mempool",{
			"rawtx" : request['rawtx'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def getAddress(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/xmr/addresses",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
	
	def createAddress(self,request = {}):
		if not('name' in request) or not request['name']:
			request['name'] = None
			
		return self.request("POST","/xmr/addresses",{
			"name" : request['name']
		})

	
	def getAddressInfo(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/xmr/addresses/" + str(request['address_id']) + "",{
			"offset" : request['offset'],
			"limit" : request['limit'],
			"private_spend_key" : request['private_spend_key'],
		})

	
	def getAddressBalance(self,request = {}):
		return self.request("GET","/xmr/addresses/" + str(request['address_id']) + "/balance",{
			"private_spend_key" : request['private_spend_key'],
		})

	def loadAddress(self,request = {}):
		return self.request("POST","/xmr/addresses/" + str(request['address_id']) + "/load",{
			"private_spend_key" : request['private_spend_key'],
			"password" : request['password']
		})

	def unloadAddress(self,request = {}):		
		return self.request("POST","/xmr/address/" + str(request['address_id']) + "/unload")
	
	def sendToAddress(self,request = {}):
		if(not('kbfee' in request) or not request['kbfee']):
			blockChain = self.getBlockChain()
			request['kbfee'] = blockChain['medium_fee_per_kb']

		
		if not('private_spend_key' in request) or not request['private_spend_key']:
			request['private_spend_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		if not('subtractfeefromamount' in request) or not request['subtractfeefromamount']:
			request['subtractfeefromamount'] = False
		
		return self.request("POST","/xmr/addresses/" + str(request['address_id']) + "/sendtoaddress",{
			"address" : request['address'],
			"amount" : request['amount'],
			"private_spend_key" : request['private_spend_key'],
			"password" : request['password'],
			"kbfee" : request['kbfee'],
			"subtractfeefromamount" : request['subtractfeefromamount']
		})

	def sendTransaction(self, request = {}):
		return self.request("POST","/eth/transactions/send",{"hex" : request['hex']})
	
	def getTransaction(self,request = {}):		
		return self.request("GET","/xmr/transactions/" + str(request['hash']) + "")
