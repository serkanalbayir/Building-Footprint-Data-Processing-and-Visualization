import pandas as pd
import json
import gzip
import folium

# Dosya okuma fonksiyonu
def read_geojson_data(file_path):
    try:
        # GeoJSON verilerini depolamak için liste
        features = []

        # gzip dosyasını satır satır oku
        with gzip.open(file_path, 'rt', encoding='utf-8') as f:
            for line in f:
                # Her satırı JSON olarak parse et
                feature = json.loads(line.strip())

                # Özellikleri ve geometriyi düzleştir
                properties = feature.get('properties', {})
                geometry = feature.get('geometry', {})
                coordinates = geometry.get('coordinates', [[]])[0]  # İlk polygon'u al

                # Veriyi düzleştirilmiş dictionary olarak sakla
                flat_feature = {
                    'height': properties.get('height', None),
                    'confidence': properties.get('confidence', None),
                    'geometry_type': geometry.get('type', None),
                }

                # Koordinatları ekle
                if coordinates:
                    flat_feature['longitude'] = coordinates[0][0]
                    flat_feature['latitude'] = coordinates[0][1]

                features.append(flat_feature)

        # Liste'yi DataFrame'e çevir
        df = pd.DataFrame(features)

        print("\nVeri başarıyla okundu!")
        print(f"Toplam satır sayısı: {len(df)}")
        print(f"Sütunlar: {df.columns.tolist()}")
        print("\nİlk 5 satır:")
        print(df.head())

        return df

    except Exception as e:
        print(f"Veri okuma hatası: {e}")
        return None

# GeoJSON formatında dışa aktarma fonksiyonu
def export_to_geojson(df, output_file):
    try:
        # GeoJSON özelliklerini oluştur
        features = []
        for _, row in df.iterrows():
            feature = {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [row['longitude'], row['latitude']]
                },
                "properties": {
                    "height": row['height'],
                    "confidence": row['confidence'],
                    "geometry_type": row['geometry_type']
                }
            }
            features.append(feature)

        # GeoJSON yapısını oluştur
        geojson_data = {
            "type": "FeatureCollection",
            "features": features
        }

        # Dosyaya yaz
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(geojson_data, f, ensure_ascii=False, indent=4)

        print(f"\nVeri '{output_file}' dosyasına başarıyla GeoJSON formatında kaydedildi.")

    except Exception as e:
        print(f"GeoJSON dışa aktarma hatası: {e}")

# OpenStreetMap ile görselleştirme fonksiyonu
def visualize_buildings(df):
    try:
        # Harita oluştur
        map_center = [df['latitude'].mean(), df['longitude'].mean()]
        m = folium.Map(location=map_center, zoom_start=13)

        # Veriyi haritaya ekle
        for _, row in df.iterrows():
            folium.CircleMarker(
                location=[row['latitude'], row['longitude']],
                radius=1,
                color='blue',
                fill=True,
                fill_opacity=0.5
            ).add_to(m)

        # Haritayı kaydet ve göster
        m.save('bina_konumlari.html')
        print("\nHarita 'bina_konumlari.html' olarak kaydedildi.")

    except Exception as e:
        print(f"Görselleştirme hatası: {e}")

if __name__ == "__main__":
    file_path = "part-00006-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz"  # Dosya yolunuzu buraya yazın

    print("GeoJSON veri okuma denemesi:")
    print("-" * 50)

    # Veri okuma
    data = read_geojson_data(file_path)

    if data is not None:
        # GeoJSON formatında dışa aktarma
        export_to_geojson(data, "bina_konumlari.geojson")

        # Görselleştirme
        visualize_buildings(data)

        # Bazı temel istatistikler
        print("\nVeri İstatistikleri:")
        print("-" * 50)
        print(f"Toplam bina sayısı: {len(data):,}")
        print(f"\nKoordinat aralıkları:")
        print(f"Boylam: {data['longitude'].min():.6f} - {data['longitude'].max():.6f}")
        print(f"Enlem: {data['latitude'].min():.6f} - {data['latitude'].max():.6f}")
