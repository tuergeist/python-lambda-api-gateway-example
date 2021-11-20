import base64

from requests_toolbelt.multipart import decoder

from main import reverse_it


def handler_name(event, context):
    try:
        result = ''
        content_type_header = event['headers']['content-type']
        post_data = base64.b64decode(event['body']).decode('iso-8859-1')
        for part in decoder.MultipartDecoder(post_data.encode('utf-8'), content_type_header).parts:
            result = reverse_it(part.text.split('\n'))
            result = '\n'.join(result)
        return result
    except Exception as e:
        print('error occured', e)
        print('# event')
        print(event)

    # just for demo purposes. This does not make much sense here :) I'd be better not to catch all exceptions!
    return {
        "statusCode": 500,
        "body": "could not handle error, see log",
        "headers": {
            'Content-Type': 'text/html',
        }
    }
