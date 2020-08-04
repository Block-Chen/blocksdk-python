from base import Base
from dash import Dash
from bitcoin import Bitcoin
from ethereum import Ethereum
from bitcoincash import BitcoinCash
from monero import Monero
from webhook import WebHook
from litecoin import Litecoin
from price import Price

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

	def createPrice(self):
		return Price(self.api_token)

	def createWebHook(self):
		return WebHook(self.api_token)

	def createDash(self):
		return Dash(self.api_token)

	def createBitcoinCash(self):
		return BitcoinCash(self.api_token)
