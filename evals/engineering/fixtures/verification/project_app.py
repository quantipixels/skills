import argparse
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
from pathlib import Path
import sqlite3
import sys
from urllib.error import HTTPError
from urllib.parse import quote, unquote, urlparse
from urllib.request import Request, urlopen


class ItemHandler(BaseHTTPRequestHandler):
    database_path = None

    def log_message(self, _format, *_args):
        return

    def item_id(self):
        parsed = urlparse(self.path)
        prefix = "/items/"
        if not parsed.path.startswith(prefix):
            return None
        return unquote(parsed.path[len(prefix):])

    def send_json(self, status, value):
        body = json.dumps(value, sort_keys=True).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_PUT(self):
        item_id = self.item_id()
        if not item_id:
            self.send_json(404, {"error": "not found"})
            return
        length = int(self.headers.get("Content-Length", "0"))
        value = json.loads(self.rfile.read(length))
        with sqlite3.connect(self.database_path) as database:
            database.execute(
                "INSERT OR REPLACE INTO items(id, text) VALUES (?, ?)",
                (item_id, value["text"]),
            )
            database.execute(
                "INSERT INTO request_log(event, item_id) VALUES ('put', ?)",
                (item_id,),
            )
        self.send_json(200, {"id": item_id, "text": value["text"]})

    def do_GET(self):
        item_id = self.item_id()
        if os.environ.get("QP_FAIL_GET") == "1":
            with sqlite3.connect(self.database_path) as database:
                database.execute(
                    "INSERT INTO request_log(event, item_id) VALUES ('get_failed', ?)",
                    (item_id,),
                )
            self.send_json(503, {"error": "forced read failure"})
            return
        with sqlite3.connect(self.database_path) as database:
            row = database.execute("SELECT text FROM items WHERE id = ?", (item_id,)).fetchone()
            database.execute(
                "INSERT INTO request_log(event, item_id) VALUES ('get', ?)",
                (item_id,),
            )
        if row is None:
            self.send_json(404, {"error": "not found"})
        else:
            self.send_json(200, {"id": item_id, "text": row[0]})


def serve(args):
    database_path = Path(args.db).resolve()
    with sqlite3.connect(database_path) as database:
        database.execute("CREATE TABLE IF NOT EXISTS items (id TEXT PRIMARY KEY, text TEXT NOT NULL)")
        database.execute(
            "CREATE TABLE IF NOT EXISTS request_log ("
            "sequence INTEGER PRIMARY KEY AUTOINCREMENT, event TEXT NOT NULL, item_id TEXT NOT NULL)"
        )
    ItemHandler.database_path = database_path
    server = HTTPServer(("127.0.0.1", 0), ItemHandler)
    Path(args.port_file).write_text(str(server.server_port), encoding="utf-8")
    server.timeout = 10
    try:
        for _ in range(args.max_requests):
            server.handle_request()
    finally:
        server.server_close()


def request(args):
    url = f"{args.url.rstrip('/')}/items/{quote(args.id, safe='')}"
    data = None
    method = "GET"
    if args.command == "put":
        data = json.dumps({"text": args.text}).encode()
        method = "PUT"
    try:
        with urlopen(Request(url, data=data, method=method), timeout=5) as response:
            value = json.loads(response.read())
    except HTTPError as error:
        print(error.read().decode(), file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps(value, sort_keys=True))


def build_parser():
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    server = commands.add_parser("serve")
    server.add_argument("--db", required=True)
    server.add_argument("--port-file", required=True)
    server.add_argument("--max-requests", type=int, required=True)
    for name in ("put", "get"):
        command = commands.add_parser(name)
        command.add_argument("--url", required=True)
        command.add_argument("--id", required=True)
        if name == "put":
            command.add_argument("--text", required=True)
    return parser


def main():
    args = build_parser().parse_args()
    serve(args) if args.command == "serve" else request(args)


if __name__ == "__main__":
    main()
