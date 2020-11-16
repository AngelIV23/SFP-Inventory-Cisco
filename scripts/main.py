from genie.testbed import load

identifier = 0
tb = load('yaml/my_testbed.yaml')

"""This module search for info inside testbed hosts."""
text_file = open("testing.xlsx", "w")
### first line
n = text_file.write('Id,Device Name, Serial\n')


for device_name in tb.devices:
    dev = tb.devices[device_name]
    dev.connect(log_stdout=False)
    p1 = dev.parse('show inventory')
    ###    print(p1['main']['chassis']['IOSv']['sn'])
    print(str(identifier)+'. ' + device_name + " has a serial number: " + p1['main']['chassis']['IOSv']['sn'])
    ### next lines
    n = text_file.write(str(identifier) +', ' + device_name +', ' + p1['main']['chassis']['IOSv']['sn'] + '\n')
    identifier = identifier + 1


text_file.close()
