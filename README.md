# PYTHON REST API SDK for BlockSDK
[![@BLOCKSDK on Twitter](https://img.shields.io/badge/twitter-%40BLOCKSDK-blue.svg)](https://twitter.com/BlockSdk)
[![@BLOCKSDK on Facebook](https://img.shields.io/badge/facebook-%40BLOCKSDK-blue.svg)](https://www.facebook.com/blocksdk)
[![PYTHON version](https://img.shields.io/pypi/v/BlockSDK.svg)](https://pypi.python.org/pypi/BlockSDK)
[![PYPI downloads](https://img.shields.io/pypi/pyversions/BlockSDK.svg)](https://pypi.python.org/pypi/BlockSDK)
[![DOCS](https://readthedocs.org/projects/sagemaker/badge/?version=stable)](https://docs.blocksdk.com/)

__Welcome to BlockSDK PYTHON__. This repository contains BlockSDK's PHP SDK and samples for REST API.

## SDK Documentation
[ Our BlockSDK-PYTHON Page ](https://docs.blocksdk.com/) includes all the documentation related to JS SDK. Sample Codes, to Releases. Here are few quick links to get you there faster.
* [ BlockSDK Developer Docs]

## Prerequisites

   - [deasync](https://www.npmjs.com/package/deasync) & [request](https://www.npmjs.com/package/request) extensions must be enabled
   
### In PYTHON

The preferred way to install the BlockSDK for Python is to use the
[pypi](https://pypi.org/) package manager for Python. Simply type the following
into a terminal window:

```sh
pip install BlockSDK
```

## Quick Examples
### Create an Bitcoin client
```python

blockSDK = BlockSDK("YOU TOKEN")
btcClient = blockSDK.createBitcoin()
```
### Get Address info
```python
addressInfo = btcClient.getAddressInfo({
    "address" : "18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX",
    "rawtx" : true,
    "reverse" : true,
    "offset" : 0,
    "limit" : 10
})

print(addressInfo)
```

### Create an Bitcoin Wallet
```python
wallet = btcClient.createWallet({
    "name" : "test"
})
```

[install-packagist]: https://packagist.org/packages/block-chen/blocksdk-php
[npm]:(http://npmjs.org)
[packagist]: http://packagist.org
[BlockSDK Developer Docs]: https://docs.blocksdk.com
