def convertUser(doc) -> dict:
    return {
        '_id': str(doc['_id']),
        'username': doc['username'],
        'password': doc['password'],
        'email': doc['email'],
        'profileName': doc['profileName'],
        'profileImg': doc['profileImg'],
    
    }