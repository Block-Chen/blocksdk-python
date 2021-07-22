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
       
		return self.request("GET","/eth/blocks/" + str(request['block']),{
            "rawtx" : request['rawtx'],
            "offset": request['offset'],
            "limit" : request['limit']
        })
	
	def getMemPool(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/mempool",{
            "rawtx" : request['rawtx'],
            "offset" : request['offset'],
            "limit" : request['limit']
        })
	
	
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
		return self.request("POST","/eth/addresses/" + request['address'] + "/load",{
            "private_key" : request['private_key'],
            "password" : request['password']
        })
	
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
		
		return self.request("GET","/eth/addresses/" + request['address'],{
            "reverse" : request['reverse'],
            "rawtx"  : request['rawtx'],
            "offset" : request['offset'],
            "limit"  : request['limit']
        })
	
	
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
		
		return self.request("POST","/eth/addresses/" + request['from'] + "/sendtoaddress",{
            "to" : request['to'],
            "amount" : request['amount'],
            "private_key" : request['private_key'],
            "password" : request['password'],
            "gwei" : request['gwei'],
            "gas_limit" : request['gas_limit']
        })
	
	
	def sendTransaction(self, request = {}):
		return self.request("POST","/eth/transactions/send",{
            "hex" : request['hex']
        })
	
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
		
		return self.request("POST","/eth/erc20-tokens/" + request['contract_address'] + "/" + request['from'] + "/transfer",{
            "to" : request['to'],
            "amount" : request['amount'],
            "private_key" : request['private_key'],
            "password" : request['password'],
            "gwei" : request['gwei'],
            "gas_limit" : request['gas_limit']
        })

    def getNfts(self, request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/erc721-tokens/" + request['contract_address'] + "/tokens",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
        
    def getOwnerNfts(self, request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/erc721-tokens/" + request['contract_address'] + "/" + request['owner_address'] + "/owner",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
        
    def getCreatorNfts(self, request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/erc721-tokens/" + request['contract_address'] + "/" + request['creator_address'] + "/creator",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
        
    def getAuctionNfts(self, request = {}):
		if not('order_by' in request) or not request['order_by']:
			request['order_by'] = 'end_time'
		if not('order_direction' in request) or not request['order_direction']:
			request['order_direction'] = 'desc'
        if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/erc721-tokens/" + request['contract_address'] + "/auction",{
			"order_by" : request['order_by'],
            "order_direction" : request['order_direction'],
            "offset" : request['offset'],
			"limit" : request['limit']
		})
        
    def getSaleNfts(self, request = {}):
		if not('order_direction' in request) or not request['order_direction']:
			request['order_direction'] = 'desc'
        if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/erc721-tokens/" + request['contract_address'] + "/" + request['seller_address'] + "/sale",{
			"order_direction" : request['order_direction'],
            "offset" : request['offset'],
			"limit" : request['limit']
		})
        
    def getNftBids(self, request = {}):
        if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = 0
		if not('order_direction' in request) or not request['order_direction']:
			request['order_direction'] = 'desc'
        if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/erc721-tokens/" + request['contract_address'] + "/" + request['token_id'] + "/bid",{
			"order_direction" : request['order_direction'],
            "rawtx" : request['rawtx'],
            "offset" : request['offset'],
			"limit" : request['limit']
		})
        
	def getNftInfo(self, request = {}):
		return self.request("GET","/eth/erc721-tokens/" + request['contract_address'] + "/" + request['token_id'] + "/info")
        
	def getNftTransfers(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = 0
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/eth/erc721-tokens/" + request['contract_address'] + "/" + request['token_id'] + "/transfers",{
            "rawtx" : request['rawtx'],
            "offset" : request['offset'],
            "limit" : request['limit']
        })
        
	def getContractRead(self, request = {}):
		if not('parameter_type' in request) or not request['parameter_type']:
			request['parameter_type'] = None
		if not('parameter_data' in request) or not request['parameter_data']:
			request['parameter_data'] = None

		
		return self.request("POST","/eth/contracts/" + request['contract_address'] + "/read",{
            "method" : request['method'],
            "return_type" : request['return_type'],
            "parameter_type" : request['parameter_type'],
            "parameter_data" : request['parameter_data']
        })

	def getContractWrite(self, request = {}):
		if not('private_key' in request) or not request['private_key']:
			request['private_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		if not('gas_limit' in request) or not request['gas_limit']:
			request['gas_limit'] = None
            
		if not('parameter_type' in request) or not request['parameter_type']:
			request['parameter_type'] = None
		if not('parameter_data' in request) or not request['parameter_data']:
			request['parameter_data'] = None

		
		return self.request("POST","/eth/contracts/" + request['contract_address'] + "/write",{
            "method" : request['method'],
            "return_type" : request['return_type'],
            "parameter_type" : request['parameter_type'],
            "parameter_data" : request['parameter_data'],
            "from" : request['from'],
            "private_key" : request['private_key'],
            "password" : request['password'],
            "amount" : request['amount'],
            "gas_limit" : request['gas_limit']
        })
        
	def getContractWriteFees(self, request = {}):
		if not('gas_limit' in request) or not request['gas_limit']:
			request['gas_limit'] = None
            
		if not('parameter_type' in request) or not request['parameter_type']:
			request['parameter_type'] = None
		if not('parameter_data' in request) or not request['parameter_data']:
			request['parameter_data'] = None

		
		return self.request("POST","/eth/contracts/" + request['contract_address'] + "/write/fees",{
            "method" : request['method'],
            "return_type" : request['return_type'],
            "parameter_type" : request['parameter_type'],
            "parameter_data" : request['parameter_data'],
            "from" : request['from'],
            "amount" : request['amount'],
            "gas_limit" : request['gas_limit']
        })
