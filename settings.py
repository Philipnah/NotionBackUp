import json

emailList = ["email", "mail", "em", "1"]
passList = ["password", "pswd", "pwd", "2"]


choice = input("\nWhat do you want to change? [First time setup press 0] ")

if choice in emailList:
     with open("settings.json") as json_file:
          data = json.load(json_file)
          for i in data["details"]:
               newPassword = i["password"]
     
     newEmail = input("New email: ")

elif choice in passList:
     with open("settings.json") as json_file:
          data = json.load(json_file)
          for i in data["details"]:
               newEmail = i["email"]

     newPassword = input("New password: ")

elif choice == "0":
     newEmail = input("Email address: ")
     newPassword = input("Password: ")

elif choice == "time" or "timing":
     pass
     # get webDelay for main script

else:
     print("Your selection was not found")

details = "details"

data = {}
data[details] = []
try:
     data[details].append({
          "email": newEmail,
          "password": newPassword
     })

     with open("settings.json", "w") as outputFile:
          json.dump(data, outputFile)

except NameError as identifier:
     print("\n" + str(identifier) + "\nTry running the file again as first time user.")