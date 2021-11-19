from pathlib import Path


def handler_name(event, context):
    with Path('web/index.html').open() as file:
        html = file.read()
    response = {
        "statusCode": 200,
        "body": html,
        "headers": {
            'Content-Type': 'text/html',
        }
    }
    return response
