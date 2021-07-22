from BlockSDK.base import Base
class Klaytn(Base):
	def getBlockChain(self, request = {}):
		return self.request("GET","/klay/info")		
	
	def getBlock(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
       
		return self.request("GET","/klay/blocks/" + str(request['block']),{"rawtx" : request['rawtx'],"offset": request['offset'],"limit" : request['limit']})
	
	def getMemPool(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/klay/mempool",{"rawtx" : request['rawtx'],"offset" : request['offset'],"limit" : request['limit']})
	
	
	def getAddresses(self, request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/klay/addresses",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
	
	def loadAddress(self, request = {}):
		return self.request("POST","/klay/addresses/" + request['address'] + "/load",{"private_key" : request['private_key'],"password" : request['password']})
	
	def unloadAddress(self, request = {}):
		return self.request("POST","/klay/addresses/" + request['address'] + "/unload")
	
	def createAddress(self, request = {}):
		if not('name' in request) or not request['name']:
			request['name'] = None  	
		return self.request("POST","/klay/addresses",{"name" : request['name']})

	
	def getAddressInfo(self, request = {}):

		if not('reverse' in request) or not request['reverse']:
			request['reverse'] = True
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = None
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/klay/addresses/" + request['address'],{"reverse" : request['reverse'],"rawtx"  : request['rawtx'],"offset" : request['offset'],"limit"  : request['limit']})
	
	
	def getAddressBalance(self, request = {}):
		return self.request("GET","/klay/addresses/" + request['address'] + "/balance")
	
	def sendToAddress(self, request = {}):
		if not('nonce' in request) or not request['nonce']:
			request['nonce'] = None
        if not('data' in request) or not request['data']:
			request['data'] = None
		if not('private_key' in request) or not request['private_key']:
			request['private_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		if not('gas_limit' in request) or not request['gas_limit']:
			request['gas_limit'] = None
		
		return self.request("POST","/klay/addresses/" + request['from'] + "/sendtoaddress",{
            "to" : request['to'],
            "amount" : request['amount'],
            "private_key" : request['private_key'],
            "password" : request['password'],
            "gas_limit" : request['gas_limit']
        })
	
	
	def sendTransaction(self, request = {}):
		return self.request("POST","/klay/transactions/send",{
            "hex" : request['hex']
        })
	
	def getTransaction(self, request = {}):
		return self.request("GET","/klay/transactions/" + request['hash'])
	
	def getKIP7(self, request = {}):
		return self.request("GET","/klay/kip7-tokens/" + request['contract_address'])
	
	def getKIP7Balance(self, request = {}):
		return self.request("GET","/klay/kip7-tokens/" + request['contract_address'] + "/" + request['from'] + "/balance")
	
	def getKIP7Transfer(self, request = {}):
		if not('private_key' in request) or not request['private_key']:
			request['private_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		if not('gas_limit' in request) or not request['gas_limit']:
			request['gas_limit'] = None
		
		return self.request("POST","/klay/kip7-tokens/" + request['contract_address'] + "/" + request['from'] + "/transfer",{
            "to" : request['to'],
            "amount" : request['amount'],
            "private_key" : request['private_key'],
            "password" : request['password'],
            "gas_limit" : request['gas_limit']
        })
        
	def getKIP7Sign(self, request = {}):
		if not('private_key' in request) or not request['private_key']:
			request['private_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		if not('gas_limit' in request) or not request['gas_limit']:
			request['gas_limit'] = None
		
		return self.request("POST","/klay/kip7-tokens/" + request['contract_address'] + "/" + request['from'] + "/sign",{
            "to" : request['to'],
            "amount" : request['amount'],
            "private_key" : request['private_key'],
            "password" : request['password'],
            "gas_limit" : request['gas_limit']
        })
        
	def getKIP7Feedelegated(self, request = {}):
		if not('private_key' in request) or not request['private_key']:
			request['private_key'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		if not('gas_limit' in request) or not request['gas_limit']:
			request['gas_limit'] = None
		
		return self.request("POST","/klay/kip7-tokens/" + request['contract_address'] + "/" + request['fee_payer'] + "/transfer/feedelegated",{
            "from" : request['from'],
            "to" : request['to'],
            "amount" : request['amount'],
            "private_key" : request['private_key'],
            "password" : request['password'],
            "gwei" : request['gwei'],
            "gas_limit" : request['gas_limit'],
            "nonce" : request['nonce'],
            "v" : request['v'],
            "r" : request['r'],
            "s" : request['s']
        })

    def getNfts(self, request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/klay/kip17-tokens/" + request['contract_address'] + "/tokens",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
        
    def getOwnerNfts(self, request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/klay/kip17-tokens/" + request['contract_address'] + "/" + request['owner_address'] + "/owner",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
        
    def getCreatorNfts(self, request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/klay/kip17-tokens/" + request['contract_address'] + "/" + request['creator_address'] + "/creator",{
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
		
		return self.request("GET","/klay/kip17-tokens/" + request['contract_address'] + "/auction",{
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
		
		return self.request("GET","/klay/kip17-tokens/" + request['contract_address'] + "/" + request['seller_address'] + "/sale",{
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
		
		return self.request("GET","/klay/kip17-tokens/" + request['contract_address'] + "/" + request['token_id'] + "/bid",{
			"order_direction" : request['order_direction'],
            "rawtx" : request['rawtx'],
            "offset" : request['offset'],
			"limit" : request['limit']
		})
        
	def getNftInfo(self, request = {}):
		return self.request("GET","/klay/kip17-tokens/" + request['contract_address'] + "/" + request['token_id'] + "/info")
        
	def getNftTransfers(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = 0
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/klay/kip17-tokens/" + request['contract_address'] + "/" + request['token_id'] + "/transfers",{
            "rawtx" : request['rawtx'],
            "offset" : request['offset'],
            "limit" : request['limit']
        })
        
	def getContractRead(self, request = {}):
		if not('parameter_type' in request) or not request['parameter_type']:
			request['parameter_type'] = None
		if not('parameter_data' in request) or not request['parameter_data']:
			request['parameter_data'] = None

		
		return self.request("POST","/klay/contracts/" + request['contract_address'] + "/read",{
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

		
		return self.request("POST","/klay/contracts/" + request['contract_address'] + "/write",{
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
        
	def getContractWriteSign(self, request = {}):
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

		
		return self.request("POST","/klay/contracts/" + request['contract_address'] + "/write/sign",{
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
        
	def getContractWriteFeedelegated(self, request = {}):
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

		
		return self.request("POST","/klay/contracts/" + request['contract_address'] + "/write/feedelegated",{
            "method" : request['method'],
            "return_type" : request['return_type'],
            "parameter_type" : request['parameter_type'],
            "parameter_data" : request['parameter_data'],
            "from" : request['from'],
            "fee_payer" : request['fee_payer'],
            "private_key" : request['private_key'],
            "password" : request['password'],
            "amount" : request['amount'],
            "gwei" : request['gwei'],
            "gas_limit" : request['gas_limit']
        })
        
	def getContractWriteFees(self, request = {}):
		if not('gas_limit' in request) or not request['gas_limit']:
			request['gas_limit'] = None
            
		if not('parameter_type' in request) or not request['parameter_type']:
			request['parameter_type'] = None
		if not('parameter_data' in request) or not request['parameter_data']:
			request['parameter_data'] = None

		
		return self.request("POST","/klay/contracts/" + request['contract_address'] + "/write/fees",{
            "method" : request['method'],
            "return_type" : request['return_type'],
            "parameter_type" : request['parameter_type'],
            "parameter_data" : request['parameter_data'],
            "from" : request['from'],
            "amount" : request['amount'],
            "gas_limit" : request['gas_limit']
        })
