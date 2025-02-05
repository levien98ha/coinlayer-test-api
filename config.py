from dotenv import load_dotenv
import os

load_dotenv()
private_key = os.getenv("PRIVATE_KEY")
api_url = os.getenv("API_URL")

end_point = {
    "live": "/live",
    #another api endpoint
}