import osgeo.ogr

def get_centroid(feature):
    geometry = feature.GetGeometryRef()
    centroid = geometry.Centroid()
    return centroid.GetY(), centroid.GetX()  # (широта, довгота)

shapefile = osgeo.ogr.Open("ukraine_Village_Councils_level_3.shp")
layer = shapefile.GetLayer(0)

feature_id = 5  # заміни ID за потреби
feature = layer.GetFeature(feature_id)

if feature is None:
    print(f"Об'єкта з ID = {feature_id} не існує.")
else:
    lat, lon = get_centroid(feature)
    print(f"Центральна точка об'єкта з ID {feature_id}: (широта: {lat:.6f}, довгота: {lon:.6f})")
