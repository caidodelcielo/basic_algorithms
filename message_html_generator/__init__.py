import json
from collections import OrderedDict
import datetime

def generateHTML():
    with open('message_html_generator/message.json') as f:
        data = json.load(f, object_pairs_hook=OrderedDict)['messages']

    with open("message_html_generator/message_parsed.txt", "w", encoding='utf-8') as result_file:
        for item in list(reversed(data)):
            if 'content' in item:
                jmeno = fixEncoding(item['sender_name'])
                zprava = fixEncoding(item['content'])
                datumMs = item['timestamp_ms']
                datum = datetime.datetime.utcfromtimestamp(int(datumMs / 1000)) + datetime.timedelta(hours=2)
                datumLidske = datum.strftime('%Y-%m-%d %H:%M:%S')

                result_file.write(str(datumLidske) + ' - ' + jmeno + ': ' + zprava + '\n')

    print('finished writing')


def fixEncoding(text):
    return text.encode('latin1').decode('utf8')