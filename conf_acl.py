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

    devices_role = ObjectVar(
        description = "Выбери роль",
        model=DeviceRole,
        )
    
    template_dev = MultiObjectVar(
        model=DeviceRole.objects.get(name="Conf_routers_test"),
        
        )
    
    def run(self, data, commit) -> None:
        pass



