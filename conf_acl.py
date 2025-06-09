from jinja2 import Environment, FileSystemLoader
import yaml

from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar

class ConfACL(Script):
    class Meta:
        name = "Игра: собери свой ACL,бро",
        description = "conf_ACL"

    devices_role = ObjectVar(
        model=DeviceRole,
        context= "Выбери роль,э"
        )
    def run(self, data, commit) -> None:
        pass
        


