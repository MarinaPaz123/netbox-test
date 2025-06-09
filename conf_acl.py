from dcim.models import DeviceRole, Device
from jinja2 import Environment, FileSystemLoader
import yaml

from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar

class ConfACL(Script):
    class Meta:
        name = "Игра: собери свой ACL,бро"
        description = "conf_ACL"

    devices_role = ObjectVar(
        description = "Выбери роль",
        model=DeviceRole,
        )
    
    template_dev = MultiObjectVar(
        model=DeviceRole,
        query_params={"config_template": {"id": 2}}
        )

    def run(self, data, commit) -> None:
        pass



