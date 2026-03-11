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
import subprocess
import sys

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Agregar headers CORS para desarrollo
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def start_api_server() -> subprocess.Popen:
    """Arranca el servidor FastAPI (uvicorn) en 127.0.0.1:8000 en un
proceso separado."""
    # usamos el intérprete actual para que se respete el entorno virtual
    cmd = [sys.executable, "-m", "uvicorn", "src.app.main:app", "--reload"]
    print("⚙️  Iniciando API FastAPI en http://127.0.0.1:8000 (uvicorn)")
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc


def run_server(port=8080, start_api: bool = True):
    """Ejecuta el servidor en el puerto especificado.

    Si *start_api* es True lanza también el proceso de la API.
    """

    # Cambiar al directorio del proyecto
    project_root = Path(__file__).parent
    os.chdir(project_root)

    api_proc = None
    if start_api:
        api_proc = start_api_server()

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
        finally:
            if api_proc:
                print("🛑 Deteniendo proceso de API")
                api_proc.terminate()
                api_proc.wait()

if __name__ == "__main__":
    run_server()