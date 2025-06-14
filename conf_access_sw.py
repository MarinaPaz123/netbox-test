from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar,ChoiceVar
from dcim.models import DeviceRole, Device

class Access_sw(Script):
  class Meta:
    name = "Настрой свитч доступа"
    description = "conf access sw"
    
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
  
    
  
  def run(self, data, commit) -> None:
    return str(data["action"])

