from BlockSDK.base import Base
class Bitcoin(Base):
	def getBlockChain(self,request = {}):
		return self.request("GET","/btc/info")
	
	def getBlock(self,request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
			
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/btc/blocks/" + str(request['block']),{
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
		
		return self.request("GET","/btc/mempool",{
			"rawtx" : request['rawtx'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def getAddressInfo(self,request = {}):
		if not('reverse' in request) or not request['reverse']:
			request['reverse'] = True
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/btc/addresses/{request['address']}",{
			"reverse" : request['reverse'],
			"rawtx" : request['rawtx'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def getAddressBalance(self,request = {}):
		return self.request("GET","/btc/addresses/{request['address']}/balance")
	 
	def getWallets(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/btc/wallets",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def createHdWallet(self,request = {}):
		if not('name' in request) or not request['name']:
			request['name'] = None
		
		return self.request("POST","/btc/wallet/hd",{
			"name" : request['name']
		})
	
	def loadWallet(self,request = {}):

		return self.request("POST","/btc/wallets/" + str(request['wallet_id']) + "/load",{
			"wif" : request['wif'],
			"password" : request['password']
		})

	def unloadWallet(self,request = {}):
		return self.request("POST","/btc/wallets/" + str(request['wallet_id']) + "/unload")
	
	def getWalletAddress(self,request = {}):
		if not('address' in request) or not request['address']:
			request['address'] = None
		if not('hdkeypath' in request) or not request['hdkeypath']:
			request['hdkeypath'] = None
		
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/btc/wallets/" + str(request['wallet_id']) + "/addresses",{
			"address" : request['address'],
			"hdkeypath" : request['hdkeypath'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})
	
	def createWalletAddress(self,request = {}):
		if not('wif' in request) or not request['wif']:
			request['wif'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		
		return self.request("POST","/btc/wallets/" + str(request['wallet_id']) + "/addresses",{
			"wif" : request['wif'],
			"password" : request['password']
		})
	
	def getWalletBalance(self,request = {}):	
		return self.request("GET","/btc/wallets/" + str(request['wallet_id']) + "/balance")		
	
	def getWalletTransactions(self,request = {}):
		if not('order' in request) or not request['order']:
			request['order'] = 'desc'
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		if not('type' in request) or not request['type']:
			request['type'] = 'all'

		return self.request("GET","/btc/wallets/" + str(request['wallet_id']) + "/transaction",{
			"type" : request['type'],
			"order" : request['order'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})
		
	def sendToAddress(self,request = {}):
		if(not('kbfee' in request) or not request['kbfee']):
			blockChain = self.getBlockChain()
			request['kbfee'] = blockChain['medium_fee_per_kb']

		
		if not('wif' in request) or not request['wif']:
			request['wif'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		
		return self.request("POST","/btc/wallets/" + str(request['wallet_id']) + "/sendtoaddress",{
			"address" : request['address'],
			"amount" : request['amount'],
			"wif" : request['wif'],
			"password" : request['password'],
			"kbfee" : request['kbfee']
		})
	
	def sendMany(self,request = {}):
		
		if not('wif' in request) or not request['wif']:
			request['wif'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		
		return self.request("POST","/btc/wallets/" + str(request['wallet_id']) + "/sendmany",{
			"to" : request['to'],
			"wif" : request['wif'],
			"password" : request['password']
		})

	def sendTransaction(self,request = {}):
		return self.request("POST","/btc/transactions/send",{
			"hex" : request['hex']
		})
	
	def getTransaction(self,request = {}):
		return self.request("GET","/btc/transactions/" + str(request['hash']) + "")
