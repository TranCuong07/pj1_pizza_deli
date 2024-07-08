# supabase_client.py
from dotenv import load_dotenv
import os
from supabase import create_client, Client

# Load environment variables from .env file
load_dotenv()

# Get the Supabase URL and key from environment variables, ensuring they are not None
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")


# Check if URL and key are None and raise an error if they are
if url is None or key is None:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in the environment variables")

# Create a Supabase client
supabase: Client = create_client(url, key)
