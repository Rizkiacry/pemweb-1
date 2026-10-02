import sqlite3
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs

DB = "pendaftaran.db"
WRITE_LOCK = threading.Lock()


class Handler(SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length).decode("utf-8", "replace")
        data = parse_qs(body, keep_blank_values=True)
        get = lambda k, d="": data.get(k, [d])[0]
        minat = ",".join(data.get("minat", []))
        try:
            nim_raw = get("nim", "").strip()
            nim = int(nim_raw) if nim_raw else None
            con = sqlite3.connect(DB)
            try:
                with WRITE_LOCK:
                    con.execute(
                        "INSERT INTO pendaftar (nama, pass, nim, tgl, jk, minat, prodi, alasan) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (get("nama"), get("pass"), nim, get("tgl"),
                         get("jk"), minat, get("prodi"), get("alasan")),
                    )
                    con.commit()
            finally:
                con.close()
            msg, status = "Data tersimpan.", 200
        except Exception as e:
            msg, status = f"Gagal simpan: {e}", 400
        raw = f"<p>{msg} <a href='/pendaftaran.html'>Kembali</a></p>".encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    ThreadingHTTPServer(("0.0.0.0", port), Handler).serve_forever()
