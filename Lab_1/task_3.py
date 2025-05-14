import osgeo.ogr
import math

def get_centroid_coords(feature):
    geometry = feature.GetGeometryRef()
    centroid = geometry.Centroid()
    return centroid.GetY(), centroid.GetX()  # Повертаємо як (lat, lon)

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Радіус Землі в км
    rLat1, rLon1 = math.radians(lat1), math.radians(lon1)
    rLat2, rLon2 = math.radians(lat2), math.radians(lon2)
    dLat = rLat2 - rLat1
    dLon = rLon2 - rLon1
    a = math.sin(dLat / 2)**2 + math.cos(rLat1) * math.cos(rLat2) * math.sin(dLon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

# Відкриваємо файл
shapefile = osgeo.ogr.Open("ukraine_Village_Councils_level_3.shp")
layer = shapefile.GetLayer(0)

# Вибір двох об'єктів (наприклад, ID 5 і 9 — заміни на потрібні)
feature1 = layer.GetFeature(5)
feature2 = layer.GetFeature(9)

# Отримуємо центроїди
lat1, lon1 = get_centroid_coords(feature1)
lat2, lon2 = get_centroid_coords(feature2)

# Обчислюємо відстань
distance_km = haversine(lat1, lon1, lat2, lon2)

print(f"Відстань між центральними точками об'єктів ID 5 і 9: {distance_km:.2f} км")
