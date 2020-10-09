import requests
import json
import time

createJSON = {
    "name": "JTest",
    "isbn": "JB123",
    "aisle": "141717157111",
    "author": "Jimmy Bowden"
}

deleteJSON = {
    "ID": createJSON['isbn'] + createJSON['aisle'],
}

headers = {
     "content-type": "application/json"
}

response = requests.post("http://216.10.245.166/Library/Addbook.php", json=createJSON, headers=headers)

print(response.status_code)
assert response.status_code == 200
print(json.loads(response.text))
assert json.loads(response.text)['Msg'] == 'successfully added'
assert json.loads(response.text)['ID'] == str(createJSON['isbn']) + str(createJSON['aisle'])

time.sleep(3)

response2 = requests.post("http://216.10.245.166/Library/DeleteBook.php", json=deleteJSON, headers=headers)
#Fix 404 here next time you work on this
print(response2.status_code)
print(response2.text)