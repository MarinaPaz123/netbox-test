from dcim.models import DeviceRole, Device
from dcim.models.mixins import RenderConfigMixin
from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar, FileVar
from dcim.models.devices import DeviceRole
#from django.utils.text import slugify
#import pynetbox
#import requests


from jinja2 import Environment, FileSystemLoader
import yaml
from netmiko import ConnectHandler
from netmiko.exceptions import ReadTimeout


class ConfACL(Script):
    class Meta:
        name = "Игра: собери свой ACL,бро"
        description = "conf_ACL"

    devices = MultiObjectVar(
        description = "Выбери устройство",
        model=Device,
        )
     
    
    def run(self, data, commit) -> None:
        
        print_result = ""
        for dev in data["devices"]:
            command_list = []
            # Проходимся циклом по кастомному полю!!
            for key,val in dev.custom_field_data.items():
                if val == None:
                    return "пусто поле"  # Поправить ! - continue
                command_list.append(val)
                cisco_dev = {
                    'device_type': 'cisco_ios',
                    'host': str(dev.primary_ip.address.ip),
                    'username': 'cisco',
                    'password': 'cisco',
                    'secret': 'cisco',
                    }
                connection = ConnectHandler(**cisco_dev)
                connection.enable()
                for i in command_list:
                    try:
                        result = connection.send_config_set(i)
                    except ReadTimeout: # Не понятно, почему. Ибо команды все отправляются 
                        return f"РЭАД ТАЙМАУТ БЛЯДЬ НА {dev.name}"
                

        return  " ок"
        #return str(dev.custom_field_data)
            
            



