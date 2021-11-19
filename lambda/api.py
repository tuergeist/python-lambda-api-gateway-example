import base64

from requests_toolbelt.multipart import decoder

from main import reverse_it


def handler_name(event, context):
    try:

        content_type_header = event['headers']['content-type']
        postdata = base64.b64decode(event['body']).decode('iso-8859-1')
        for part in decoder.MultipartDecoder(postdata.encode('utf-8'), content_type_header).parts:
            result = reverse_it(part.text.split('\n'))
        result = '\n'.join(result)
        return result
    except Exception as e:
        print('error occured', e)
        print('# event')
        print(event)

    return {
        "statusCode": 500,
        "body": "could not handle error, see log",
        "headers": {
            'Content-Type': 'text/html',
        }
    }