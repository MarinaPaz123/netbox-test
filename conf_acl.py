from dcim.models import DeviceRole, Device
from dcim.models.mixins import RenderConfigMixin
from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar, FileVar
from dcim.models.devices import DeviceRole
#from django.utils.text import slugify
import pynetbox
import requests


from jinja2 import Environment, FileSystemLoader
import yaml


class ConfACL(Script):
    class Meta:
        name = "Игра: собери свой ACL,бро"
        description = "conf_ACL"

    devices = MultiObjectVar(
        description = "Выбери устройство",
        model=Device,
        )
     
    
    def run(self, data, commit) -> None:
        #URL = 'http://192.168.85.128/'
        #API_KEY = '1c99a62d0cafe13c94d375a982cfd87b470513f0'
        #netbox = pynetbox.api(URL, token = API_KEY)
        test_list = []
        for dev in data["devices"]:
            test_list.append(str(dev.name))
            
            #test_list.append(str(dev.custom_fields.field_name))
            #test_list.append(str(dev.primary_ip.address.ip))
         
        return test_list
            
            



