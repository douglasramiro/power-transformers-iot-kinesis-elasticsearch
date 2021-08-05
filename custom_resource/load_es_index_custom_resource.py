from aws_cdk import (
    aws_cloudformation as cfn,
    aws_lambda as lambda_,
    aws_iam as iam,
    core
)


class LoadESIndexCustomResource(core.Construct):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id)

        es_host = kwargs.get("es_host")
        es_region = kwargs.get("es_region")
        es_domain_arn = kwargs.get("es_domain_arn")

        function = lambda_.SingletonFunction(
            self, "Singleton",
            uuid="e43d1f1e-5676-415c-84d5-d376069aa0da",
            code=lambda_.Code.asset("./lambda/load-es-index.zip"),
            handler="lambda_function.handler",
            timeout=core.Duration.seconds(300),
            runtime=lambda_.Runtime.PYTHON_3_8,
            environment={'ES_HOST': es_host, 'ES_REGION': es_region}
        )

        function.add_to_role_policy(
            iam.PolicyStatement(actions=['es:ESHttpPost', 'es:ESHttpPut'], resources=[es_domain_arn], effect=iam.Effect.ALLOW))

        resource = cfn.CustomResource(
            self, "Resource",
            provider=cfn.CustomResourceProvider.lambda_(function),
            properties=kwargs,
        )

        self.response = resource.get_att("Response").to_string()
