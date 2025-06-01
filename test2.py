# Modules
from icmplib import ping


# Netbox artifcats
from extras.scripts import Script, ObjectVar, MultiObjectVar
from dcim.models import Site, Device


# Classes
class DeviceChecker(Script):
    class Meta:
        name = "Псс,брат.Проверь статус устройств"
        description = "Sample Script to set the status of the device based on its availability"
        field_order = ("site","device roles", "devices")

    site = ObjectVar(
        model=Site
    )

    #device_roles =

    devices = MultiObjectVar(
        model=Device,
        query_params={
            "site_id": "$site"
        }
    )

    def run(self, data, commit) -> None:
        print_in_nb = []
        for device in data["devices"]:
            result = ping(str(device.primary_ip.address.ip), count=3, interval=0.2, privileged=False)

            if result.is_alive:
                device.status = "active"

            else:
                device.status = "offline"

            print_in_nb.append(f"{device.name}  ёбта {device.status}")
            device.save()

        return "\n".join(print_in_nb)
