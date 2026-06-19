# %%
import dotenv
import os 
import boto3

dotenv.load_dotenv()
# %%
AWS_KEY = os.getenv("AWS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
# %%
s3 = boto3.client("s3",
                   aws_access_key_id=AWS_KEY,
                   aws_secret_access_key=AWS_SECRET_KEY, region_name="us-east-2"
        )
# %%
s3.list_buckets()

