def add_create_payload(isbn, aisle):

    body = {
        "name": "JTest",
        "isbn": isbn,
        "aisle": aisle,
        "author": "Jimmy Bowden"
    }
    return body

def ad_delete_payload(isbn, aisle):
    body = {
        "ID": isbn + aisle
    }
    return body