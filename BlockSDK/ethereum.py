from BlockSDK.base import Base


class Ethereum(Base):
    def GetBlockChainInfo(self):
        return self.request("GET", f"/eth/info")

    def GetBlock(self, request):
        return self.request("GET", f"/eth/block/{request.get('block', '')}", request)

    def GetAddresses(self, request):
        return self.request("GET", f"/eth/address", request)

    def CreateAddress(self, request):
        return self.request("POST", f"/eth/address", request)

    def GetAddressInfo(self, request):
        return self.request("GET", f"/eth/address/{request.get('address', '')}/info", request)

    def GetAddressBalance(self, request):
        return self.request("GET", f"/eth/address/{request.get('address', '')}/balance")

    def Send(self, request):
        return self.request("POST", f"/eth/address/{request.get('from', '')}/send", request)

    def SendTransaction(self, request):
        return self.request("POST", f"/eth/transaction/send", request)

    def GetTransaction(self, request):
        return self.request("GET", f"/eth/transaction/{request.get('hash', '')}")

    def GetTokenInfo(self, request):
        return self.request("GET", f"/eth/token/{request.get('contract_address', '')}/info")

    def SendToken(self, request):
        return self.request("POST", f"/eth/token/{request.get('contract_address', '')}/{request.get('from', '')}/transfer", request)

    def GetTokenBalance(self, request):
        return self.request("GET", f"/eth/token/{request.get('contract_address', '')}/{request.get('from', '')}/balance")

    def GetTokenTxs(self, request):
        return self.request("GET", f"/eth/token/{request.get('from_address', '')}/transactions", request)

    def GetTokenContractTxs(self, request):
        return self.request("GET", f"/eth/token/{request.get('contract_address', '')}/{request.get('from_address', '')}/transactions", request)

    def GetTokenAllBalance(self, request):
        return self.request("GET", f"/eth/token/{request.get('from_address', '')}/all-balance", request)

    def GetSingleNfts(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('contract_address', '')}/nfts", request)

    def GetSingleOwnerNfts(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('owner_address', '')}/owner-nfts", request)

    def GetSingleCreatorNfts(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('creator_address', '')}/creator-nfts", request)

    def GetSingleTxs(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('from_address', '')}/transactions", request)

    def GetSingleNftOwnerNfts(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('contract_address', '')}/{request.get('owner_address', '')}/owner-nfts", request)

    def GetSingleNftCreatorNfts(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('contract_address', '')}/{request.get('creator_address', '')}/creator-nfts", request)

    def GetSingleNftTxs(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('contract_address', '')}/{request.get('from_address', '')}/from-transactions", request)

    def GetSingleNftInfo(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('contract_address', '')}/{request.get('token_id', '')}/info", request)

    def GetSingleNftTokenTxs(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('contract_address', '')}/{request.get('token_id', '')}/nft-transactions", request)

    def GetSingleNftAuctionNfts(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('contract_address', '')}/auction-nfts", request)

    def GetSingleNftSellerNfts(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('contract_address', '')}/{request.get('seller_address', '')}/seller-nfts", request)

    def GetSingleNftTokenBids(self, request):
        return self.request("GET", f"/eth/single-nft/{request.get('contract_address', '')}/{request.get('token_id', '')}/nft-bids", request)

    def GetMultiNfts(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('contract_address', '')}/nfts", request)

    def GetMultiOwnerNfts(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('owner_address', '')}/owner-nfts", request)

    def GetMultiCreatorNfts(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('creator_address', '')}/creator-nfts", request)

    def GetMultiTxs(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('from_address', '')}/transactions", request)

    def GetMultiNftOwnerNfts(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('contract_address', '')}/{request.get('owner_address', '')}/owner-nfts", request)

    def GetMultiNftCreatorNfts(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('contract_address', '')}/{request.get('creator_address', '')}/creator-nfts", request)

    def GetMultiNftTxs(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('contract_address', '')}/{request.get('from_address', '')}/from-transactions", request)

    def GetMultiNftInfo(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('contract_address', '')}/{request.get('token_id', '')}/info", request)

    def GetMultiNftTokenTxs(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('contract_address', '')}/{request.get('token_id', '')}/nft-transactions", request)

    def GetMultiNftSellerNfts(self, request):
        return self.request("GET", f"/eth/multi-nft/{request.get('contract_address', '')}/{request.get('seller_address', '')}/seller-nfts", request)

    def ReadContract(self, request):
        return self.request("POST", f"/eth/contract/{request.get('contract_address', '')}/read", request)

    def WriteContract(self, request):
        return self.request("POST", f"/eth/contract/{request.get('contract_address', '')}/write", request)