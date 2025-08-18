import requests
import base64
from auth import autentikasi

BASE_URL = "http://127.0.0.1:8000"  # UTP/IP
TOKEN = autentikasi()  # Valid token

def test_root():
    try:
        r = requests.get(f"{BASE_URL}/")
        print("Root:", r.status_code, r.json(), "uji berhasil")
    except Exception as e:
        print("Uji gagal", e)
def test_image_base64():
    try:
        with open("image_01.jpg", "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode("utf-8")

        payload = {"getImage": img_base64}
        r = requests.post(f"{BASE_URL}/image", json=payload)
        print("Image (base64):", r.status_code, r.json(), "uji berhasil" )
    except Exception as e:
        print("Uji gagal", e)
def test_image_file(): # pake token
    try:
        headers = {"Authorization": f"Bearer {TOKEN}"}
        files = {"file": open("image_02.jpg", "rb")}
        r = requests.post(f"{BASE_URL}/imgeOCR", headers=headers, files=files)
        print("Image (file upload):", r.status_code, r.json(), "uji berhasil")
    except Exception as e:
        print("uji gagal", e)

def test_translate():
    try:
        payload = {
            "source": "auto",
            "target": "en",
            "text": "Halo dunia",
            "proxies": []
        }
        r = requests.post(f"{BASE_URL}/translate", json=payload)
        print("Translate:", r.status_code, r.json(), "uji berhasil")
    except Exception as e:
        print("Uji gagal (translate)", e)
    
if __name__ == "__main__":
    test_root()
    test_image_base64()
    test_image_file()
    test_translate()
