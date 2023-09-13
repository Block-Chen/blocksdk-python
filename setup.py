from setuptools import setup, find_packages

setup(
	name = 'BlockSDK',

	version = '3.0.0',

	description = 'BlockSDK is an API service for blockchain applications',

	long_description=open('README.md', encoding='utf-8').read(),

	long_description_content_type='text/markdown',

	license_file='LICENSE',

	author = 'BlockChen',

	author_email = 'bianconery@blockchen.io',

	url = 'https://blocksdk.com',

	download_url = 'https://github.com/Block-Chen/blocksdk-python',

	install_requires = ['requests'],

	packages = find_packages(exclude = []),

	keywords = ['blocksdk api'],

	python_requires = '>=3',

	package_data = {},

	zip_safe = False,

	classifiers = [ 
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.7',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3.9',
	],
)
