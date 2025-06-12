from dcim.models import DeviceRole, Device
from dcim.models.mixins import RenderConfigMixin
from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar, FileVar
from dcim.models.devices import DeviceRole


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
            test_list.append(dev.custom_fields.test_temp_conf)
        return test_list
            
            



