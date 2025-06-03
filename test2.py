# Modules
from icmplib import ping
from netmiko import ConnectHandler

# Netbox artifcats
from extras.scripts import Script, ObjectVar, MultiObjectVar
from dcim.models import DeviceRole, Device


# Classes
class DeviceChecker(Script):
    class Meta:
        name = "Псс"
        description = "Sample Script to set the status of the device based on its availability"
        field_order = ("devices_role", "devices")

    devices_role = ObjectVar(
        model=DeviceRole
    )

    devices = MultiObjectVar(
        model=Device,
        query_params={"role_id": "$devices_role"}

    )

    def run(self, data, commit) -> None:
        print_in_nb = []
        for device in data["devices"]:
            cisco_dev = {
            'device_type': 'cisco_ios',
            'host': str(device.primary_ip.address.ip),
            'username': 'cisco',
            'password': 'cisco',
            'secret': 'cisco',
            }
            connection = ConnectHandler(**cisco_dev)
            connection.enable()
            result = connection.send_command('show ip int br')
            print_in_nb.append(result)

            device.save()
        return "\n".join(print_in_nb)


