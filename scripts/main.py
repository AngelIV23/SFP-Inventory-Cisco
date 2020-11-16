from genie.testbed import load

tb = load('yaml/my_testbed.yaml')

"""This module search for info inside testbed hosts."""

for device_name in tb.devices:
    print(device_name)
    dev = tb.devices[device_name]
    dev.connect(log_stdout=False)
    p1 = dev.parse('show inventory')
    print(p1['main']['chassis']['IOSv']['sn'])

    print(device_name + " has a serial number: " + p1['main']['chassis']['IOSv']['sn'])
