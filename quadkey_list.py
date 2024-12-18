import re
import mercantile

# Metni değişken olarak tanımlayın
data = """
Turkey,120322312,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120322312/part-00120-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,71.7KB,2024-12-02
Turkey,120322321,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120322321/part-00039-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.2MB,2024-12-02
Turkey,120322323,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120322323/part-00115-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.2MB,2024-12-02
Turkey,120322330,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120322330/part-00130-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.5MB,2024-12-02
Turkey,120322331,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120322331/part-00041-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.8MB,2024-12-02
Turkey,120322332,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120322332/part-00081-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,8.5MB,2024-12-02
Turkey,120322333,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120322333/part-00016-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,14.7MB,2024-12-02
Turkey,120323220,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323220/part-00016-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.9KB,2024-12-02
Turkey,120323222,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323222/part-00143-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,22.1MB,2024-12-02
Turkey,120323223,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323223/part-00092-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,36.5MB,2024-12-02
Turkey,120323232,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323232/part-00042-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.6MB,2024-12-02
Turkey,120323233,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323233/part-00089-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.6MB,2024-12-02
Turkey,120323321,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323321/part-00114-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.6MB,2024-12-02
Turkey,120323322,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323322/part-00035-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.9MB,2024-12-02
Turkey,120323323,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323323/part-00012-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,11.8MB,2024-12-02
Turkey,120323330,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323330/part-00089-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.3MB,2024-12-02
Turkey,120323331,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323331/part-00061-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.6MB,2024-12-02
Turkey,120323332,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323332/part-00102-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.1MB,2024-12-02
Turkey,120323333,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120323333/part-00032-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.0MB,2024-12-02
Turkey,120332203,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332203/part-00114-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,60.9KB,2024-12-02
Turkey,120332212,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332212/part-00188-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1005.0B,2024-12-02
Turkey,120332220,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332220/part-00000-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.1MB,2024-12-02
Turkey,120332221,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332221/part-00196-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.5MB,2024-12-02
Turkey,120332222,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332222/part-00007-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.2MB,2024-12-02
Turkey,120332223,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332223/part-00057-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.1MB,2024-12-02
Turkey,120332230,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332230/part-00104-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.5MB,2024-12-02
Turkey,120332231,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332231/part-00016-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.6MB,2024-12-02
Turkey,120332232,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332232/part-00066-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.0MB,2024-12-02
Turkey,120332233,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332233/part-00090-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,12.0MB,2024-12-02
Turkey,120332322,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332322/part-00132-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,11.3MB,2024-12-02
Turkey,120332323,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332323/part-00071-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.5MB,2024-12-02
Turkey,120332333,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120332333/part-00068-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.7MB,2024-12-02
Turkey,120333222,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120333222/part-00163-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.7MB,2024-12-02
Turkey,120333223,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120333223/part-00086-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.7MB,2024-12-02
Turkey,120333231,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120333231/part-00064-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,211.0B,2024-12-02
Turkey,120333232,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120333232/part-00045-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.3MB,2024-12-02
Turkey,120333233,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120333233/part-00071-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.6MB,2024-12-02
Turkey,120333320,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120333320/part-00000-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,223.8KB,2024-12-02
Turkey,120333322,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120333322/part-00121-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.5MB,2024-12-02
Turkey,120333323,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=120333323/part-00194-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.1MB,2024-12-02
Turkey,122100101,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100101/part-00088-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.5MB,2024-12-02
Turkey,122100102,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100102/part-00045-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,535.8KB,2024-12-02
Turkey,122100103,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100103/part-00143-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.7MB,2024-12-02
Turkey,122100110,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100110/part-00042-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.1MB,2024-12-02
Turkey,122100111,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100111/part-00141-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.8MB,2024-12-02
Turkey,122100112,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100112/part-00040-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.9MB,2024-12-02
Turkey,122100113,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100113/part-00015-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,8.7MB,2024-12-02
Turkey,122100120,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100120/part-00058-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,36.8KB,2024-12-02
Turkey,122100121,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100121/part-00084-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.1MB,2024-12-02
Turkey,122100123,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100123/part-00030-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.3MB,2024-12-02
Turkey,122100130,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100130/part-00193-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,10.0MB,2024-12-02
Turkey,122100131,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100131/part-00089-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,12.8MB,2024-12-02
Turkey,122100132,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100132/part-00138-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,11.2MB,2024-12-02
Turkey,122100133,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100133/part-00022-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,10.2MB,2024-12-02
Turkey,122100301,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100301/part-00001-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.9MB,2024-12-02
Turkey,122100303,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100303/part-00139-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,404.8KB,2024-12-02
Turkey,122100310,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100310/part-00070-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,33.5MB,2024-12-02
Turkey,122100311,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100311/part-00111-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,14.1MB,2024-12-02
Turkey,122100312,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100312/part-00146-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,15.3MB,2024-12-02
Turkey,122100313,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100313/part-00078-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,20.9MB,2024-12-02
Turkey,122100330,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100330/part-00110-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.6MB,2024-12-02
Turkey,122100331,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100331/part-00116-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,11.5MB,2024-12-02
Turkey,122100332,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100332/part-00105-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.1MB,2024-12-02
Turkey,122100333,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122100333/part-00177-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.6MB,2024-12-02
Turkey,122101000,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101000/part-00007-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.2MB,2024-12-02
Turkey,122101001,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101001/part-00073-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,29.2MB,2024-12-02
Turkey,122101002,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101002/part-00130-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,10.3MB,2024-12-02
Turkey,122101003,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101003/part-00124-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,25.2MB,2024-12-02
Turkey,122101010,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101010/part-00073-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,19.7MB,2024-12-02
Turkey,122101011,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101011/part-00017-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,21.4MB,2024-12-02
Turkey,122101012,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101012/part-00140-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,8.6MB,2024-12-02
Turkey,122101013,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101013/part-00162-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.4MB,2024-12-02
Turkey,122101020,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101020/part-00119-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.4MB,2024-12-02
Turkey,122101021,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101021/part-00197-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.2MB,2024-12-02
Turkey,122101022,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101022/part-00026-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.6MB,2024-12-02
Turkey,122101023,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101023/part-00172-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.1MB,2024-12-02
Turkey,122101030,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101030/part-00034-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.8MB,2024-12-02
Turkey,122101031,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101031/part-00179-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,10.7MB,2024-12-02
Turkey,122101032,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101032/part-00171-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.1MB,2024-12-02
Turkey,122101033,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101033/part-00119-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.4MB,2024-12-02
Turkey,122101100,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101100/part-00078-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,14.3MB,2024-12-02
Turkey,122101101,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101101/part-00014-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.9MB,2024-12-02
Turkey,122101102,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101102/part-00177-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.8MB,2024-12-02
Turkey,122101103,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101103/part-00154-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.4MB,2024-12-02
Turkey,122101110,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101110/part-00040-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.2MB,2024-12-02
Turkey,122101111,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101111/part-00180-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.0MB,2024-12-02
Turkey,122101112,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101112/part-00008-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,23.4MB,2024-12-02
Turkey,122101113,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101113/part-00088-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.7MB,2024-12-02
Turkey,122101120,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101120/part-00150-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.1MB,2024-12-02
Turkey,122101121,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101121/part-00030-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.1MB,2024-12-02
Turkey,122101122,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101122/part-00127-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.3MB,2024-12-02
Turkey,122101123,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101123/part-00069-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.0MB,2024-12-02
Turkey,122101130,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101130/part-00180-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,14.6MB,2024-12-02
Turkey,122101131,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101131/part-00107-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.6MB,2024-12-02
Turkey,122101132,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101132/part-00006-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.8MB,2024-12-02
Turkey,122101133,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101133/part-00168-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.7MB,2024-12-02
Turkey,122101200,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101200/part-00019-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,10.3MB,2024-12-02
Turkey,122101201,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101201/part-00148-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,8.6MB,2024-12-02
Turkey,122101202,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101202/part-00030-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,13.5MB,2024-12-02
Turkey,122101203,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101203/part-00197-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,13.4MB,2024-12-02
Turkey,122101210,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101210/part-00159-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.4MB,2024-12-02
Turkey,122101211,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101211/part-00070-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,11.5MB,2024-12-02
Turkey,122101212,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101212/part-00181-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.5MB,2024-12-02
Turkey,122101213,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101213/part-00004-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,8.9MB,2024-12-02
Turkey,122101220,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101220/part-00065-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.7MB,2024-12-02
Turkey,122101221,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101221/part-00122-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.4MB,2024-12-02
Turkey,122101222,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101222/part-00113-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,8.8MB,2024-12-02
Turkey,122101223,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101223/part-00191-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,9.1MB,2024-12-02
Turkey,122101230,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101230/part-00158-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.9MB,2024-12-02
Turkey,122101231,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101231/part-00163-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.9MB,2024-12-02
Turkey,122101232,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101232/part-00120-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.1MB,2024-12-02
Turkey,122101233,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101233/part-00105-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,21.7MB,2024-12-02
Turkey,122101300,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101300/part-00087-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.3MB,2024-12-02
Turkey,122101301,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101301/part-00010-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.9MB,2024-12-02
Turkey,122101302,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101302/part-00050-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.4MB,2024-12-02
Turkey,122101303,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101303/part-00105-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.0MB,2024-12-02
Turkey,122101310,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101310/part-00111-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.3MB,2024-12-02
Turkey,122101311,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101311/part-00016-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.4MB,2024-12-02
Turkey,122101312,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101312/part-00069-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,17.6MB,2024-12-02
Turkey,122101313,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101313/part-00117-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.8MB,2024-12-02
Turkey,122101320,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101320/part-00169-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.1MB,2024-12-02
Turkey,122101321,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101321/part-00153-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.9MB,2024-12-02
Turkey,122101322,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101322/part-00194-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,11.9MB,2024-12-02
Turkey,122101323,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101323/part-00163-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.5MB,2024-12-02
Turkey,122101330,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101330/part-00027-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.6MB,2024-12-02
Turkey,122101331,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101331/part-00112-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.0MB,2024-12-02
Turkey,122101332,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101332/part-00008-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.0MB,2024-12-02
Turkey,122101333,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122101333/part-00190-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.6MB,2024-12-02
Turkey,122102111,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122102111/part-00096-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.4KB,2024-12-02
Turkey,122103001,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122103001/part-00140-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.2MB,2024-12-02
Turkey,122103010,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122103010/part-00008-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.5MB,2024-12-02
Turkey,122103011,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122103011/part-00113-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.0MB,2024-12-02
Turkey,122103101,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122103101/part-00099-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.1MB,2024-12-02
Turkey,122103110,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122103110/part-00134-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.6MB,2024-12-02
Turkey,122103111,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122103111/part-00117-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.9MB,2024-12-02
Turkey,122103112,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122103112/part-00081-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,15.9KB,2024-12-02
Turkey,122110000,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110000/part-00143-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.1MB,2024-12-02
Turkey,122110001,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110001/part-00190-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,8.4MB,2024-12-02
Turkey,122110002,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110002/part-00060-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.7MB,2024-12-02
Turkey,122110003,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110003/part-00130-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.8MB,2024-12-02
Turkey,122110010,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110010/part-00024-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,9.4MB,2024-12-02
Turkey,122110011,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110011/part-00046-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.7MB,2024-12-02
Turkey,122110012,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110012/part-00133-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.7MB,2024-12-02
Turkey,122110013,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110013/part-00130-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,8.1MB,2024-12-02
Turkey,122110020,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110020/part-00116-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.5MB,2024-12-02
Turkey,122110021,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110021/part-00166-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.7MB,2024-12-02
Turkey,122110022,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110022/part-00019-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.9MB,2024-12-02
Turkey,122110023,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110023/part-00172-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.7MB,2024-12-02
Turkey,122110030,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110030/part-00116-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.6MB,2024-12-02
Turkey,122110031,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110031/part-00128-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.8MB,2024-12-02
Turkey,122110032,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110032/part-00088-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.6MB,2024-12-02
Turkey,122110033,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110033/part-00132-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.3MB,2024-12-02
Turkey,122110100,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110100/part-00189-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,9.2MB,2024-12-02
Turkey,122110101,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110101/part-00072-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,13.1MB,2024-12-02
Turkey,122110102,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110102/part-00141-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.1MB,2024-12-02
Turkey,122110103,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110103/part-00153-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.4MB,2024-12-02
Turkey,122110110,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110110/part-00093-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,9.2MB,2024-12-02
Turkey,122110111,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110111/part-00122-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,8.9MB,2024-12-02
Turkey,122110112,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110112/part-00033-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.8MB,2024-12-02
Turkey,122110113,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110113/part-00150-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.5MB,2024-12-02
Turkey,122110120,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110120/part-00020-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.2MB,2024-12-02
Turkey,122110121,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110121/part-00102-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.0MB,2024-12-02
Turkey,122110122,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110122/part-00005-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.5MB,2024-12-02
Turkey,122110123,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110123/part-00000-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.0MB,2024-12-02
Turkey,122110130,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110130/part-00004-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.9MB,2024-12-02
Turkey,122110131,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110131/part-00047-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.4MB,2024-12-02
Turkey,122110132,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110132/part-00182-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.7MB,2024-12-02
Turkey,122110133,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110133/part-00002-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.7MB,2024-12-02
Turkey,122110200,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110200/part-00058-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,10.1MB,2024-12-02
Turkey,122110201,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110201/part-00078-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,10.2MB,2024-12-02
Turkey,122110202,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110202/part-00033-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.8MB,2024-12-02
Turkey,122110203,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110203/part-00096-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,9.0MB,2024-12-02
Turkey,122110210,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110210/part-00129-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,15.5MB,2024-12-02
Turkey,122110211,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110211/part-00124-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.0MB,2024-12-02
Turkey,122110212,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110212/part-00082-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.9MB,2024-12-02
Turkey,122110213,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110213/part-00011-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.5MB,2024-12-02
Turkey,122110220,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110220/part-00040-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.9MB,2024-12-02
Turkey,122110221,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110221/part-00185-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.8MB,2024-12-02
Turkey,122110222,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110222/part-00082-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.9MB,2024-12-02
Turkey,122110223,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110223/part-00012-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,16.9MB,2024-12-02
Turkey,122110230,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110230/part-00025-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.3MB,2024-12-02
Turkey,122110231,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110231/part-00175-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,9.7MB,2024-12-02
Turkey,122110232,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110232/part-00077-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,23.9MB,2024-12-02
Turkey,122110233,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110233/part-00010-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,12.3MB,2024-12-02
Turkey,122110300,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110300/part-00103-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.2MB,2024-12-02
Turkey,122110301,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110301/part-00068-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.1MB,2024-12-02
Turkey,122110302,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110302/part-00170-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.6MB,2024-12-02
Turkey,122110303,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110303/part-00061-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.9MB,2024-12-02
Turkey,122110310,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110310/part-00013-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,10.9MB,2024-12-02
Turkey,122110311,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110311/part-00094-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.9MB,2024-12-02
Turkey,122110312,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110312/part-00000-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.0MB,2024-12-02
Turkey,122110313,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110313/part-00036-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.2MB,2024-12-02
Turkey,122110320,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110320/part-00180-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,12.3MB,2024-12-02
Turkey,122110321,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110321/part-00034-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.9MB,2024-12-02
Turkey,122110322,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110322/part-00172-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.3MB,2024-12-02
Turkey,122110323,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110323/part-00006-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,17.0MB,2024-12-02
Turkey,122110330,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110330/part-00149-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.1MB,2024-12-02
Turkey,122110331,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110331/part-00045-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.5MB,2024-12-02
Turkey,122110332,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110332/part-00160-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.6MB,2024-12-02
Turkey,122110333,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122110333/part-00019-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,10.9MB,2024-12-02
Turkey,122111000,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111000/part-00068-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,11.0MB,2024-12-02
Turkey,122111001,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111001/part-00113-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.8MB,2024-12-02
Turkey,122111002,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111002/part-00059-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.4MB,2024-12-02
Turkey,122111003,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111003/part-00063-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.5MB,2024-12-02
Turkey,122111010,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111010/part-00048-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.1MB,2024-12-02
Turkey,122111011,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111011/part-00005-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.2MB,2024-12-02
Turkey,122111012,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111012/part-00109-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.9MB,2024-12-02
Turkey,122111013,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111013/part-00054-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.3MB,2024-12-02
Turkey,122111020,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111020/part-00160-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.3MB,2024-12-02
Turkey,122111021,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111021/part-00151-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.0MB,2024-12-02
Turkey,122111022,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111022/part-00190-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.3MB,2024-12-02
Turkey,122111023,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111023/part-00094-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.7MB,2024-12-02
Turkey,122111030,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111030/part-00149-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.1MB,2024-12-02
Turkey,122111031,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111031/part-00018-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.4MB,2024-12-02
Turkey,122111032,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111032/part-00076-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.5MB,2024-12-02
Turkey,122111033,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111033/part-00090-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.9MB,2024-12-02
Turkey,122111100,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111100/part-00162-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.3MB,2024-12-02
Turkey,122111101,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111101/part-00116-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.7MB,2024-12-02
Turkey,122111102,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111102/part-00133-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.0MB,2024-12-02
Turkey,122111103,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111103/part-00166-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.9MB,2024-12-02
Turkey,122111110,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111110/part-00121-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,605.8KB,2024-12-02
Turkey,122111112,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111112/part-00146-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.3MB,2024-12-02
Turkey,122111113,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111113/part-00009-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,518.6KB,2024-12-02
Turkey,122111120,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111120/part-00140-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.9MB,2024-12-02
Turkey,122111121,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111121/part-00189-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.1MB,2024-12-02
Turkey,122111122,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111122/part-00109-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.6MB,2024-12-02
Turkey,122111123,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111123/part-00141-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.3MB,2024-12-02
Turkey,122111130,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111130/part-00071-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.1MB,2024-12-02
Turkey,122111131,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111131/part-00001-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,832.7KB,2024-12-02
Turkey,122111132,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111132/part-00193-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.8MB,2024-12-02
Turkey,122111200,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111200/part-00070-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.6MB,2024-12-02
Turkey,122111201,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111201/part-00121-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.9MB,2024-12-02
Turkey,122111202,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111202/part-00060-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,6.0MB,2024-12-02
Turkey,122111203,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111203/part-00097-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,9.3MB,2024-12-02
Turkey,122111210,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111210/part-00178-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.7MB,2024-12-02
Turkey,122111211,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111211/part-00079-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.9MB,2024-12-02
Turkey,122111212,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111212/part-00178-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.6MB,2024-12-02
Turkey,122111213,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111213/part-00065-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.6MB,2024-12-02
Turkey,122111220,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111220/part-00153-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,5.4MB,2024-12-02
Turkey,122111221,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111221/part-00032-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,7.1MB,2024-12-02
Turkey,122111222,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111222/part-00080-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.8MB,2024-12-02
Turkey,122111223,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111223/part-00020-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.4MB,2024-12-02
Turkey,122111230,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111230/part-00070-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,4.0MB,2024-12-02
Turkey,122111231,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111231/part-00019-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.7MB,2024-12-02
Turkey,122111232,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111232/part-00197-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.3MB,2024-12-02
Turkey,122111233,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111233/part-00094-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,288.8KB,2024-12-02
Turkey,122111300,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111300/part-00132-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.1MB,2024-12-02
Turkey,122111301,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111301/part-00070-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,9.5MB,2024-12-02
Turkey,122111302,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111302/part-00155-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.7MB,2024-12-02
Turkey,122111303,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111303/part-00192-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,996.5KB,2024-12-02
Turkey,122111310,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111310/part-00114-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.7MB,2024-12-02
Turkey,122111311,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111311/part-00133-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,169.2KB,2024-12-02
Turkey,122111312,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111312/part-00108-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.1MB,2024-12-02
Turkey,122111313,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111313/part-00038-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,150.6KB,2024-12-02
Turkey,122111320,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111320/part-00110-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.8MB,2024-12-02
Turkey,122111321,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111321/part-00071-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1012.7KB,2024-12-02
Turkey,122111322,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111322/part-00044-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,55.2KB,2024-12-02
Turkey,122111330,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111330/part-00123-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,2.3MB,2024-12-02
Turkey,122111331,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111331/part-00145-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.5MB,2024-12-02
Turkey,122111332,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111332/part-00018-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,109.7KB,2024-12-02
Turkey,122111333,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122111333/part-00182-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,406.8KB,2024-12-02
Turkey,122112000,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122112000/part-00082-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,3.8MB,2024-12-02
Turkey,122112010,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122112010/part-00143-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,456.0KB,2024-12-02
Turkey,122112011,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122112011/part-00002-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,19.9MB,2024-12-02
Turkey,122112013,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122112013/part-00008-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.1MB,2024-12-02
Turkey,122112100,https://minedbuildings.z5.web.core.windows.net/global-buildings/2024-11-26/global-buildings.geojsonl/RegionName=Turkey/quadkey=122112100/part-00177-e2ba5ad4-8096-4382-98c8-81b5beefe645.c000.csv.gz,1.8MB,2024-12-02
"""

# Quadkey'leri bulmak için düzenli ifade
quadkey_pattern = r"quadkey=(\d+)"
quadkeys = re.findall(quadkey_pattern, data)

# Sonuçları yazdırma
print("Bulunan Quadkeys:")
print(quadkeys)
print(f"Toplam Quadkey sayısı: {len(quadkeys)}")

# Ankara'nın sınırları - koordinatları güncelledim
ankara_bounds = {
    "west": 32.0,  # Batı sınırı
    "east": 34.0,  # Doğu sınırı
    "south": 39.0, # Güney sınırı
    "north": 41.0  # Kuzey sınırı
}

# Ankara sınırında olan quadkey'leri bulma
ankara_quadkeys = []
for qk in quadkeys:
    try:
        tile = mercantile.quadkey_to_tile(qk)
        bounds = mercantile.bounds(tile)
        
        # Tile'ın sınırları Ankara'nın sınırları ile kesişiyor mu kontrol et
        if (bounds.west <= ankara_bounds["east"] and 
            bounds.east >= ankara_bounds["west"] and 
            bounds.south <= ankara_bounds["north"] and 
            bounds.north >= ankara_bounds["south"]):
            ankara_quadkeys.append(qk)
            
    except Exception as e:
        print(f"Hata: {qk} quadkey'i işlenirken hata oluştu: {e}")

print("\nAnkara'ya ait Quadkeys:", ankara_quadkeys)
print(f"Ankara'da bulunan quadkey sayısı: {len(ankara_quadkeys)}")

# Debug için ilk birkaç quadkey'in koordinatlarını yazdır
print("\nÖrnek Quadkey Koordinatları:")
for qk in quadkeys[:3]:
    try:
        tile = mercantile.quadkey_to_tile(qk)
        bounds = mercantile.bounds(tile)
        print(f"\nQuadkey: {qk}")
        print(f"Batı: {bounds.west:.6f}")
        print(f"Doğu: {bounds.east:.6f}")
        print(f"Güney: {bounds.south:.6f}")
        print(f"Kuzey: {bounds.north:.6f}")
    except Exception as e:
        print(f"Hata: {qk} quadkey'i işlenirken hata oluştu: {e}")
