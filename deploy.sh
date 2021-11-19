#!/usr/bin/env bash
# fill in your function names
FUNCTION=medium-example-1
WEBSITE=medium-example-web

aws lambda update-function-code --function-name $FUNCTION --zip-file fileb://deployment-pkg.zip
aws lambda update-function-code --function-name $WEBSITE --zip-file fileb://website-pkg.zip
