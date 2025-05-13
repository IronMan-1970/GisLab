import osgeo.ogr
def findPoints(geometry, results):
    for i in range(geometry.GetPointCount()):
          x,y,z = geometry.GetPoint(i)
          if results['east'] == None or results ['east'][0] < x:
                results['east'] = (x,y)
          if results['west'] == None or results ['west'][0] > x:
                results['west'] = (x,y)
    for i in range(geometry.GetGeometryCount()):
          findPoints(geometry.GetGeometryRef(i), results)
shapefile = osgeo.ogr.Open("ukraine_Village_Councils_level_3.shp")
layer = shapefile.GetLayer(0)
feature = layer.GetFeature(9)
geometry = feature.GetGeometryRef()
results = {'east' : None, 'west' : None}
findPoints (geometry, results)
print ("Найсхідніша точка: ( {:.4f}, {:.4f})".format(results['east'][0], results['east'][1]))
print ("Найзахідніша точка: ( {:.4f}, {:.4f})". format(results['west'][0], results['west'][1]))
