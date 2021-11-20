# Python-based AWS Lambda functions example with API Gateway

This example shows how to implement and serve a function in AWS Lambda plus using it
via a static website (in AWS Lambda).

## Interesting parts

* [lambda/api.py](lambda/api.py) - the actual point where the lambda event handler lives
* [lambda/website.py](lambda/website.py) - website handler (serving a static local file)
* [web/index.html](web/index.html) - The HTML of the website

* `packme.sh` - packs two zip files, one for the code and one for the website
* `deploy.sh` - deploys the zips (needs proper AWS setup up front)

## Detailed How to

* [[Python + AWS Lambda + API Gateway] How to set up a complete service? (Medium article)](https://medium.com/@tuergeist/python-aws-lambda-api-gateway-how-to-set-up-a-complete-service-520b9dbe39c)

## Interesting Links

* https://pipenv.pypa.io/en/latest/
* https://docs.aws.amazon.com/cli/latest/reference/lambda/ 
* https://docs.aws.amazon.com/cli/latest/reference/lambda/create-function.html