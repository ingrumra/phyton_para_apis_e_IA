import time
from serve_dashboard import start_api_server, run_server


def test_start_api_process():
    # el método debe devolver un objeto Popen que arranca uvicorn
    proc = start_api_server()
    try:
        assert proc.poll() is None  # sigue en ejecución
    finally:
        proc.terminate()
        proc.wait(timeout=5)


def test_run_server_api_flag(tmp_path, monkeypatch):
    # correr run_server con start_api=False no debe lanzar error
    # usamos un puerto temporal y no intentamos servir forever
    # monkeypatch la clase TCPServer para que no bloquee
    class Dummy:
        def __init__(self, *args, **kwargs):
            pass
        def __enter__(self):
            return self
        def __exit__(self, *args):
            return False
        def serve_forever(self):
            pass
        def shutdown(self):
            pass
    monkeypatch.setattr("serve_dashboard.socketserver.TCPServer", Dummy)
    # ejecutar sin API (por velocidad)
    run_server(port=8081, start_api=False)
