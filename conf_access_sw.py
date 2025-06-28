from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar, ChoiceVar, ScriptVariable
from dcim.models import DeviceRole, Device,Site
from dcim.models.mixins import CachedScopeMixin

from django.contrib.contenttypes.fields import GenericRelation

class Access_sw(Script,CachedScopeMixin):
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
        'scope_type','scope_id','action',"site"
    )
  def clean(self):
    super().clean()
    site = None
    #action = None
    if self.action:
        action = self.action.model_class()
        if action == 'vlan_access_sw':
            site = "ляляля"
        else:
            site = "ляляля"
          
            

  
 
  


  def run(self, data, commit) -> None:
    return str(data["select_action"])

