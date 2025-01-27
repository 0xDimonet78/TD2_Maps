import re
import json

# Leer el contenido del archivo Spain Locations.md con codificación utf-8
with open('Spain Locations.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Expresión regular mejorada para extraer nombres y coordenadas
# Maneja posibles espacios adicionales o líneas vacías entre las entradas
locations = re.findall(r'## (.+?)\n(?:.+?\n)?\n(.+?)\n(.+?)\n', content)

if not locations:
    print("No se encontraron ubicaciones. Verifica el formato del archivo Spain Locations.md.")
else:
    # Crear una lista de diccionarios para las ubicaciones
    locations_list = [{"name": name, "lat": float(lat), "lng": float(lon)} for name, lat, lon in locations]

    # Guardar la lista en formato JSON en locations.json
    with open('locations.json', 'w', encoding='utf-8') as file:
        json.dump(locations_list, file, ensure_ascii=False, indent=2)

    print("locations.json ha sido generado con éxito.")
