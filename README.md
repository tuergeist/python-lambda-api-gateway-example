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

* TODO Medium article here

## Interesting Links

* 
