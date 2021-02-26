import os
import tinytuya as tn
from dotenv import load_dotenv
from printer import is_printing

load_dotenv()


class Rozetka:
    def __init__(self): #Задаем начальные параметры, если про ООП прочитал, понял че такое методы ООП,
                        #атрибуты, экземпляры, то проблем возникнуть не должно
        self.dps = {
            'printer': '1',
            'tv': '2'
        }

        self.device_manager = tn.OutletDevice(os.getenv('socket_id'), '0.0.0.0', os.getenv('socket_key'))
        #грубо говоря получили доступ к розетке для работы с ней
        self.device_manager.set_version(3.3)
        

    def get_status(self, all: bool = False) -> dict:
        data = self.device_manager.status()

        device_statuses = data['dps'] #{'1':'','2':''}
        if all: #смори, если у нас all станет true, то оно нам вернет все данные о розетке.
            #а если нет, то нет)
            return device_statuses

        return {
            self.dps['printer']: device_statuses[self.dps['printer']],
            self.dps['tv']: device_statuses[self.dps['tv']],#здесь мы для удобства работы будем использовать
            #значения из словаря dps. Значение принтера равно 1, а тв 2. Мы просто можем написать 
            # self.dps['tv']
            # таким образом, чтобы не вспоминать какой номер у розетки или тв 
        }


    def set_status(self, switch: str, status: bool, *, force: bool = False) -> None:
        if force:
            self.device_manager.set_status(status, switch=switch)
            #Если наш force равен True условный толкатель всего, то он выполняет действие независимо от статуса принтера.
            return True         
        if status == False and switch == self.dps['printer']:
            if self.get_status()[self.dps['printer']] == True and is_printing(): #прикольная штука - проверяет включен ли принтер, если да,
                #то шлет пользователя , если же он включен и печатает, то тоже шлет.
                print('get the fuck out of here')
                return False #интересная штука, после того, как оно отослало сообщение, мы выходим с метода полностью.
        self.device_manager.set_status(status, switch=switch)
        return True  

a = Rozetka()
a.set_status(a.dps['printer'], False, force=True)


