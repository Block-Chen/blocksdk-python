from base import Base
class Dash(Base):
	def getBlockChain(self, request = {}):
		return self.request("GET","/dash/block")


	def getBlock(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
       
		return self.request("GET","/dash/block/" + str(request['block']),{"rawtx" : request['rawtx'],"offset": request['offset'],"limit" : request['limit']})
	
	def getMemPool(self, request = {}):
		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = False
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/dash/mempool",{"rawtx" : request['rawtx'],"offset" : request['offset'],"limit" : request['limit']})

	
	def getAddressInfo(self, request = {}):


		if not('rawtx' in request) or not request['rawtx']:
			request['rawtx'] = None
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/dash/address/" + str(request['address']),{"rawtx"  : request['rawtx'],"offset" : request['offset'],"limit"  : request['limit']})
	
	
	def getAddressBalance(self, request = {}):
		return self.request("GET","/dash/address/" + str(request['address']) + "/balance")


	def listWallet(self,request = {}):
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		
		return self.request("GET","/dash/wallet",{
			"offset" : request['offset'],
			"limit" : request['limit']
		})
		
	def createWallet(self,request = {}):

		if not('name' in request) or not request['name']:
			request['name'] = None
		
		return self.request("POST","/dash/wallet",{
			"name" : request['name']
		})
	
	def loadWallet(self,request = {}):
		return self.request("POST","/dash/wallet/" + str(request['wallet_id']) + "/load",{"seed_wif" : request['seed_wif'],"password" : request['password']})
	
	def unLoadWallet(self,request = {}):
		return self.request("POST","/dash/wallet/" + str(request['wallet_id']) + "/unload")
	
	def listWalletAddress(self,request = {}):

		if not('address' in request) or not request['address']:
			request['address'] = None
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		if not('hdkeypath' in request) or not request['hdkeypath']:
			request['hdkeypath'] = None
		
		return self.request("GET","/dash/wallet/" + str(request['wallet_id']) + "/address",{
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
		
		return self.request("POST","/dash/wallet/" + str(request['wallet_id']) + "/address",{
			"seed_wif" : request['seed_wif'],
			"password" : request['password']
		})		
	
	def getWalletBalance(self,request = {}):
		return self.request("GET","/dash/wallet/" + str(request['wallet_id']) + "/balance")
			
	
	def getWalletTransaction(self,request = {}):

		if not('order' in request) or not request['order']:
			request['order'] = 'desc'
		if not('offset' in request) or not request['offset']:
			request['offset'] = 0
		if not('limit' in request) or not request['limit']:
			request['limit'] = 10
		if not('category' in request) or not request['category']:
			request['category'] = 'all'
		
		return self.request("GET","/dash/wallet/" + str(request['wallet_id']) + "/transaction",{
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
		
		return self.request("POST","/dash/wallet/" + str(request['wallet_id']) + "/sendtoaddress",{"address" : request['address'],"amount" : request['amount'],"seed_wif" : request['seed_wif'],"password" : request['password'],"kbfee" : request['kbfee']})
	
	def sendMany(self,request = {}):
		
		if not('seed_wif' in request) or not request['seed_wif']:
			request['seed_wif'] = None
		if not('password' in request) or not request['password']:
			request['password'] = None
		
		return self.request("POST","/dash/wallet/" + str(request['wallet_id']) + "/sendmany",{"to" : request['to'],"seed_wif" : request['seed_wif'],"password" : request['password']})	

	def sendTransaction(self, request = {}):
		return self.request("POST","/dash/transaction",{"sign_hex" : request['sign_hex']})
	
	def getTransaction(self, request = {}):
		return self.request("GET","/dash/transaction/" + request['hash'])		
	