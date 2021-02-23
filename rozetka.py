import os
import tinytuya as tn
from dotenv import load_dotenv
from printer import is_printing

load_dotenv()


class Rozetka:
    def __init__(self):
        self.dps = {
            'printer': '1',
            'tv': '2'
        }

        self.device_manager = tn.OutletDevice(os.getenv('socket_id'), '0.0.0.0', os.getenv('socket_key'))
        self.device_manager.set_version(3.3)
        

    def get_status(self, all: bool = False) -> dict:
        data = self.device_manager.status()

        device_statuses = data['dps'] #{'1':'','2':''}
        
        if all:
            return device_statuses

        return {
            self.dps['printer']: device_statuses[self.dps['printer']],
            self.dps['tv']: device_statuses[self.dps['tv']],
        }

    def set_status(self, switch: str, status: bool, *, force: bool = False) -> None:
        if force:
            self.device_manager.set_status(status, switch=switch)
            return True         
        if status == False and switch == self.dps['printer']:
            if self.get_status()[self.dps['printer']] == True and is_printing():
                print('get the fuck out of here')
                return False
        self.device_manager.set_status(status, switch=switch)
        return True

a = Rozetka()
print(a.get_status())
a.set_status(a.dps['printer'], False, True)
