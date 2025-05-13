import osgeo.ogr
shapefile = osgeo.ogr.Open("ukraine_Village_Councils_level_3.shp")
layer = shapefile. GetLayer(0)
feature = layer.GetFeature(9)
print("Геооб’єкт № 9 має наступні атрибути:")
print()
attributes = feature.items()
for key,value in attributes.items():
    print("{} = {}".format(key, value))
geometry = feature.GetGeometryRef()
geometryName = geometry.GetGeometryName()
print ()
print ("Геометрія заданного Геооб’єкту представляє собою {} ".format(geometryName))
