![image](github-header-banner.png)

![Logo Bahasa](https://img.shields.io/badge/Python-Py-orange)
![Logo Bahasa](https://img.shields.io/badge/FastAPI-Fa-green)
![Logo Bahasa](https://img.shields.io/badge/JavaScript-Js-blue)

Aplikasi **OCR Translator** berbasis Python dan FastAPI yang mampu mendeteksi teks dari gambar dan menerjemahkannya secara otomatis ke 3 bahasa: Inggris, Indonesia, dan Jepang.  

Detail:
1. versi terbaru: Ver-2.1.0 Alpha
2. Update detail: 
- Bug solving
- Penyesuaian environtment
3. Pengembang: `Wirardi Syahputra || The god0100`

---

## Daftar Isi

1. [Tentang Aplikasi](#Tentang-Aplikasi)
2. [Fitur](#Fitur)
3. [Informasi API](#🛠️-Informasi-API)
4. [Instalasi](#instalasi)
   - [Manual](#manual)
   - [Docker](#docker)
5. [Menjalankan Frontend](#menjalankan-frontend)
6. [Kontribusi](#kontribusi)

---

# Tentang Aplikasi

OCR Translator dirancang untuk memudahkan penerjemahan teks dari gambar secara cepat dan akurat. Aplikasi ini dapat digunakan untuk dokumen, gambar, atau teks apapun yang ingin diterjemahkan ke tiga bahasa secara otomatis.  
Backend dibangun menggunakan **FastAPI** untuk performa API yang cepat, sementara frontend menggunakan **HTML**, **CSS**, dan **JavaScript**. Untuk fornt menggunakan [GOOGLE FONT](https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap)

---

## Fitur

- Pengenalan teks (OCR) dari gambar.  
- Terjemahan otomatis ke tiga bahasa: Inggris, Indonesia, Jepang.  
- REST API yang ringan dan mudah digunakan.  
- Frontend responsif dan mudah diintegrasikan.  

---

## Informasi API
1. buat file baru dengan nama `.env`
- linux:
```bash
  cd backend
  mkdir .env
```
- windows
```
  cd backend
  md .env
```
Untuk latest version 2.1.0 cukup rename file `.env.example` menjadi `.env`

2. isi `.env` dengan kode ini:

```bash
API_TOKEN=hkbsafwoyusdhblb12hblflhb5
API_URL = https://deep-translator-api.azurewebsites.net/google/
OCR_PATH = <YOUR_PATH>
```

3. alternatif token (opsional)
ganti path API_TOKEN dengan:
```bash
VALID_TOKEN = autentikasi()
```
---

## Instalasi
1. clone repo:
```bash
git clone <URL_REPO>
cd backend
```
2. Buat virtual environment (opsional):
```bash
python -m venv venv
```
3. Aktifkan virtual environment (opsional):
- windows:
     ```bash
       venv\Scripts\activate
     ```
- Linux/MacOS:
  ```bash
    source venv/bin/activate
  ```
  
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. jalankan fastAPI:
```bash
fastapi dev main.py
```

Dengan docker
- 
1. build image
```bash
docker build --tag <NAMA_IMAGE> .
```
2. buat dan jalankan kontainer
```bash
docker run -d -p <PORT_LOCAL>:<PORT_DOCKER> --name <NAMA_CONTAINER> <NAMA_IMAGE>
```

---------------

## Menjalankan Frontend

Frontend dapat dijalankan menggunakan ekstensi **Live Server**:  
[VSCode Live Server++](https://github.com/ritwickdey/vscode-live-server-plus-plus)  

Atau menggunakan npm:  
```bash
npm install
npm run dev
```
