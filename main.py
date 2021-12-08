
import helper

config = helper.read_config()

ftpUrl = config['FTPSettings']['ftpUrl']
userName = config['FTPSettings']['userName']
password = config['FTPSettings']['password']

print("\nDisplaying FTP details\n")

print("FTP URL: " + ftpUrl)
print("FTP User Name: " + userName)
print("Password: " + password)