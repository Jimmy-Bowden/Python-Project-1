import requests
import json

response = requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "Rahul Shetty2"})
dict_response = json.loads(response.text)[0]
# print(dict_response)
# print(response.status_code)
# print(response.headers)

assert response.status_code == 200
assert response.headers['content-type'] == 'application/json;charset=UTF-8'


response2 = requests.get("http://216.10.245.166/Library/GetBook.php", params={"AuthorName": "Rahul Shetty"})
dict_response2 = json.loads(response2.text)
for book in dict_response2:
    if book['isbn'] == "RGHCC":
        assertBook = book

expectedBook = {
    "book_name": "Learn API Automation with RestAssured",
    "isbn": "RGHCC",
    "aisle": "12239c"
}

assert assertBook == expectedBook
