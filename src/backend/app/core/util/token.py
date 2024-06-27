import boto3
import tiktoken

class TokenUtilityService:
    def __init__(self, aws_access_key, aws_secret_access_key, aws_region):
        self.aws_access_key = aws_access_key
        self.aws_secret_access_key = aws_secret_access_key
        self.aws_region = aws_region

        self.boto3_session = boto3.Session(
            aws_access_key_id=self.aws_access_key,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.aws_region
        )
        self.bedrock_client = self.boto3_session.client('bedrock-runtime')

    def get_bedrock_token_count(self, text, model_id='amazon.titan-text-lite-v1'):
        try:
            response = self.bedrock_client.invoke_endpoint(
                EndpointName=model_id,
                Body=text.encode('utf-8'),
                ContentType='text/plain',
                Accept='application/json'
            )
            response_body = response['Body'].read().decode('utf-8')
            tokens = response_body.split()
            return len(tokens)
        except Exception as e:
            print(f"Error calculating Bedrock token count: {e}")
            return None

    def get_openai_token_count(self, text, model_name='gpt-3.5-turbo'):
        try:
            encoding = tiktoken.encoding_for_model(model_name)
            tokens = encoding.encode(text)
            return len(tokens)
        except Exception as e:
            print(f"Error calculating OpenAI token count: {e}")
            return None