from math import sin, cos, sqrt, atan2, radians
from aiogram import types
from locations import filiallar

    


async def distance(lat1, lon1, lon2, lat2):
    # Approximate radius of earth in km
    R = 6373.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = int(R * c)

    return distance



async def find_near_location(lat1, lon1):
    masofa = []
    for nomi, lokatsiya in filiallar:
        masofa.append(
            (nomi, await distance(
                lat1 = lat1,
                lon1 = lon1,
                lat2 = lokatsiya['lat'],
                lon2 = lokatsiya['lon']), 
           (lokatsiya['lat'], lokatsiya['lon'])))
    print(masofa)
    return sorted(masofa, key=lambda x: x[1])[:1]