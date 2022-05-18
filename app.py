#!/usr/bin/env python3

import aws_cdk as cdk
from aws_cdk import Tags

from kerb_lambda_poc.kerb_lambda_poc_stack import KerbLambdaPocStack


app = cdk.App()
stack = KerbLambdaPocStack(app, 'KerbLambdaPocStack')
Tags.of(stack).add('Environment', 'Dev')
Tags.of(stack).add('Project', 'Lambda Kerberos')

app.synth()
