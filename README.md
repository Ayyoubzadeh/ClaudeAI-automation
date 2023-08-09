# SeleniumGPT
Automatic ClaudeAI data extraction using selenium without email or api key.
<br />
This Python script uses the Selenium library to automate interactions with the Claude.ai website. It then imports several modules from Selenium, including the Chrome driver, options, keys, and wait. The script defines several functions that interact with the Claude.ai website, including functions to log in, enter text, click buttons, and extract data. The script also defines a function to generate a temporary email address using the Temp Mail website. The script repeatedly calls the extractDataFromCaludeAI function with a prompt until it returns a valid response. If the function returns an error, the script restarts the Chrome driver and logs in again.
# Setup
0. Install Python :smiley:
1. Copy ChromeDriver to scripts folder
2. Install selenium
```
pip install selenium
```
3. Change sample prompt
```
prompt='please answer 2+17'
```
# Run
Run py file. :wink:
