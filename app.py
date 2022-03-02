import os
from dotenv import load_dotenv
load_dotenv()

serverIP = os.getenv("SERVER_IP")
print(serverIP)
