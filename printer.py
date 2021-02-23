from octorest import OctoRest
from dotenv import load_dotenv
import os
load_dotenv()
def is_printing():
    client = OctoRest(url="http://octopi.local", apikey=os.getenv('api_key_printer'))
    return client.printer()['state']['flags']['printing']
    
#63434FF7AF4047E2881F3229DC52CB44
