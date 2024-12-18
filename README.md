# Building Footprint Data Processing and Visualization

This repository contains a Python script for processing and visualizing building footprint data derived from the [Microsoft Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) project. The script processes GeoJSON data, visualizes it on an interactive map, and exports the processed data in GeoJSON format.

## Features
- Reads compressed GeoJSON data from `.csv.gz` files.
- Extracts building properties such as height, confidence, and geometry type.
- Converts building coordinates into a structured DataFrame.
- Visualizes the building locations using OpenStreetMap with interactive zooming functionality.
- Exports processed data to GeoJSON format for further analysis.

## Requirements
Make sure you have the following Python libraries installed:
- `pandas`
- `json`
- `gzip`
- `folium`

You can install the required packages using pip:
```bash
pip install pandas folium
```

## Usage
1. **Download the Data**:
   Download the building footprint data from the [Microsoft Global ML Building Footprints GitHub repository](https://github.com/microsoft/GlobalMLBuildingFootprints).

2. **Prepare Your File**:
   Place the compressed GeoJSON file (e.g., `part-00006-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz`) in the same directory as the script.

3. **Run the Script**:
   Execute the script in your terminal:
   ```bash
   python your_script_name.py
   ```

4. **Outputs**:
   - A GeoJSON file (`bina_konumlari.geojson`) containing processed building data.
   - An interactive map saved as `bina_konumlari.html`.

## File Descriptions
- **`read_geojson_data()`**: Reads and processes compressed GeoJSON data into a structured DataFrame.
- **`export_to_geojson()`**: Exports processed data to a new GeoJSON file.
- **`visualize_buildings()`**: Generates an interactive map of building locations using OpenStreetMap.

## Example Output
**DataFrame Overview:**
| height | confidence | geometry_type | longitude | latitude |
|--------|------------|---------------|-----------|----------|
| -1.0   | -1.0       | Polygon       | 32.343434 | 38.872817|

**Interactive Map:**
The generated map shows building locations as blue markers. Open the `bina_konumlari.html` file in your browser to view it interactively.

## Data Attribution
This project utilizes data provided by the [Microsoft Global ML Building Footprints](https://github.com/microsoft/GlobalMLBuildingFootprints) repository. All credit for the data goes to Microsoft.

## License
This project is open-source and available under the MIT License. See the `LICENSE` file for more details.

---
For questions or contributions, please feel free to open an issue or submit a pull request.

