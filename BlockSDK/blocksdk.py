from BlockSDK.ethereum import Ethereum
from BlockSDK.avalanche import Avalanche
from BlockSDK.ethereumclassic import EthereumClassic
from BlockSDK.klaytn import Klaytn
from BlockSDK.binancesmart import BinanceSmart
from BlockSDK.polygon import Polygon


class BlockSDK:

	def __init__(self, api_token, endpoint="https://testnet-api.blocksdk.com"):
		self.ethereum = Ethereum(api_token=api_token, endpoint=endpoint)
		self.avalanche = Avalanche(api_token=api_token, endpoint=endpoint)
		self.ethereum_classic = EthereumClassic(api_token=api_token, endpoint=endpoint)
		self.klaytn = Klaytn(api_token=api_token, endpoint=endpoint)
		self.binance_smart = BinanceSmart(api_token=api_token, endpoint=endpoint)
		self.polygon = Polygon(api_token=api_token, endpoint=endpoint)
