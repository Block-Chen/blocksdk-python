from base import Base
class Ethereum(Base):
	def getBlockChain(self, request = {}):
		return self.request("GET","/eth/block")		
	
	def getBlock(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
       
		return self.request("GET","/eth/block/" + str(request['block']),{"rawtx" : request['rawtx'],"offset": request['offset'],"limit" : request['limit']})
	
	def getMemPool(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/mempool",{"rawtx" : request['rawtx'],"offset" : request['offset'],"limit" : request['limit']})
	
	
	def listAddress(self, request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/address",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
	
	def loadAddress(self, request = {}):
		return self.request("POST","/eth/address/" + request['address'] + "/load",{"seed_wif" : request['seed_wif'],"password" : request['password']})
	
	def unLoadAddress(self, request = {}):
		return self.request("POST","/eth/address/" + request['address'] + "/unload")
	
	def createAddress(self, request = {}):
		if not('name' in request) or not request['name']:
			request['name'] = None  	
		return self.request("POST","/eth/address",{"name" : request['name']})

	
	def getAddressInfo(self, request = {}):

		if not('reverse' in request) or not request['reverse']:
			request['reverse'] = True
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = None
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/address/" + request['address'],{"reverse" : request['reverse'],"rawtx"  : request['rawtx'],"offset" : request['offset'],"limit"  : request['limit']})
	
	
	def getAddressBalance(self, request = {}):
		return self.request("GET","/eth/address/" + request['address'] + "/balance")
	
	def sendToAddress(self, request = {}):
		if not('gwei' in request) or not request['gwei']:
			blockChain = self.getBlockChain()
			request['gwei'] = blockChain['medium_gwei']
		if not('private_key' in request) or not request['private_key']:
			request['private_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		
		return self.request("POST","/eth/address/" + request['from'] + "/sendtoaddress",{"address" : request['to'],"amount" : request['amount'],"private_key" : request['private_key'],"password" : request['password'],"gwei" : request['gwei']})
	
	
	def sendTransaction(self, request = {}):
		return self.request("POST","/eth/transaction",{"sign_hex" : request['sign_hex']})
	
	def getTransaction(self, request = {}):
		return self.request("GET","/eth/transaction/" + request['hash'])


# ethereum = Ethereum('B1zZARyW1d2FdqWxPUpB79izHmtAc2Az693WF9DD')
# print(ethereum.getBlockChain({        "block" : 8913145,
#     "offset" : 0,
#     "limit" : 10,
#     "rawtx" : True}))