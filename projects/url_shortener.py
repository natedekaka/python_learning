#!/usr/bin/env python3
"""
URL Shortener Sederhana
Belajar: Flask routing, database SQLite, redirect, session

Install: pip install flask
Run: python url_shortener.py
Access: http://localhost:5000
"""

from flask import (
    Flask,
    render_template_string,
    request,
    redirect,
    url_for,
    flash,
    make_response,
)
import sqlite3
import random
import string
from datetime import datetime

app = Flask(__name__)
app.secret_key = "rahasia123"
DB = "url_shortener.db"


def init_db():
    """Buat tabel database"""
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            short_code TEXT UNIQUE NOT NULL,
            original_url TEXT NOT NULL,
            description TEXT,
            clicks INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def generate_code(length=6):
    """Buat kode acak untuk short URL"""
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))


HTML = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>URL Shortener</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 min-h-screen">
    <div class="max-w-2xl mx-auto py-12 px-4">
        <div class="text-center mb-8">
            <h1 class="text-4xl font-bold text-blue-600">
                <i class="fas fa-link"></i> URL Shortener
            </h1>
            <p class="text-gray-600 mt-2">Pendekkan URL panjang kamu免费的!</p>
        </div>

        {% with messages = get_flashed_messages() %}
        {% if messages %}
        {% for msg in messages %}
        <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded mb-4">
            {{ msg }}
        </div>
        {% endfor %}
        {% endif %}
        {% endwith %}

        <div class="bg-white rounded-xl shadow-lg p-6 mb-8">
            <form method="POST" class="space-y-4">
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">
                        URL Asli (panjang)
                    </label>
                    <input type="url" name="url" required placeholder="https://contoh.com/page/yang/panjang/banget"
                        class="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none">
                </div>
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">
                        Deskripsi (opsional)
                    </label>
                    <input type="text" name="description" placeholder=" Contoh: Link YouTube"
                        class="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none">
                </div>
                <button type="submit" class="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 font-medium">
                    <i class="fas fa-scissors mr-1"></i> Pendekkan!
                </button>
            </form>
        </div>

        <div class="bg-white rounded-xl shadow-lg p-6">
            <h2 class="text-xl font-bold text-gray-800 mb-4">Daftar URL</h2>
            {% if urls %}
            <div class="overflow-x-auto">
                <table class="w-full text-sm">
                    <thead>
                        <tr class="border-b">
                            <th class="text-left py-2">Short URL</th>
                            <th class="text-left py-2">Asli</th>
                            <th class="text-center py-2">Klik</th>
                            <th class="text-center py-2">aksi</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for url in urls %}
                        <tr class="border-b hover:bg-gray-50">
                            <td class="py-2">
                                <a href="/{{ url.short_code }}" target="_blank" 
                                   class="text-blue-600 hover:underline font-mono">
                                    /{{ url.short_code }}
                                </a>
                            </td>
                            <td class="py-2 truncate max-w-xs" title="{{ url.original_url }}">
                                {{ url.description or url.original_url[:30] }}...
                            </td>
                            <td class="py-2 text-center">{{ url.clicks }}</td>
                            <td class="py-2 text-center">
                                <button onclick="copyToClipboard('{{ request.host_url }}{{ url.short_code }}')"
                                        class="text-gray-500 hover:text-blue-600">
                                    <i class="fas fa-copy"></i>
                                </button>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
            {% else %}
            <p class="text-gray-500 text-center py-4">Belum ada URL yang pendekkan.</p>
            {% endif %}
        </div>
        
        <div class="text-center mt-8 text-gray-500 text-sm">
            Total: {{ total }} URL | {{ total_clicks }} klik
        </div>
    </div>

    <script>
        function copyToClipboard(text) {
            navigator.clipboard.writeText(text).then(() => {
                alert('Copied: ' + text);
            });
        }
    </script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</body>
</html>"""


@app.route("/", methods=["GET", "POST"])
def index():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row

    if request.method == "POST":
        original_url = request.form["url"]
        description = request.form.get("description", "")

        short_code = generate_code()
        while True:
            check = conn.execute(
                "SELECT id FROM urls WHERE short_code = ?", (short_code,)
            ).fetchone()
            if not check:
                break
            short_code = generate_code()

        conn.execute(
            "INSERT INTO urls (short_code, original_url, description) VALUES (?, ?, ?)",
            (short_code, original_url, description),
        )
        conn.commit()
        flash(
            f'URL berhasil dibuat! → <a href="/{short_code}" class="text-blue-600 underline">/{short_code}</a>'
        )

    urls = conn.execute("SELECT * FROM urls ORDER BY created_at DESC").fetchall()
    total = conn.execute("SELECT COUNT(*) FROM urls").fetchone()[0]
    total_clicks = conn.execute("SELECT SUM(clicks) FROM urls").fetchone()[0] or 0
    conn.close()

    return render_template_string(
        HTML, urls=urls, total=total, total_clicks=total_clicks
    )


@app.route("/<short_code>")
def redirect_to_url(short_code):
    conn = sqlite3.connect(DB)
    url = conn.execute(
        "SELECT original_url, clicks FROM urls WHERE short_code = ?", (short_code,)
    ).fetchone()

    if url:
        conn.execute(
            "UPDATE urls SET clicks = clicks + 1 WHERE short_code = ?", (short_code,)
        )
        conn.commit()
        conn.close()
        return redirect(url["original_url"])

    conn.close()
    return f"<h1>404 - URL tidak ditemukan</h1><p>Kode: {short_code}</p>", 404


@app.route("/api/stats")
def stats():
    """API endpoint untuk stats"""
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    urls = conn.execute("SELECT * FROM urls ORDER BY clicks DESC LIMIT 10").fetchall()
    conn.close()

    result = []
    for url in urls:
        result.append(
            {
                "short_code": url["short_code"],
                "original_url": url["original_url"],
                "clicks": url["clicks"],
                "created_at": url["created_at"],
            }
        )
    return {"success": True, "data": result}


if __name__ == "__main__":
    init_db()
    print("""
╔═══════════════════════════════════════════════════════════╗
║              URL Shortener v1.0                         ║
╠═══════════════════════════════════════════════════════════╣
║  Start: http://localhost:5000                            ║
║  Stats: http://localhost:5000/api/stats                     ║
║  Demo:                                                  ║
║    python url_shortener.py                              ║
╚═══════════════════════════════════════════════════════════╝
""")
    app.run(debug=True, port=5000)
