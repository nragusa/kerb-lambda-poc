# Start with AWS Lambda python 3.7 runtimei environment
# See https://docs.aws.amazon.com/lambda/latest/dg/python-image.html#python-image-base
FROM public.ecr.aws/lambda/python:3.7

# Copy function code into container
COPY app/app.py ${LAMBDA_TASK_ROOT}

# Install kerb specific packages
RUN yum -y install krb5-workstation krb5-devel gcc

# Install python modules specific for this environment, e.g. requests-kerberos
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler
CMD [ "app.handler" ] 