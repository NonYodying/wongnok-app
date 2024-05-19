def convertRecipe(doc) -> dict:
    return {
        '_id': str(doc['_id']),
        'title': doc['title'],
        'img': doc['img'],
        'ingradient': doc['ingradient'],
        'time': doc['time'],
        'difucallty': doc['difucallty'],
    
    }


def convertRecipes(docs) -> list:
    return [convertRecipe(doc) for doc in docs]