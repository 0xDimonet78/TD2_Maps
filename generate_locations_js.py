import re

# Leer el contenido del archivo Spain Locations.md
with open('Spain Locations.md', 'r') as file:
    content = file.read()

# Extraer nombres y coordenadas usando expresiones regulares
locations = re.findall(r'## (.+?)\n\n.+?\n\n(.+?)\n(.+?)\n', content)

# Generar el contenido de locations.js
js_content = 'const locations = [\n'
for name, lat, lon in locations:
    js_content += f'  {{ name: "{name}", coords: [{lat}, {lon}] }},\n'
js_content += '];\n'

# Guardar el contenido en locations.js
with open('locations.js', 'w') as file:
    file.write(js_content)

print("locations.js ha sido generado con éxito.")
