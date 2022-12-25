import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import random
from fsm import TocMachine
from utils import send_text_message, send_carousel_message, send_button_message, send_image_message

load_dotenv()


machine = TocMachine(
    states=[
        'input_select',
        'input_language',
        'input_num',
        'input_check',
        'send',
    ],
    transitions=[
        {'trigger': 'advance', 'source': 'user', 'dest': 'input_language', 'conditions': 'is_going_to_input_language'},
        {'trigger': 'advance', 'source': 'input_language', 'dest': 'input_select', 'conditions': 'is_going_to_input_select'},
        {'trigger': 'advance', 'source': 'input_select', 'dest': 'input_num', 'conditions': 'is_going_to_input_num'},
        {'trigger': 'advance', 'source': 'input_num', 'dest': 'input_check', 'conditions': 'is_going_to_input_check'},
        {'trigger': 'advance', 'source': 'input_check', 'dest': 'send', 'conditions': 'is_going_to_send'},
        {
            'trigger': 'go_back',
            'source': [
                'input_select',
                'input_language',
                'input_num',
                'input_check',
                'send',
            ],
            'dest': 'user'
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path='')

os.environ['LINE_CHANNEL_SECRET'] = '242bb133047a8c705d54a83c57a45c56'
os.environ['LINE_CHANNEL_ACCESS_TOKEN'] = 'GOXF+HWsyEgiSv3kJ5e1YUY0MKZTWhxIWVodq1NUjBtRZKid9Y6Micop/EPUdEx0BVNMxVGQpcLyD9K4TjnTQtVhXvzZAV/1Qw5+HLwQEMhOpmcR9WtfbobCw1/cdgwIeUHuzwePyaKRQA3i6NSOgAdB04t89/1O/w1cDnyilFU='
# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)
if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

mode = 0

@app.route('/callback', methods=['POST'])
def webhook_handler():
    global mode
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f'Request body: {body}')

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f'\nFSM STATE: {machine.state}')
        print(f'REQUEST BODY: \n{body}')

        if mode == 1:
            if event.message.text.lower() == 'search':
                mode = 0
                send_text_message(event.reply_token, 'Back to meme searching......')
                continue
        else:
            if event.message.text.lower() == 'show':
                mode = 1
                url = 'https://i.imgur.com/tLwz078.png'
                send_image_message(event.reply_token, url)
                continue
            else:
                response = machine.advance(event)

        if response == False:
            if machine.state != 'user' and event.message.text.lower() == 'restart':
                send_text_message(event.reply_token, 'Enter "Search" to search for memes:D\nEnter "Show" to show the project fsm diagram.\nEnter "Restart" to return.')
                machine.go_back()
            elif machine.state == 'user':
                send_text_message(event.reply_token, 'Enter "Search" to search for memes:D\nEnter "Show" to show the project fsm diagram.\nEnter "Restart" to return.')
            elif machine.state == 'input_select' or machine.state == 'input_num' or machine.state == 'input_check':
                send_text_message(event.reply_token, 'Type "1" for general memes. Type "2" for copypastas. Type "3" for jokes.')
            elif machine.state == 'input_language':
                send_text_message(event.reply_token, 'Choose between "Chinese" or "English".')
            elif machine.state == 'send':
                send_text_message(event.reply_token, '')
            elif machine.state == 'choose':
                send_text_message(event.reply_token, '')
            elif machine.state == 'Memes':
                send_text_message(event.reply_token, '')
            elif machine.state == 'Jokes':
                send_text_message(event.reply_token, '')
    return 'OK'


if __name__ == '__main__':
    port = os.environ.get('PORT', 8000)
    app.run(host='0.0.0.0', port=port, debug=True)
