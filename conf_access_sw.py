from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar, ScriptVariable
from dcim.models import DeviceRole, Device,Site

from django.contrib.contenttypes.fields import GenericRelation

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

  test = ScriptVariable(
    description='какая-то херня',
    )
  clone_fields = (
        'action',
    )
  def clean(self):
        super().clean()

  
 
  


  def run(self, data, commit) -> None:
    return str(data["select_action"])

