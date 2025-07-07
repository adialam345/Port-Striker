# Port-Striker
# ⚔️ Multi-Port DDoS Striker

---

## 🧾 Deskripsi

`Multi-Port DDoS Striker` adalah script Python sederhana untuk melakukan _stress testing_ pada port TCP sebuah server. Script ini menggunakan multi-threading untuk mengirimkan sejumlah besar data acak ke alamat IP dan port tertentu.

---

## 🛠️ Fitur

- Pengiriman data ke port TCP tertentu
- Multi-threading hingga 1000 thread
- Menampilkan status pengiriman setiap thread
- Dapat digunakan untuk pengujian performa jaringan/server

---

## 📦 Ketergantungan

- Python 3.x
- Modul bawaan:
  - `socket`
  - `random`
  - `time`
  - `os`
  - `threading`
  - `datetime`
  - `concurrent.futures`

---

## 🚀 Cara Menggunakan

1. Buka terminal.
2. Jalankan script dengan Python:

```bash
python3 main.py
