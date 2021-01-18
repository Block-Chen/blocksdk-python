from BlockSDK.base import Base
from BlockSDK.dash import Dash
from BlockSDK.bitcoin import Bitcoin
from BlockSDK.ethereum import Ethereum
from BlockSDK.bitcoincash import BitcoinCash
from BlockSDK.monero import Monero
from BlockSDK.webhook import WebHook
from BlockSDK.litecoin import Litecoin
from BlockSDK.market import Market
from BlockSDK.token import Token
from BlockSDK.tool import Tool

class BlockSDK(Base):
	def __init__(self, api_token):
		self.api_token = api_token

	def createBitcoin(self):
		return Bitcoin(self.api_token)

	def createEthereum(self):
		return Ethereum(self.api_token)

	def createLitecoin(self):
		return Litecoin(self.api_token)

	def createMonero(self):
		return Monero(self.api_token)

	def createWebHook(self):
		return WebHook(self.api_token)

	def createDash(self):
		return Dash(self.api_token)

	def createBitcoinCash(self):
		return BitcoinCash(self.api_token)
	
	def createMarket(self):
		return Market(self.api_token)
	
	def createToken(self):
		return Token(self.api_token)
	
	def createTool(self):
		return Tool(self.api_token)
