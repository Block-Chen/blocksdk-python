from BlockSDK.base import Base
class Tool(Base):
	def getHashType(self, request = {}):
		return self.request("GET","/tools/hash-type/" + request['hash'])
