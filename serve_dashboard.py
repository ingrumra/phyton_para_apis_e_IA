#!/usr/bin/env python3
"""
Servidor simple para servir el dashboard HTML localmente.
Esto soluciona el problema de CORS cuando se abre index.html directamente.

Uso:
    python serve_dashboard.py

Luego abre: http://localhost:8080
"""

import http.server
import socketserver
import os
from pathlib import Path

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers CORS para desarrollo
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def run_server(port=8080):
    """Ejecuta el servidor en el puerto especificado"""

    # Cambiar al directorio del proyecto
    project_root = Path(__file__).parent
    os.chdir(project_root)

    with socketserver.TCPServer(("", port), CustomHTTPRequestHandler) as httpd:
        print(f"🚀 Dashboard servido en: http://localhost:{port}")
        print(f"📊 API disponible en: http://localhost:8000")
        print(f"📖 Documentación API: http://localhost:8000/docs")
        print("\n💡 Para detener el servidor presiona Ctrl+C\n")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Servidor detenido")
            httpd.shutdown()

if __name__ == "__main__":
    run_server()