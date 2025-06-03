# Modules
# Modules
from icmplib import ping


# Netbox artifcats
from extras.scripts import Script, ObjectVar, MultiObjectVar
from dcim.models import DeviceRole, Device


# Classes
class DeviceChecker(Script):
    class Meta:
        name = "Псс"
        description = "Sample Script to set the status of the device based on its availability"
        field_order = ("deviceroles", "devices")

    devrole = ObjectVar(
        model=DeviceRole
    )

    dev = MultiObjectVar(
        model=Device,
    )

