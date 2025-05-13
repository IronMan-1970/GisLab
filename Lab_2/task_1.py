# GIS Analysis Script

import geopandas as gpd
import rasterio
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
from pyproj import Transformer
import folium
import numpy as np

# 1. Load Vector and Raster Data
def load_data(vector_path, raster_path):
    try:
        vector_data = gpd.read_file(vector_path)
        raster_data = rasterio.open(raster_path)
        print("Data loaded successfully.")
        return vector_data, raster_data
    except Exception as e:
        print(f"Failed to load data: {e}")

# 2. Check and Reproject CRS
def check_and_reproject(vector_data, crs):
    print(f"Original CRS: {vector_data.crs}")
    if vector_data.crs != crs:
        vector_data = vector_data.to_crs(crs)
        print(f"Reprojected to: {crs}")
    else:
        print("No re-projection needed.")
    return vector_data

# 3. Analytical Operations
## 3.1 Calculate Area of Administrative Unit
def calculate_area(vector_data, column):
    vector_data['Area'] = vector_data.geometry.area
    print(vector_data[[column, 'Area']])

## 3.2 Calculate Length of Roads/Rivers
def calculate_length(vector_data, column):
    vector_data['Length'] = vector_data.geometry.length
    print(vector_data[[column, 'Length']])

## 3.3 Filter Points by Administrative Unit
def filter_points(vector_data, admin_unit):
    filtered_points = vector_data[vector_data['admin_unit'] == admin_unit]
    print(f"Filtered points for {admin_unit}:")
    print(filtered_points)
    return filtered_points

## 3.4 Find Points Around an Object
def points_within_buffer(vector_data, buffer_distance):
    buffer = vector_data.geometry.buffer(buffer_distance)
    result = vector_data[vector_data.geometry.within(buffer.unary_union)]
    print(f"Found {len(result)} points within buffer of {buffer_distance}m.")
    return result

## 3.5 Analyze Raster Data (Height Analysis)
def analyze_raster(raster_data):
    data = raster_data.read(1)
    print(f"Raster data statistics:\n Min: {data.min()}\n Max: {data.max()}\n Mean: {np.mean(data)}")
    plt.imshow(data, cmap='terrain')
    plt.colorbar(label='Elevation (m)')
    plt.show()

# 4. Visualization
def visualize_data(vector_data, result_data, output_map):
    m = folium.Map(location=[48.3794, 31.1656], zoom_start=6)
    folium.GeoJson(vector_data.to_json(), name='Base Layer').add_to(m)
    folium.GeoJson(result_data.to_json(), name='Analysis Result', style_function=lambda x: {'color': 'red'}).add_to(m)

    # Add markers for points
    for idx, row in result_data.iterrows():
        folium.Marker(
            location=[row.geometry.y, row.geometry.x],
            popup=f"{row['admin_unit']}"
        ).add_to(m)

    folium.LayerControl().add_to(m)
    m.save(output_map)
    print(f"Map saved to {output_map}")


# Example Usage
# vector_data, raster_data = load_data('path_to_vector.shp', 'path_to_raster.tif')
# vector_data = check_and_reproject(vector_data, 'EPSG:4326')
# calculate_area(vector_data, 'admin_name')
# calculate_length(vector_data, 'road_name')
# result_data = filter_points(vector_data, 'Kyiv')
# analyze_raster(raster_data)
# visualize_data(vector_data, result_data, 'output_map.html')
