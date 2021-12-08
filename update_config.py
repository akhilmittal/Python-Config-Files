import configparser

# CREATE OBJECT
config_file = configparser.ConfigParser()

# READ CONFIG FILE
config_file.read("configurations.ini")
 
# UPDATE A FIELD VALUE
config_file["Logger"]["LogLevel"]="Debug"
 
# ADD A NEW FIELD UNDER A SECTION
config_file["Logger"].update({"Format":"(message)"})


 
# SAVE THE SETTINGS TO THE FILE
with open("configurations.ini","w") as file_object:
    config_file.write(file_object)
 
# DISPLAY UPDATED SAVED SETTINGS
print("Config file 'configurations.ini' is updated")
print("Updated file settings are:\n")
file=open("configurations.ini","r")
settings=file.read()
print(settings)