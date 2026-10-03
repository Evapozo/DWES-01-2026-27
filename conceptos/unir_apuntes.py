import os

output_file = "apuntes_completos_reales.md"

# Abre el archivo de salida donde se guardará todo el contenido unificado
with open(output_file, "w", encoding="utf-8") as outfile:
    # Recorre de forma recursiva la carpeta actual y todas sus subcarpetas
    for root, dirs, files in os.walk("."):
        for file in sorted(files):
            # Filtra solo los archivos .md y evita incluir el propio archivo de salida si ya existe
            if file.endswith(".md") and file != output_file:
                file_path = os.path.join(root, file)
                
                # Escribe un encabezado indicando el origen de cada archivo
                outfile.write(f"\n\n--- \n# Archivo: {file} (Ruta: {root})\n---\n\n")
                
                # Lee el contenido del archivo markdown y lo escribe en el archivo final
                try:
                    with open(file_path, "r", encoding="utf-8") as infile:
                        outfile.write(infile.read())
                except Exception as e:
                    print(f"No se pudo leer el archivo {file}: {e}")

print("¡Proceso terminado con éxito!")