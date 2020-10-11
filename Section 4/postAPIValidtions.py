import requests
import json
import random

from payLoadHelper import *

isbn = "JB" + str(random.randrange(1,999))
aisle = str(random.randrange(1,999))

createJSON = add_create_payload(isbn, aisle)
deleteJSON = ad_delete_payload(isbn, aisle)

headers = {
     "content-type": "application/json"
}

# POST create endpoint - should create a new book
response = requests.post("http://216.10.245.166/Library/Addbook.php", json=createJSON, headers=headers)

print(response.status_code)
assert response.status_code == 200
print(json.loads(response.text))
assert json.loads(response.text)['Msg'] == 'successfully added'
assert json.loads(response.text)['ID'] == str(createJSON['isbn']) + str(createJSON['aisle'])

# POST Addbook endpoint - should NOT create a book that has a non unique ID (isbn + aisle)
response = requests.post("http://216.10.245.166/Library/Addbook.php", json=createJSON, headers=headers)

print(response.status_code)
assert response.status_code == 404
print(json.loads(response.text))
assert json.loads(response.text)['msg'] == 'Add Book operation failed, looks like the book already exists'

# POST DeleteBook endpoint - should delete a book with a valid ID
response2 = requests.post("http://216.10.245.166/Library/DeleteBook.php", json=deleteJSON, headers=headers)
print(response2.status_code)
assert response2.status_code == 200
print(response2.text)
assert json.loads(response2.text)['msg'] == 'book is successfully deleted'

# POST DeleteBook endpoint - should return error message when deleting a book with an invalid ID
response2 = requests.post("http://216.10.245.166/Library/DeleteBook.php", json=deleteJSON, headers=headers)
print(response2.status_code)
assert response2.status_code == 404
print(response2.text)
assert json.loads(response2.text)['msg'] == 'Delete Book operation failed, looks like the book doesnt exists'