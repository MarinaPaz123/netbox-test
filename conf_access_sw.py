from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar, ScriptVariable,StringVar
from dcim.models import DeviceRole, Device, Site
from ipam.models.vlans import VLAN
from dcim.models.device_components import Interface
from extras.models.customfields import CustomField, CustomFieldChoiceSet, CustomFieldManager



class Access_sw(Script):
  class Meta():
    name = "Настрой vlan на свитче доступа"
    description = "conf vlan access sw"
    
  devices = MultiObjectVar(
        description = "Выбери коммутатор",
        model=Device,
        query_params={"role_id": 2} # Выбрать можно коммутаторы ACCESS!
        )
  
  vlan_id = MultiObjectVar(
       description = "Выбери vlan,братишка",
       model=VLAN,
       query_params={"site_id": 1} # Выбрать можно vlan только в сайте test!
  )
  Interfaces = MultiObjectVar(
     description = "Выбери порты,братишка",
     model= Interface,
     query_params={"device_id": "$devices"}
  )
  templ = MultiObjectVar(
     model= CustomFieldManager,
     #query_params={"role_id": 2}
  )
        


  def run(self, data, commit) -> None:
    return str(data["vlan_id"])

