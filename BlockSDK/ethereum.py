from BlockSDK.base import Base
class Ethereum(Base):
	def getBlockChain(self, request = {}):
		return self.request("GET","/eth/info")		
	
	def getBlock(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
       
		return self.request("GET","/eth/blocks/" + str(request['block']),{"rawtx" : request['rawtx'],"offset": request['offset'],"limit" : request['limit']})
	
	def getMemPool(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/mempool",{"rawtx" : request['rawtx'],"offset" : request['offset'],"limit" : request['limit']})
	
	
	def getAddresses(self, request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/addresses",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
	
	def loadAddress(self, request = {}):
		return self.request("POST","/eth/addresses/" + request['address'] + "/load",{"private_key" : request['private_key'],"password" : request['password']})
	
	def unloadAddress(self, request = {}):
		return self.request("POST","/eth/addresses/" + request['address'] + "/unload")
	
	def createAddress(self, request = {}):
		if not('name' in request) or not request['name']:
			request['name'] = None  	
		return self.request("POST","/eth/addresses",{"name" : request['name']})

	
	def getAddressInfo(self, request = {}):

		if not('reverse' in request) or not request['reverse']:
			request['reverse'] = True
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = None
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/addresses/" + request['address'],{"reverse" : request['reverse'],"rawtx"  : request['rawtx'],"offset" : request['offset'],"limit"  : request['limit']})
	
	
	def getAddressBalance(self, request = {}):
		return self.request("GET","/eth/addresses/" + request['address'] + "/balance")
	
	def sendToAddress(self, request = {}):
		if not('gwei' in request) or not request['gwei']:
			blockChain = self.getBlockChain()
			request['gwei'] = blockChain['medium_gwei']
		if not('private_key' in request) or not request['private_key']:
			request['private_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		if not('gas_limit' in request) or not request['gas_limit']:
			request['gas_limit'] = None
		
		return self.request("POST","/eth/addresses/" + request['from'] + "/sendtoaddress",{"to" : request['to'],"amount" : request['amount'],"private_key" : request['private_key'],"password" : request['password'],"gwei" : request['gas_limit'],"gwei" : request['gas_limit']})
	
	
	def sendTransaction(self, request = {}):
		return self.request("POST","/eth/transactions/send",{"hex" : request['hex']})
	
	def getTransaction(self, request = {}):
		return self.request("GET","/eth/transactions/" + request['hash'])
	
	def getErc20(self, request = {}):
		return self.request("GET","/eth/erc20-tokens/" + request['contract_address'])
	
	def getErc20Balance(self, request = {}):
		return self.request("GET","/eth/erc20-tokens/" + request['contract_address'] + "/" + request['from'] + "/balance")
	
	def getErc20Transfer(self, request = {}):
		if not('gwei' in request) or not request['gwei']:
			blockChain = self.getBlockChain()
			request['gwei'] = blockChain['high_gwei']
		if not('private_key' in request) or not request['private_key']:
			request['private_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		if not('gas_limit' in request) or not request['gas_limit']:
			request['gas_limit'] = None
		
		return self.request("POST","/eth/erc20-tokens/" + request['contract_address'] + "/" + request['from'] + "/transfer",{"to" : request['to'],"amount" : request['amount'],"private_key" : request['private_key'],"password" : request['password'],"gwei" : request['gas_limit'],"gwei" : request['gas_limit']})


# ethereum = Ethereum('B1zZARyW1d2FdqWxPUpB79izHmtAc2Az693WF9DD')
# print(ethereum.getBlockChain({        "block" : 8913145,
#     "offset" : 0,
#     "limit" : 10,
#     "rawtx" : True}))
