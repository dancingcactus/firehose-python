# Overview
Really simple script to consume the firehose. Basically it will allow you to connect and stream the data down to the terminal in a prettier format. It aslo allows you to slow down how fast it reads firehose or how many messages it downloads from the firehose. 

#Setup
This script requires the requests library see the [installation instructions](http://www.python-requests.org/en/latest/user/install/) for how to install. 

# Usage 
Basic usage 
    
    python firehoser.py -a [ACCESS_TOKEN] -u [FIREHOSE_URL]
    
Slowing down requests to be half a second appart

    python firehoser.py -a [ACCESS_TOKEN] -u [FIREHOSE_URL] -s 0.5
    
Only downloading n number of messages

    python firehoser.py -a [ACCESS_TOKEN] -u [FIREHOSE_URL] -n 10

## Access Tokens
Access tokens can be obtained in a few ways the developer conection has instructions for obtaining an access token. 

## Configuration 
All configuration can be done either as command line parameters or as parameters as a configuration file. Command line parameters will override those parameters in the config file. 

The format of the config file is this. 
	
	[firehose]
	access_token=138256612637...
	firehose_url=https://firehose1.omniture.com/api/1/stream/jgrover-geometrixx
	
By default the script will read sample.conf unless overridden by a command line file

## Parameters 

### -a --access_token (Required)
The OAuth access token. 

*Command Line Usage*

	python firehoser.py -a 138256612637...

*Config File*
	
	access_token=138256612637...
	
### -u --firehose_url (Required)
The complete URL for your firehose stream 

*Command Line Usage*

	python firehoser.py -u "https://firehose1.omniture.com/api/1/stream/jgrover-geometrixx"

*Config File*
	
	firehose_url=https://firehose1.omniture.com/api/1/stream/jgrover-geometrixx
	
### -s --seconds (Optional)	
Number of seconds between each read (can be a decimal)

*Command Line Usage*

	python firehoser.py -s 0.5

*Config File*
	
	seconds=0.5
Defaults to 0

### -n --number (Optional)	
Number of messages to download

*Command Line Usage*

	python firehoser.py -n 10

*Config File*
	
	number=10
	
Defaults to 0

### -c --config_file (Optional)	
A relative URL reference to a custom config file. Allows you to have multiple configs

*Command Line Usage*

	python firehoser.py -c "my_config.conf"

Defaults to sample.conf
