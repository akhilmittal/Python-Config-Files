import configparser

# CREATE OBJECT
config_file = configparser.ConfigParser()

# ADD FTPSettings SECTION
config_file.add_section("FTPSettings")
# ADD SETTINGS TO FTPSettings SECTION
config_file.set("FTPSettings", "ftpUrl", "demoftp.codeteddy.com")
config_file.set("FTPSettings", "userName", "codeteddy")
config_file.set("FTPSettings", "password", "my#supersecret#password")

# ADD NEW SECTION AND SETTINGS
config_file["Logger"]={
        "LogFilePath":"<Path to log file>",
        "LogFileName" : "<Name of log file>",
        "LogLevel" : "Info"
        }

# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configfileObj:
    config_file.write(configfileObj)
    configfileObj.flush()
    configfileObj.close()

print("Config file 'configurations.ini' created")

# PRINT FILE CONTENT
read_file = open("configurations.ini", "r")
content = read_file.read()
print("Content of the config file are:\n")
print(content)
read_file.flush()
read_file.close()