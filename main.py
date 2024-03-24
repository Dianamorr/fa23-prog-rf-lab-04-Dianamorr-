"""
>>> x = [1, 3, [5, 7], 9]
>>> x[2][1]
7
>>> x = [[7]]
>>> x[0][0]
7
>>> x = [3, 2, 1, [9, 8, 7]]
>>> x[3][2]
7
>>> x = [[3, [5, 7], 9]]
>>> x[0][1][1]
7
"""
"""
>>> lst = [3, 2, 7, [84, 83, 82]]
>>> lst[4]
IndexError: list index out of range
>>> lst[3][0]
84
"""
"""
>>> [x*x for x in range(5)]
[0, 1, 4, 9, 16]
>>> [n for n in range(10) if n % 2 == 0]
[0, 2, 4, 6, 8]
>>> ones = [1 for i in ["привет", "как", "сам"]]
>>> ones + [str(i) for i in [6, 3, 8, 4]]
[1, 1, 1, '6', '3', '8', '4']
>>> [i+5 for i in [n for n in range(1,4)]]
[6, 7, 8]
"""
"""
>>> [i**2 for i in range(10) if i < 3]
[0, 1, 4]
>>> lst = ['привет' for i in [1, 2, 3]]
>>> print(lst)
['привет', 'привет', 'привет']
>>> lst + [i for i in ['1', '2', '3']]
['привет', 'привет', 'привет', '1', '2', '3']
"""



def if_this_not_that(i_list, this):
    """
    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    for i in i_list:
        if i <= this:
            print("that")
        else:
            print(i)

def make_city(name, lat, lon):
    return [name, lat, lon]

def get_name(city):
    return city[0]

def get_lat(city):
    return city[1]

def get_lon(city):
    return city[2]



from math import sqrt
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    x1, y1 = get_lat(city1), get_lon(city1)
    x2, y2 = get_lat(city2), get_lon(city2)
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)



def closer_city(lat, lon, city1, city2):
    """
    Возвращает название города city1 или города city2 в зависимости от того,
    какой из них ближе к координате (lat, lon).

    >>> moscow = make_city('Москва', 55.75, 37.616667)
    >>> saint_petersburg = make_city('Питер', 59.9375, 30.308611)
    >>> closer_city(57.616667, 39.85, moscow, saint_petersburg)
    'Москва'
    >>> london = make_city('Лондон', 51.507222, -0.1275)
    >>> mumbai = make_city('Мумбаи', 18.975, 72.825833)
    >>> closer_city(57.616667, 39.85, london, mumbai)
    'Лондон'
    """
    city = make_city('Ярославль', lat, lon)
    if distance(city, city1) <= distance(city, city2):
        return get_name(city1)
    else:
        return get_name(city2)


make_city = lambda name, lat, lon: {'name': name, 'lat': lat, 'lon': lon}
get_name = lambda city: city['name']
get_lat = lambda city: city['lat']
get_lon = lambda city: city['lon']

"""
>>> city = make_city('Ярославль', 57.616667, 39.85)
>>> get_name(city)
'Ярославль'
>>> get_lat(city)
57.616667
>>> get_lon(city)
39.85
"""