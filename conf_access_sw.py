from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar
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

  def run(self, data, commit) -> None:
    pass

