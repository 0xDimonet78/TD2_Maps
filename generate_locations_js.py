import re

# Leer el contenido del archivo Spain Locations.md con codificación utf-8
with open('Spain Locations.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Expresión regular mejorada para extraer nombres y coordenadas
# Maneja posibles espacios adicionales o líneas vacías entre las entradas
locations = re.findall(r'## (.+?)\n(?:.+?\n)?\n(.+?)\n(.+?)\n', content)

if not locations:
    print("No se encontraron ubicaciones. Verifica el formato del archivo Spain Locations.md.")
else:
    # Generar el contenido de locations.js
    js_content = 'const locations = [\n'
    for name, lat, lon in locations:
        js_content += f'  {{ name: "{name}", coords: [{lat}, {lon}] }},\n'
    js_content += '];\n'

    # Guardar el contenido en locations.js
    with open('Docs/locations.js', 'w', encoding='utf-8') as file:
        file.write(js_content)

    print("locations.js ha sido generado con éxito.")
