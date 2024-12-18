![resim](https://github.com/user-attachments/assets/f0594e60-8879-43b6-80e2-c4e65cfd0145)# Processing and Visualization of Building Footprint Data

This repository contains a Python script for processing and visualizing building footprint data derived from the [Microsoft Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) project. The script processes GeoJSON data, visualizes it on an interactive map, and exports the processed data in GeoJSON format.

## Features
- Reads compressed GeoJSON data from `.csv.gz` files.
- Identifies data within the Ankara province boundary from the entire dataset of Turkey in the file `quadkey_list.py`. It provides the quadkey values for the data inside Ankara's boundary to the user.
- Extracts building properties such as height, confidence, and geometry type from the identified quadkeys.
- Converts building coordinates into a structured DataFrame.
- Visualizes building locations on an interactive map using OpenStreetMap.
- Exports processed data to GeoJSON format for further analysis.

## Requirements
Ensure you have the following Python libraries installed:
- `pandas`
- `json`
- `gzip`
- `folium`

You can install the required packages using the following command:
```bash
pip install pandas folium
```


## Usage
1. **Download the Data**:
   Download the building footprint data from the [Microsoft Global ML Building Footprints GitHub repository](https://github.com/microsoft/GlobalMLBuildingFootprints).

2. **Prepare Your File**:
   Place the compressed GeoJSON file (e.g., `part-00006-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz`) in the same directory as the script.

3. **Run the Script**:
   Execute the script in your terminal using the following command:
   ```bash
   python your_script_name.py
   ```

4. **Outputs**:
   - A GeoJSON file (`bina_konumlari.geojson`) containing processed building data.
   - An interactive map saved as an HTML file (`bina_konumlari.html`).
![resim](https://github.com/user-attachments/assets/6494ecca-876b-4cb4-b8ab-67ac4410acc8)

## File Descriptions
1. **`quadkey_list.py`**:
   - Identifies data within Ankara province boundaries from the entire Turkey dataset available at [this source](https://minedbuildings.z5.web.core.windows.net/global-buildings/dataset-links.csv). It provides the quadkey values of the data within Ankara's boundaries to the user.

![resim](https://github.com/user-attachments/assets/7ccc97d5-10c4-4e23-8c81-f1ed6ded5226)

2. **`read_data.py`**:
   - **`read_geojson_data()`**: Reads compressed GeoJSON data and converts it into a structured DataFrame.
   - **`export_to_geojson()`**: Exports processed data to a new GeoJSON file.
   - **`visualize_buildings()`**: Creates an interactive map of building locations using OpenStreetMap.
   
![resim](https://github.com/user-attachments/assets/79b36ff1-7fef-4fb9-9425-c542b35ad825)


## Example Outputs
**DataFrame Overview:**
| height | confidence | geometry_type | longitude | latitude |
|--------|------------|---------------|-----------|----------|
| -1.0   | -1.0       | Polygon       | 32.343434 | 38.872817|

**Interactive Map:**
The generated map displays building locations as blue markers. Open the `bina_konumlari.html` file in your browser to view it interactively.

## Data Attribution
This project utilizes data provided by the [Microsoft Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) repository. All rights to the data belong to Microsoft.

## License
This project is open-source and available under the MIT License. See the `LICENSE` file for more details.

---
For questions or contributions, feel free to open an issue or submit a pull request.

