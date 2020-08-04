from base import Base
class Price(Base):
	def listPrice(self,request = {}):
			return self.request("GET","/price")
# price = Price('B1zZARyW1d2FdqWxPUpB79izHmtAc2Az693WF9DD')
# print(price.listPrice())