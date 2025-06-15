from extras.scripts import Script, ObjectVar, MultiObjectVar, TextVar,ChoiceVar
from dcim.models import DeviceRole, Device,Site
import django_filters
from django.db.models import Q
#from .models import BgpPeering

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
  
class BgpPeeringFilter(django_filters.FilterSet):
  """Filter capabilities for BgpPeering instances."""

    q = django_filters.CharFilter(
        method="search",
        label="Search",
    )
    class Meta:
        model = BgpPeering

        fields = [
            "local_as",
            "remote_as",
            "peer_name",
        ]

  
  
  
    
  
  def run(self, data, commit) -> None:
    return str(data["select_action"])

