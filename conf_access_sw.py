from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar, ScriptVariable,StringVar
from dcim.models import DeviceRole, Device,Site
from ipam.models.vlans import VLAN



class Access_sw(Script):
  class Meta():
    name = "Настрой vlan на свитче доступа"
    description = "conf vlan access sw"
    
  devices = MultiObjectVar(
        description = "Выбери коммутатор",
        model=Device,
        query_params={"role_id": 2} # Выбрать можно коммутаторы ACCESS!
        )
  
  vlan_id = StringVar(
       description = "Введи vlan_id.Если vlan несколько,введи их через запятую е мае",)
        


  def run(self, data, commit) -> None:
    return str(data["vlan_id"])

