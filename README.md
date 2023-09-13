# PYTHON REST API SDK for BlockSDK
[![@BLOCKSDK on Twitter](https://img.shields.io/badge/twitter-%40BLOCKSDK-blue.svg)](https://twitter.com/BlockSdk1)
[![@BLOCKSDK on Facebook](https://img.shields.io/badge/facebook-%40BLOCKSDK-blue.svg)](https://www.facebook.com/blocksdk)
[![PYTHON version](https://img.shields.io/pypi/v/BlockSDK.svg)](https://pypi.python.org/pypi/BlockSDK)
[![PYPI downloads](https://img.shields.io/pypi/pyversions/BlockSDK.svg)](https://pypi.python.org/pypi/BlockSDK)

BlockSDK PYTHON에 오신 것을 환영합니다. 이 저장소에는 BlockSDK의 PYTHON SDK와 REST API용 샘플이 포함되어 있습니다.

## 지원중인 블록체인 네트워크
비트코인 , 라이트코인 , 비트코인 캐시 , 웹후크 는 V2버전 에서 지원되고 있습니다.
```
1.이더리움
2.클레이튼  
3.바이낸스 스마트 체인
4.폴리곤
5.아발란체
6.이더리움 클래식
```
## 개발자 문서
* [BlockSDK REST API V3 문서](https://documenter.getpostman.com/view/20292093/Uz5FKwxw)
* [BlockSDK REST API V2 문서](https://docs-v2.blocksdk.com/ko/#fa255f0ccc)
* [BLOCKSDK PYTHON SDK V3 문서](https://github.com/Block-Chen/blocksdk-python/wiki)

## 요구 사양

   - [deasync](https://www.npmjs.com/package/deasync) & [request](https://www.npmjs.com/package/request) extensions must be enabled
   
## 시작하기
SDK 설치 – pip를 사용하여 설치 것이 BLOCKSDK PYTHON SDK를 설치하는 권장 방법입니다.

```sh
pip install BlockSDK
```

## 코드 샘플
### 테스트넷 클라이언트 생성
```python
from BlockSDK.blocksdk import BlockSDK
client = BlockSDK(api_token="YOU_TOKEN")
```
### 메인넷 클라이언트 생성
엔드 포인트를 지정해주지 않는경우 테스트넷으로 기본 설정되어 호출 됩니다
메인넷은 아래 예시와 같이 클라이언트 생성시 두번째 매개변수를 메인넷으로 지정해 주시길 바랍니다.
```python
from BlockSDK.blocksdk import BlockSDK
client = BlockSDK(api_token="YOU_TOKEN",endpoint="https://mainnet-api.blocksdk.com")
```
### 이더리움 블록체인 정보 가져오기
```python
result = client.ethereum.GetBlockChainInfo();
print(result);
```

### 이더리움 테스트넷 특정 컨트렉트 NFT 목록 가져오기
```python
nfts = client.ethereum.GetSingleNfts({
    "contract_address": "0xf5de760f2e916647fd766b4ad9e85ff943ce3a2b",
    "includeMetadata": False,
    "offset": 0,
    "limit": 10
})

print(nfts)
```