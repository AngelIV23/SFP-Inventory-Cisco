from genie.testbed import load

tb = load('yaml/my_testbed.yaml')

"""This module search for info inside testbed hosts."""
text_file = open("testing.csv", "w")
### first line
n = text_file.write('Id,Device Name, Serial\n')

for device_name in tb.devices:
    print(device_name)
    dev = tb.devices[device_name]
    dev.connect(log_stdout=False)
    p1 = dev.parse('show inventory')
###    print(p1['main']['chassis']['IOSv']['sn'])
    print(device_name + " has a serial number: " + p1['main']['chassis']['IOSv']['sn'])
### next lines
    n = text_file.write('1,' + device_name +', ' + p1['main']['chassis']['IOSv']['sn'] + '\n')


text_file.close()
