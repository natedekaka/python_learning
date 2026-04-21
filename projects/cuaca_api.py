#!/usr/bin/env python3
"""
Weather API Sederhana
belajar fetch data dari Open-Meteo API (gratis, tanpa API key)

Open-Meteo: https://open-meteo.com/
Dokumentasi: https://open-meteo.com/en/docs
"""

import requests
from datetime import datetime

URL = "https://api.open-meteo.com/v1/forecast"

KOTA = {
    "jakarta": {"name": "Jakarta", "lat": -6.2088, "lon": 106.8456},
    "bandung": {"name": "Bandung", "lat": -6.9175, "lon": 107.6191},
    "surabaya": {"name": "Surabaya", "lat": -7.2575, "lon": 112.7521},
    "yogyakarta": {"name": "Yogyakarta", "lat": -7.7956, "lon": 110.3695},
    "cimahi": {"name": "Cimahi", "lat": -6.8719, "lon": 107.5617},
}

CUACA = {
    0: "Cerah",
    1: "Umum",
    2: "Berkembang",
    3: "Mendung",
    45: "Kabut",
    48: "Kabut",
    51: "Gerimis Ringan",
    53: "Gerimis Sedang",
    55: "Gerimis Lebat",
    61: "Hujan Ringan",
    63: "Hujan Sedang",
    65: "Hujan Lebat",
    71: "Salju Ringan",
    73: "Salju Sedang",
    75: "Salju Lebat",
    80: "Hujan Lokal Ringan",
    81: "Hujan Lokal Sedang",
    82: "Hujan Lokal Lebat",
    95: "Badai",
    96: "Badai + Halus",
    99: "Badai + Kasar",
}


def ambil_cuaca(kota: str, hari: int = 1) -> dict:
    """Ambil data cuaca dari API"""
    if kota.lower() not in KOTA:
        raise ValueError(f"Kota tidak dikenal: {kota}. Pilih: {', '.join(KOTA.keys())}")

    data = KOTA[kota.lower()]
    params = {
        "latitude": data["lat"],
        "longitude": data["lon"],
        "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Asia/Jakarta",
        "forecast_days": hari,
    }

    try:
        resp = requests.get(URL, params=params, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Gagal mengambil data: {e}")


def tampilkan_cuaca(kota: str, hari: int = 1):
    """Tampilkan cuaca sesuai kota"""
    data = ambil_cuaca(kota, hari)
    lokasi = KOTA[kota.lower()]["name"]

    print(f"\n{'=' * 50}")
    print(f"  CUACA {lokasi.upper()}")
    print(f"{'=' * 50}")
    print(f"Diperbarui: {datetime.now().strftime('%d-%m-%Y %H:%M')}")

    current = data.get("current", {})
    print(f"\n📍 Sekarang:")
    print(f"   Suhu: {current.get('temperature_2m', 'N/A')}°C")
    print(f"   Kelembaban: {current.get('relative_humidity_2m', 'N/A')}%")
    kode = current.get("weather_code", 0)
    print(f"   Cuaca: {CUACA.get(kode, 'Tidak dikenal')} ({kode})")
    print(f"   Angin: {current.get('wind_speed_10m', 'N/A')} km/j")

    daily = data.get("daily", {})
    if daily.get("time"):
        print(f"\n📅 Ramalan {hari} hari ke depan:")
        for i, tgl in enumerate(daily["time"]):
            tgl_obj = datetime.strptime(tgl, "%Y-%m-%d")
            tgl_indo = tgl_obj.strftime("%d %b")
            max_suhu = daily["temperature_2m_max"][i]
            min_suhu = daily["temperature_2m_min"][i]
            hujan = daily["precipitation_sum"][i]

            print(f"   {tgl_indo}: {min_suhu}° - {max_suhu}°C | Hujan: {hujan}mm")

    print(f"{'=' * 50}\n")


def tampilkan_semua_kota():
    """Tampilkan cuaca semua kota"""
    print("\n📊 Cuaca Seluruh Kota Indonesia")
    print("=" * 60)

    for nama, data in KOTA.items():
        try:
            resp = requests.get(
                URL,
                params={
                    "latitude": data["lat"],
                    "longitude": data["lon"],
                    "current": "temperature_2m,weather_code",
                    "timezone": "Asia/Jakarta",
                },
                timeout=5,
            )
            resp.raise_for_status()
            curr = resp.json()["current"]
            kode = curr["weather_code"]
            print(
                f"{data['name']:<12}: {curr['temperature_2m']:>5}°C | {CUACA.get(kode, '?')}"
            )
        except Exception:
            print(f"{data['name']:<12}: Error")

    print("=" * 60)


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("""
╔══════════════════════════════════════════════════════════════╗
║            APLIKASI CUACA SEDERHANA                          ║
╠══════════════════════════════════════════════════════════════╣
║  Usage:                                                     ║
║    python cuaca_api.py <kota> [hari]                         ║
║    python cuaca_api.py all                                  ║
║                                                              ║
║  Contoh:                                                   ║
║    python cuaca_api.py jakarta                               ║
║    python cuaca_api.py bandung 3                           ║
║    python cuaca_api.py all                                ║
║                                                              ║
║  Kota tersedia:                                             ║
║    jakarta, bandung, surabaya, yogyakarta, cimahi           ║
╚══════════════════════════════════════════════════════════════╝
""")
        sys.exit(1)

    cmd = sys.argv[1].lower()

    if cmd == "all":
        tampilkan_semua_kota()
    else:
        hari = int(sys.argv[2]) if len(sys.argv) > 2 else 1
        try:
            tampilkan_cuaca(cmd, hari)
        except (ValueError, RuntimeError) as e:
            print(f"Error: {e}")
            sys.exit(1)
