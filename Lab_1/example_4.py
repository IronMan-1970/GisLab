import math
latl = 50.1657
longl = 29.9075
lat2 = 50.0897
long2 = 29.8977
rLatl = math.radians(latl)
rLongl = math.radians(longl)
rLat2 = math.radians(lat2)
rLong2 = math.radians(long2)
dLat = rLat2 - rLatl
dLong = rLong2 - rLongl
a = math.sin(dLat / 2 ) **2 + math.cos(rLatl) * math.cos(rLat2) * math.sin(dLong/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
distance = 6371 * c
print("Відстань по дузі великого кола складає {:0.0f} км.".format(distance))
