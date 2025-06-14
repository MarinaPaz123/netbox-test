from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar
from dcim.models import DeviceRole, Device

class Access_sw(Script):
  class Meta:
    name = "Настрой свитч доступа"
    description = "conf access sw"
    
  devices = MultiObjectVar(
        description = "Выбери устройство",
        model=Device(role= {"id": 2})
        )

  def run(self, data, commit) -> None:
    pass

