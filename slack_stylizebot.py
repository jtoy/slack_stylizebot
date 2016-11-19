import os
import time
from slackclient import SlackClient
import random

# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "stylize"

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

somatic_api_key=os.environ.get("SOMATIC_API_KEY")

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."

    print(command)

    if command.startswith("help"):
        response = "Send me a command 'stylize IMAGE_URL' to stylize the image in a random style. Or you can pick a style from http://www.somatic.io/models/list and say 'stylize IMAGE_URL STYLE_ID'" 
        slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
    elif command.startswith(EXAMPLE_COMMAND):
        print("ASDSDASDAS")
        print(command)

        command_data = command.split(' ')
        print(command_data)

        if len(command_data) >= 2:
            image_url = command_data[1]
            # if len(command_data) >= 3:
            #     stylize_id = command_data[2]
            # else:
            stylize_ids=['gZDA63Ex','9kgYo1Zp','MZJNYmZY','MkeLoMEg','lEVv8vEB','2kRl49ZW','oEG3P0ER','Bka9oBkM','zZP0evZ0','VEqz4xkx','8k8aLmnM','LnL71DkK','DkMl3OEg','zZP0RvZ0','MZJN75ZY','yE72lBZm','Kkb1r4EO','7E9r2WkR','VEqzYpkx','LnL7oLkK','7ZxJo3k9']
            stylize_id=random.choice(stylize_ids)
            response = 'http://convert.somatic.io/api/v1.2/cdn-query?id='+stylize_id+'&api_key='+somatic_api_key+'&--input='+image_url[1:-1]
            slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
    else:
        slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StylizeBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
