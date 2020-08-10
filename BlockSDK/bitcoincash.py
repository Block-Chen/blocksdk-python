from BlockSDK.base import Base
class BitcoinCash(Base):
	def getBlockChain(self,request = {}):		
		return self.request("GET","/bch/block")
	
	def getBlock(self,request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/bch/block/" + str(request['block']) + "",{
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
		
		return self.request("GET","/bch/mempool",{
			"rawtx" : request['rawtx'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def getAddressInfo(self,request = {}):

		if not('reverse' in request) or not request['reverse']:
			request['reverse'] = True
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = None
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/bch/address/" + str(request['address']) + "",{
			"reverse" : request['reverse'],
			"rawtx" : request['rawtx'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def getAddressBalance(self,request = {}):
		return self.request("GET","/bch/address/" + str(request['address']) + "/balance")
	 
	def listWallet(self,request = {}):

		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/bch/wallet",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def createWallet(self,request = {}):
		if not('name' in request) or not request['name']:
			request['name'] = None
		
		return self.request("POST","/bch/wallet",{
			"name" : request['name']
		})

	
	def loadWallet(self,request = {}):
		return self.request("POST","/bch/wallet/" + str(request['wallet_id']) + "/load",{
			"seed_wif" : request['seed_wif'],
			"password" : request['password']
		})

	
	def unLoadWallet(self,request = {}):
		return self.request("POST","/bch/wallet/" + str(request['wallet_id']) + "/unload")

	
	def listWalletAddress(self,request = {}):

		if not('address' in request) or not request['address']:
			request['address'] = None
		if not('hdkeypath' in request) or not request['hdkeypath']:
			request['hdkeypath'] = None
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/bch/wallet/" + str(request['wallet_id']) + "/address",{
			"address" : request['address'],
			"hdkeypath" : request['hdkeypath'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def createWalletAddress(self,request = {}):
		if not('seed_wif' in request) or not request['seed_wif']:
			request['seed_wif'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		
		return self.request("POST","/bch/wallet/" + str(request['wallet_id']) + "/address",{
			"seed_wif" : request['seed_wif'],
			"password" : request['password']
		})
		
	
	def getWalletBalance(self,request = {}):
		return self.request("GET","/bch/wallet/" + str(request['wallet_id']) + "/balance")

	def getWalletTransaction(self,request = {}):

		if not('order' in request) or not request['order']:
			request['order'] = 'desc'
		if not('category' in request) or not request['category']:
			request['category'] = 'all'
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/bch/wallet/" + str(request['wallet_id']) + "/transaction",{
			"category" : request['category'],
			"order" : request['order'],
			"offset" : request['offset'],
			"limit" : request['limit']
		})

	
	def sendToAddress(self,request = {}):
		if(not('kbfee' in request) or not request['kbfee']):
			blockChain = self.getBlockChain()
			request['kbfee'] = blockChain['medium_fee_per_kb']

		if not('seed_wif' in request) or not request['seed_wif']:
			request['seed_wif'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		
		return self.request("POST","/bch/wallet/" + str(request['wallet_id']) + "/sendtoaddress",{
			"address" : request['address'],
			"amount" : request['amount'],
			"seed_wif" : request['seed_wif'],
			"password" : request['password'],
			"kbfee" : request['kbfee']
		})

	
	def sendMany(self,request = {}):
		
		if not('seed_wif' in request) or not request['seed_wif']:
			request['seed_wif'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		
		return self.request("POST","/bch/wallet/" + str(request['wallet_id']) + "/sendmany",{
			"to" : request['to'],
			"seed_wif" : request['seed_wif'],
			"password" : request['password']
		})
	
	def getTransaction(self,request = {}):
		return self.request("GET","/bch/transaction/" + str(request['hash']) + "")


