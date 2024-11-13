import os
import dotenv

# Take environment variables from .env
dotenv.load_dotenv()

TOKEN = os.getenv("TOKEN")
