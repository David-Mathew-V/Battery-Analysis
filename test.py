# test analysis for battery
import os
from dotenv import load_dotenv

load_dotenv()

print("Hell")
name = os.getenv("user_name") or "Unknown"
print("Name: " + name)
