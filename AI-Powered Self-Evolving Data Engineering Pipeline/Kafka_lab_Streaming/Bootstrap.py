import time
import socket
import requests
import subprocess
import sys

CONNECT_URL = "http://connect:8083"
KAFKA_SERVER = "kafka:9092"
MYSQL_HOST = "mysql"
MYSQL_PORT = 3306


def wait_for_port(host, port):
    while True:
        try:
            socket.create_connection((host, port), timeout=5)
            print(f"{host}:{port} ready")
            return
        except Exception:
            print(f"Waiting for {host}:{port}...")
            time.sleep(5)


def wait_for_connect():
    while True:
        try:
            r = requests.get(f"{CONNECT_URL}/connectors")
            if r.status_code == 200:
                print("Kafka Connect ready")
                return
        except:
            pass
        print("Waiting for Kafka Connect...")
        time.sleep(5)


def register_connector():
    config = {
        "name": "mysql-connector",
        "config": {
            "connector.class": "io.debezium.connector.mysql.MySqlConnector",
            "database.hostname": "mysql",
            "database.port": "3306",
            "database.user": "root",
            "database.password": "root",
            "database.server.id": "184054",
            "topic.prefix": "dbserver1",
            "database.include.list": "testdb",
            "schema.history.internal.kafka.bootstrap.servers": KAFKA_SERVER,
            "schema.history.internal.kafka.topic": "schema-changes.testdb"
        }
    }

    existing = requests.get(f"{CONNECT_URL}/connectors").json()

    if "mysql-connector" not in existing:
        r = requests.post(f"{CONNECT_URL}/connectors", json=config)
        print("Connector registration:", r.status_code, r.text)
    else:
        print("Connector already registered")


def start_jupyter():
    subprocess.run([
        "jupyter", "lab",
        "--ip=0.0.0.0",
        "--port=8888",
        "--no-browser",
        "--allow-root",
        "--IdentityProvider.token=",
        "--IdentityProvider.password="
    ])


if __name__ == "__main__":
    wait_for_port(MYSQL_HOST, MYSQL_PORT)
    wait_for_port("kafka", 9092)
    wait_for_connect()
    register_connector()
    start_jupyter()