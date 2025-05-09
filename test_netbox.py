# Modules
from icmplib import ping


# Netbox artifcats
from extras.scripts import Script, ObjectVar, MultiObjectVar
from dcim.models import Site, Device


# Classes
class DeviceChecker(Script):
    class Meta:
        name = "Validate state of network devices"
        description = "Sample Script to set the status of the device based on its availability"
        field_order = ("site", "devices")

    site = ObjectVar(
        model=Site
    )

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

            print_in_nb.append(f"{device.name} is set to {device.status}")
            device.save()

        return "\n".join(print_in_nb)
