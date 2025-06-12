from dcim.models import DeviceRole, Device
from dcim.models.mixins import RenderConfigMixin
from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar, FileVar
from dcim.models.devices import DeviceRole
#from django.utils.text import slugify


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
        test_list = []
        for dev in data["devices"]:
            test_list.append(str(dev.custom_fields))
         
        return test_list
            
            



