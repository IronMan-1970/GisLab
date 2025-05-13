import osgeo.ogr
def findPoints(geometry, results):
    for i in range(geometry.GetPointCount()):
          x,y,z = geometry.GetPoint(i)
          if results['north'] == None or results ['north'][1] < y:
                results['north'] = (x,y)
          if results['south'] == None or results ['south'][1] > y:
                results['south'] = (x,y)
    for i in range(geometry.GetGeometryCount()):
          findPoints(geometry.GetGeometryRef(i), results)
shapefile = osgeo.ogr.Open("ukraine_Village_Councils_level_3.shp")
layer = shapefile.GetLayer(0)
feature = layer.GetFeature(9)
geometry = feature.GetGeometryRef()
results = {'north' : None, 'south' : None}
findPoints (geometry, results)
print ("Найпівнічніша точка: ( {:.4f}, {:.4f})".format(results['north'][0], results['north'][1]))
print ("найпівденніша точка: ( {:.4f}, {:.4f})". format(results['south'][0], results['south'][1]))
