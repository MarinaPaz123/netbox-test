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

    devices = ObjectVar(
        description = "Выбери устройство",
        model=Device,
        )
    
    template_dev = MultiObjectVar(
        model=Device.objects.get(name="R2"),
        )
     
    
    def run(self, data, commit) -> None:
        pass



