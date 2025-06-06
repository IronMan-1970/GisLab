import osgeo.ogr
shapefile = osgeo.ogr.Open("ukraine_Village_Councils_level_3.shp")
numLayers = shapefile. GetLayerCount ()
print("Файл фігур містить {} шарів".format(numLayers))
print ()
for layerNum in range(numLayers):
    layer = shapefile.GetLayer(layerNum)
    spatialRef = layer.GetSpatialRef( ) .ExportToProj4()
    numFeatures = layer.GetFeatureCount()
    print("шар {} має просторову прив’язку {}".format(layerNum, spatialRef))
    print ("шар {} містить {} геооб’єктів: " . format( layerNum, numFeatures))
    print ()
for featureNum in range(numFeatures):
   feature = layer.GetFeature(featureNum)
   featureName = feature.GetField("shape3")
   print ("Геооб’єкт {} під назвою {}". format(featureNum, featureName))

