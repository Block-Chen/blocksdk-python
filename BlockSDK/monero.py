from base import Base
class Monero(Base):	
	def getBlockChain(self,request = {}):
		return self.request("GET","/xmr/block")
		
	def getBlock(self,request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/xmr/block/" + str(request['block']) + "",{
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

	
	def listAddress(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/xmr/address",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
	
	def createAddress(self,request = {}):
		if not('name' in request) or not request['name']:
			request['name'] = None
			
		return self.request("POST","/xmr/address",{
			"name" : request['name']
		})

	
	def getAddressInfo(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/xmr/address/" + str(request['address_id']) + "",{
			"offset" : request['offset'],
			"limit" : request['limit'],
			"private_spend_key" : request['private_spend_key'],
		})

	
	def getAddressBalance(self,request = {}):
		return self.request("GET","/xmr/address/" + str(request['address_id']) + "/balance",{
			"private_spend_key" : request['private_spend_key'],
		})

	def loadAddress(self,request = {}):
		return self.request("POST","/xmr/address/" + str(request['address_id']) + "/load",{
			"private_spend_key" : request['private_spend_key'],
			"password" : request['password']
		})

	def unLoadAddress(self,request = {}):		
		return self.request("POST","/xmr/address/" + str(request['address_id']) + "/unload")
	
	def sendToAddress(self,request = {}):
		if(not('kbfee' in request) or not request['kbfee']):
			blockChain = self.getBlockChain()
			request['kbfee'] = blockChain['medium_fee_per_kb']

		
		if not('private_spend_key' in request) or not request['private_spend_key']:
			request['private_spend_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		
		return self.request("POST","/xmr/address/" + str(request['address_id']) + "/sendtoaddress",{
			"address" : request['address'],
			"amount" : request['amount'],
			"private_spend_key" : request['private_spend_key'],
			"password" : request['password'],
			"kbfee" : request['kbfee']
		})

	def getTransaction(self,request = {}):		
		return self.request("GET","/xmr/transaction/" + str(request['hash']) + "")