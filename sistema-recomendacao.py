import math
#users' matrix
#inserir aqui a matriz de jogos com as respectivas horas que o usuário passou jogando determinado jogo
users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Narah Jones": 4.5, "Phoenix": 5.0, "Slight Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
        "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slight Stoopid": 3.5, "Vampire Weekend": 3.0},
        "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Narah Jones": 3.0, "Phoenix": 5.0, "Slight Stoopid": 1.0},
        "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slight Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
        "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Narah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
        "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Narah Jones": 5.0, "Phoenix": 5.0, "Slight Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
        "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Narah Jones": 3.0, "Phoenix": 5.0, "Slight Stoopid": 4.0, "The Strokes": 5.0},
        "Veronica": {"Blues Traveler": 3.0, "Narah Jones": 5.0, "Phoenix": 4.0, "Slight Stoopid": 2.5, "The Strokes": 3.0, "Iron Maiden": 5.0},
        }

def cossenoSimilarity(rating1, rating2):
    numerador = 0 #x * y
    x_comp = 0 # ||x||
    y_comp = 0 # ||y||
    for key in rating1:
        if key in rating2:
            numerador = numerador + (rating1[key]*rating2[key])
            x_comp = x_comp + pow(rating1[key], 2)
            y_comp = y_comp + pow(rating2[key], 2)
    denominador = math.sqrt(x_comp) * math.sqrt(y_comp)
    if denominador == 0:
        return 0
    else:
        return numerador / denominador

#nearest neighbors from a username function
def computeNearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
        	distance = cossenoSimilarity(users[user], users[username])
        	distances.append((distance, user))
    distances.sort()
    return distances
print (computeNearestNeighbor('Angelica', users))

#reccomender bands to a username function
def recommend(username, users):
    neighbors = computeNearestNeighbor(username, users)
    nearest = neighbors[len(neighbors)-1][1]
    print(nearest)
    recommendations = []
    neighborRatings = users[nearest]
    userRatings = users[username]   
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    return sorted(recommendations, key = lambda artistTuple: artistTuple[1], reverse = True)
    
print(recommend('Angelica', users))
