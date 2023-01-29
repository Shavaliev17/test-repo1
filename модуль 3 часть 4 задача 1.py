import json
login = input()
password = input()
data = (login,password)
with open('3.json', 'w') as f:
    json.dump(data,f)