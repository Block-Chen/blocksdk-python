# JS REST API SDK for BlockSDK
[![@BLOCKSDK on Twitter](https://img.shields.io/badge/twitter-%40BLOCKSDK-blue.svg)](https://twitter.com/BlockSdk)
[![@BLOCKSDK on Facebook](https://img.shields.io/badge/facebook-%40BLOCKSDK-blue.svg)](https://www.facebook.com/blocksdk)
[![NPM version](https://img.shields.io/pypi/v/BlockSDK.svg)](https://pypi.python.org/pypi/BlockSDK)
[![NPM downloads](https://img.shields.io/npm/dm/blocksdk-js.svg)](https://www.npmjs.com/package/blocksdk-js)

__Welcome to BlockSDK PYTHON__. This repository contains BlockSDK's PHP SDK and samples for REST API.

## SDK Documentation
[ Our BlockSDK-JS Page ](https://docs.blocksdk.com/) includes all the documentation related to JS SDK. Sample Codes, to Releases. Here are few quick links to get you there faster.
* [ BlockSDK Developer Docs]

## Prerequisites

   - [deasync](https://www.npmjs.com/package/deasync) & [request](https://www.npmjs.com/package/request) extensions must be enabled
   
### In Node.js

The preferred way to install the BlockSDK for Node.js is to use the
[npm](http://npmjs.org) package manager for Node.js. Simply type the following
into a terminal window:

```sh
npm install blocksdk-js
```

## Quick Examples
### Create an Bitcoin client
```javascript

var blockSDK = new BlockSDK("");
var btcClient = blockSDK.createBitcoin();	
```
### Get Address info
```javascript
var addressInfo = btcClient.getAddressInfo({
    "address" : "18cBEMRxXHqzWWCxZNtU91F5sbUNKhL5PX",
    "rawtx" : true,
    "reverse" : true,
    "offset" : 0,
    "limit" : 10
});

console.log(addressInfo);
```

### Create an Bitcoin Wallet
```javascript
var wallet = btcClient.createWallet({
    "name" : "test"
});
```

[install-packagist]: https://packagist.org/packages/block-chen/blocksdk-php
[npm]:(http://npmjs.org)
[packagist]: http://packagist.org
[BlockSDK Developer Docs]: https://docs.blocksdk.com
