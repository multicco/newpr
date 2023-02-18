from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPinned


api_id=                           #nums
api_hash= ''
client= TelegramClient('session_name',api_id, api_hash)
client.start()


def scarpmessage (url):
    mess =client.get_messages(url,filter=InputMessagesFilterPinned)
    for message in mess:
        if str(message.id) not in sent_messages:
            client.forward_messages('MYCHANELTELEGRAM',mess)
            sent_messages.append(str(message.id))

    with open('sent_messages.txt', 'w') as f:
         f.write('\n'.join(sent_messages))

#список каналов в блокноте
with open('channels.txt', 'r') as r:
    channels = r.readlines()



with open('sent_messages.txt', 'r') as file:
    sent_messages = file.readlines()

for chanel in channels:
    scarpmessage(chanel)


