# twitter-user-emulation
A simple twitter "bot" using Selenium to login to Twitter without using Twitter's API.

This script was built as an experiment using Selenium to login to Twitter as a bot may and tested in PyCharm.

## Install

You'll need to install Selenium via pip in your IDE's terminal.

`pip install selenium`

The only other installation is *chromedriver_autoinstaller* which installs and sets the path to chromes browser engine for Selenium to use. However, we won't pip install, chromedriver_autoinstaller is run as part of the script.

## Usage

Steps:

1. Enter your Twitter username and password at the bottom of the script on line 55.

2. Press the run button (typicall a play button right-facing arrow) in your IDE, or run manually via your IDE's terminal.

## Possible issues

### 1. The login URL may be different. 

At the time of writing Twitter's login page was "https://twitter.com/i/flow/login".

### 2. The XPATH to the username and/or password form fields may be different. 

You can find the new XPATH by using inspect element on Twitter's login page. 
