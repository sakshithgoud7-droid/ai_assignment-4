import geopandas as gpd
import matplotlib.pyplot as plt
import fiona
import random

fiona.drvsupport.supported_drivers['KML'] = 'rw'

file_path = "telangana.kml"
gdf = gpd.read_file(file_path, driver='KML')
name_col = "District" if "District" in gdf.columns else "Name"

adjacencies = {}
for index, row in gdf.iterrows():
    neighbors = gdf[gdf.geometry.touches(row.geometry)][name_col].tolist()
    adjacencies[row[name_col]] = neighbors

districts = list(adjacencies.keys())
colors = ["red", "green", "blue", "yellow"]

def is_valid(district, color, assignments, neighbors_dict):
    for neighbor in neighbors_dict.get(district, []):
        if neighbor in assignments and assignments[neighbor] == color:
            return False
    return True

def solve_csp(assignments, districts_list, color_list, neighbors_dict):
    if len(assignments) == len(districts_list):
        return assignments
    
    unassigned = [d for d in districts_list if d not in assignments]
    current = max(unassigned, key=lambda d: len(neighbors_dict[d]))
    
    shuffled_colors = color_list[:]
    random.shuffle(shuffled_colors)
    
    for color in shuffled_colors:
        if is_valid(current, color, assignments, neighbors_dict):
            assignments[current] = color
            if solve_csp(assignments, districts_list, color_list, neighbors_dict):
                return assignments
            assignments.pop(current)
    return None

csp_solution = solve_csp({}, districts, colors, adjacencies)

def get_final_color(row):
    return csp_solution.get(row[name_col], "gray")

gdf["color"] = gdf.apply(get_final_color, axis=1)

fig, ax = plt.subplots(figsize=(15, 15))
gdf.plot(ax=ax, color=gdf["color"], edgecolor="black", linewidth=1.5)

for idx, row in gdf.iterrows():
    if row.geometry:
        c = row.geometry.centroid
        ax.text(c.x, c.y, str(row[name_col]), fontsize=8, ha='center', weight='bold',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=1))

plt.title("Telangana CSP Map - Automated Border Detection", fontsize=16)
plt.axis('off')
plt.show()
