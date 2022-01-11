import configparser

config_file = configparser.ConfigParser()

config_file.add_section("APPSettings")

config_file.set("APPSettings", "WSSUrl", "wss://test.gntapi.com/")
config_file.set("APPSettings", "Market", "USDMXN")
config_file.set("APPSettings", "list_size", "10")
config_file.set("APPSettings", "number_of_samples", "20")
config_file.set("APPSettings", "wait_between_samples_seconds", "3")

with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Configuration file 'configurations.ini' initialized")

read_file = open("configurations.ini", "r")
content = read_file.read()
print("Config file contents:\n")
print(content)
read_file.flush()
read_file.close()