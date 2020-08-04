from setuptools import setup, find_packages
 
setup(
	name = 'BlockSDK',

	version = '0.1',

	description = 'BlockSDK is an API service for blockchain applications',

	author = 'BlockChen',

	author_email = 'bianconery@blockchen.io',

	url = 'https://blocksdk.com',

	download_url = 'https://github.com/Block-Chen/blocksdk-python',

	install_requires = ['requests'],

	packages = find_packages(exclude = []),

	keywords = ['blocksdk api'],

	python_requires = '>=3',

	package_data = {},

	zip_safef = False,

	classifiers = [ 
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
	],
)
