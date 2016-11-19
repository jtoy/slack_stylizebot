# slack_stylizebot
## Usage
### Step 1: Install virtualenv
`$ [sudo] pip install virtualenv`
Use sudo if there's permission issue.
### Step 2: Establishing the environment
```
virtualenv name_of_your_bot
```
This command will generate a virtualenv only for your bot. Active it using the command below:
```
source name_of_your_bot/bin/activate
```
### Step 3: Install dependencies in your environment
`pip install slackclient pyopenssl ndg-httpsclient pyasn1`
### Step 4: Create a bot on api.slack.com
Please follow: https://www.fullstackpython.com/blog/build-first-slack-bot-python.html
### Step 5: Put two python file into yout bot folder
Copy print_bot_id.py and slack_stylizebot.py into name_of_your_bot.
### Step 6: Set up environment variables
```
export SOMATIC_API_KEY='your somatic_api_key pasted here'
export SLACK_BOT_TOKEN='your slack token pasted here'
export BOT_ID='bot id returned by python print_bot_id.py'
```
### Step 7: Run the bot and play with it
`python starterbot.py`
This command above will start the bot. Play with it in the slak!
##Notice
When pass image link to the bot, make sure the link is a real image.
