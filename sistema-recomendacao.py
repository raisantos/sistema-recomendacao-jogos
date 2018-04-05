import math
#users' matrix
#inserir aqui a matriz de jogos com as respectivas horas que o usuário passou jogando determinado jogo

'''
users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Narah Jones": 4.5, "Phoenix": 5.0, "Slight Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
        "Bill": {"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slight Stoopid": 3.5, "Vampire Weekend": 3.0},
        "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Narah Jones": 3.0, "Phoenix": 5.0, "Slight Stoopid": 1.0},
        "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slight Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
        "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Narah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
        "Jordyn": {"Broken Bells": 4.5, "Deadmau5": 4.0, "Narah Jones": 5.0, "Phoenix": 5.0, "Slight Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
        "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Narah Jones": 3.0, "Phoenix": 5.0, "Slight Stoopid": 4.0, "The Strokes": 5.0},
        "Veronica": {"Blues Traveler": 3.0, "Narah Jones": 5.0, "Phoenix": 4.0, "Slight Stoopid": 2.5, "The Strokes": 3.0, "Iron Maiden": 5.0},
        }
'''
users = {'Alfredo': {'Board Game: Top Shop': 30,
  'Crimson Sea 2': 10,
  'FIFA Soccer 09': 5,
  'LEGO Star Wars III: The Clone Wars': 26,
  'Lucha Libre AAA: Heroes del Ring': 16,
  'Nanashi no Game': 4,
  'Naruto: Uzumaki Chronicles 2 (JP sales)': 7,
  'Press Your Luck 2010 Edition': 27,
  'Rugby 2004': 28,
  'SaGa 2: Hihou Densetsu - Goddess of Destiny': 12,
  'Star Fox Adventures': 27,
  'Super Mario Land': 14,
  'Super Meat Boy: Ultra Edition!': 5,
  'Tenchu: Stealth Assassins': 3,
  'The First Templar': 3,
  'Theme Hospital': 21,
  'Top Spin': 25},
 'Alyiah': {'Breath of Fire: Dragon Quarter': 18,
  'Heavy Fire: Afghanistan': 1},
 'Cerenity': {'Athens 2004': 6,
  "Cabela's Trophy Bucks": 16,
  'ESPN NFL 2K5': 10,
  'Madden NFL 2004': 2,
  'Meru Purana': 29,
  'Motto! Stitch! DS Rhythm de Rakugaki Daisakusen': 1,
  'NBA Hoopz': 7,
  'New Super Luigi U': 22,
  'Painkiller: Hell & Damnation': 21,
  'Pastel Chime Continue': 22,
  'SingStar Chartbreaker': 10,
  'Sonic Heroes': 8,
  'The Smurfs': 27,
  'Tom and Jerry: Infurnal Escape': 12,
  'Transformers: Devastation': 4},
 'Donald': {'Doraemon 2: Nobita no Toizurando Daibouken': 1, 'TigerShark': 26},
 'Efrain': {'Assetto Corsa': 12,
  'Batman: Arkham Origins': 17,
  'DJ Hero': 2,
  'Dance Factory': 12,
  'Domino Rally': 28,
  'EA Sports Active': 17,
  'Ginga Tetsudou 999 DS': 30,
  'Jampack Winter 2002': 11,
  'NBA Hangtime': 7,
  'Need for Speed: Shift 2 Unleashed': 27,
  'Nintendo World Cup': 14,
  'Playmobil Knights': 5,
  'Pokémon Yellow: Special Pikachu Edition': 8,
  'Style Lab: Makeover': 7,
  'Sébastien Loeb Rally Evo': 3,
  'The History Channel: Battle for the Pacific': 17,
  'The Legend of Kage 2': 3,
  'Winter Sports 2011': 10,
  'Yu-Gi-Oh! The Falsebound Kingdom': 10},
 'Enrico': {'Blood Bowl': 24,
  'BloodRayne 2': 18,
  'Densha De Go!': 30,
  'Hyper Formation Soccer': 9,
  'I-Ninja': 5,
  'L.A. Rush': 15,
  'Looney Tunes: Back in Action': 12,
  'NASCAR: Dirt to Daytona': 29,
  'Persona 4: Arena Ultimax': 14,
  'Power Pro Kun Pocket 3': 16,
  'Re-Volt': 12,
  'Shining Blade': 4,
  'The Legend of Heroes: Trails in the Sky Third Chapter': 29,
  'Wheel of Fortune: 2nd Edition': 22,
  'World Soccer Winning Eleven 8: Liveware Evolution': 14,
  'Yu-Gi-Oh! Dark Duel Stories': 9,
  'ZhuZhu Pets: Quest for Zhu': 18},
 'Etienne': {},
 'Gene': {'America Oudan Ultra-Quiz': 15,
  'Call of Duty 3': 29,
  'Digimon World DS': 28,
  'Etrian Odyssey': 19,
  'Fatal Frame III: The Tormented': 2,
  'Gundam Breaker': 24,
  'July': 9,
  'Katekyoo Hitman Reborn! DS: Flame Rumble Hyper - Moeyo Mirai': 3,
  'Kenshuui Tendo Dokuta': 21,
  'Kiniro no Corda 2 Encore': 23,
  'Medarot 4: Kabuto / Kuwagata Version': 28,
  'MotionSports: Adrenaline': 26,
  'NBA 2K16': 5,
  'NHL 16': 11,
  'SpongeBob SquarePants featuring Nicktoons: Globs of Doom': 6,
  'Titan Quest': 14,
  "Tom Clancy's Splinter Cell": 27,
  'Ukiyo no Roushi': 3,
  'Vin Diesel: Wheelman': 8,
  'Wipeout: The Game': 1},
 'Gennifer': {'Madagascar: Escape 2 Africa': 6},
 'Minor': {'Agatha Christie: Peril at End House': 8,
  "America's Army: Rise of a Soldier": 3,
  'Atari Anthology': 22,
  'Athens 2004': 4,
  'Captain Toad: Treasure Tracker': 17,
  'D.Gray-man: Kami no Shitotachi': 5,
  "Disney's Magical Quest 3 Starring Mickey and Donald": 15,
  'Doom': 18,
  'Dungeon Siege III': 27,
  'Fishing Master (jp sales)': 1,
  'Iron Man': 18,
  'My Baby 3 & Friends': 10,
  'Ouka Sengoku Portable': 14,
  'Rayman 2: The Great Escape': 4,
  'Red Stone DS: Akaki Ishi ni Michibikareshi Monotachi': 19,
  'Ring of Red': 24,
  'RoadKill': 6,
  'Scared Rider Xechs': 19,
  'Silent Hill: Shattered Memories': 3,
  "The King of Fighters '96": 3}}


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
print("\n\n##### VIZINHOS MAIS PRÓXIMOS #####")  
print (computeNearestNeighbor('Gennifer', users))

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
 
print("\n\n##### RECOMENDAÇÃO #####\n\n\n")  
print(recommend('Gennifer', users))
