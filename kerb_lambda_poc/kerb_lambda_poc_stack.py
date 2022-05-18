from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_s3 as s3
)
from constructs import Construct


class KerbLambdaPocStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Example lambda function that uses a Docker based image as the runtime
        # environment. Code for the Docker image is stored under ./src,
        # and the CDK will automatically build / tag / push the container into
        # an Amazon ECR registry.
        kerb_function = _lambda.DockerImageFunction(
            self,
            'KerbLambdaContainer',
            code=_lambda.DockerImageCode.from_image_asset(
                directory='./src'
            ),
            description='Example Lambda function with a custom container that has kerb libraries',
            memory_size=256,
            timeout=Duration.seconds(10)
        )

        # Example of creating an S3 bucket
        # bucket = s3.Bucket(
        #     self,
        #     'S3BucketForKerbConfig',
        #     block_public_access=s3.BlockPublicAccess(
        #         block_public_acls=True,
        #         block_public_policy=True,
        #         ignore_public_acls=True,
        #         restrict_public_buckets=True
        #     ),
        #     encryption=s3.BucketEncryption.KMS,
        #     enforce_ssl=True,
        #     versioned=True
        # )

        # # Provide Lambda function read access to bucket
        # bucket.grant_read(kerb_function.role)