from BlockSDK.base import Base
class Token(Base):
	def getUsages(self, request = {}):
		return self.request("POST","/token/usage",{"stat_date" : request['stat_date'],"end_date" : request['end_date']})
