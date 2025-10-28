# tests/test_integration_api.py
import subprocess
import time
import requests

SERVER_CMD = ["python", "app.py"]
SERVER_URL = "http://127.0.0.1:5000"


def start_server():
    # Start the flask dev server as child process
    proc = subprocess.Popen(
        SERVER_CMD,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # wait for health endpoint ready, with timeout
    try:
        for _ in range(20):
            try:
                r = requests.get(f"{SERVER_URL}/health", timeout=0.5)
                if r.status_code == 200:
                    return proc
            except Exception:
                time.sleep(0.2)
    except Exception:
        pass
    # If we get here, server didn't come up — kill and return None
    proc.kill()
    return None


def stop_server(proc):
    try:
        proc.terminate()
        proc.wait(timeout=3)
    except Exception:
        proc.kill()


def test_add_endpoint_get():
    proc = start_server()
    assert proc is not None, "Server failed to start"
    try:
        r = requests.get(f"{SERVER_URL}/add", params={"a": 2, "b": 3})
        assert r.status_code == 200
        assert r.json()["result"] == 5
    finally:
        stop_server(proc)


def test_add_endpoint_post():
    proc = start_server()
    assert proc is not None, "Server failed to start"
    try:
        r = requests.post(f"{SERVER_URL}/add", json={"a": 1.5, "b": 2.5})
        assert r.status_code == 200
        assert r.json()["result"] == 4.0
    finally:
        stop_server(proc)
