from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar, ScriptVariable,StringVar
from dcim.models import DeviceRole, Device,Site
from dcim.models.mixins import CachedScopeMixin


class Access_sw(Script):
  class Meta():
    name = "Настрой vlan на свитче доступа"
    description = "conf vlan access sw"
    
  devices = MultiObjectVar(
        description = "Выбери коммутатор",
        model=Device,
        query_params={"role_id": 2} # Выбрать можно коммутаторы ACCESS!
        )
  
  action = (
    ('vlan_access_sw', 'Создать vlan и подать на порты'),
    ('access_sw_port_security', 'Настроить port security'),
    )
  select_action = ChoiceVar(choices=action)

  vlan_id = StringVar(
       description = "Введи vlan_id",)
        


  def run(self, data, commit) -> None:
    return str(data["select_action"])

