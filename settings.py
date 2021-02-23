from dotenv import load_dotenv
import os
load_dotenv()
key_printer = os.getenv('api_key_printer')
print(key_printer)