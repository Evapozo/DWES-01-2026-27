import markdown
from weasyprint import HTML

# Leemos el archivo markdown unificado que ya creamos
with open("apuntes_completos_reales.md", "r", encoding="utf-8") as f:
    text_content = f.read()

# Convertimos el texto Markdown a HTML con soporte para tablas y bloques de código
html_content = markdown.markdown(text_content, extensions=['tables', 'fenced_code'])

# Diseñamos una plantilla HTML con estilos limpios y profesionales
styled_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; color: #333; }}
        h1, h2, h3 {{ color: #003366; page-break-after: avoid; }}
        pre {{ background-color: #f4f4f4; padding: 10px; border-radius: 5px; font-family: monospace; white-space: pre-wrap; }}
        code {{ background-color: #f4f4f4; padding: 2px 4px; border-radius: 3px; }}
        table {{ border-collapse: collapse; width: 100%; margin-bottom: 20px; page-break-inside: avoid; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        img {{ max-width: 100%; height: auto; }}
    </style>
</head>
<body>
    {html_content}
</body>
</html>
"""

# Generamos el PDF final
HTML(string=styled_html).write_pdf("apuntes_daw_completos.pdf")
print("¡PDF generado con éxito como 'apuntes_daw_completos.pdf'!")