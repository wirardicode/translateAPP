from PIL import Image
import pytesseract
import numpy as np
import cv2
from fastapi import FastAPI, Header, File, UploadFile, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import base64
from auth import autentikasi
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import requests
import os
from dotenv import load_dotenv

security = HTTPBearer()
app = FastAPI()

load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#filename = 'image_02.jpg'
#
#img1 = np.array(Image.open(filename))
#text = pytesseract.image_to_string(img1)
#
#print(text)

class image(BaseModel):
    getImage: str

VALID_TOKEN = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

VALID_TOKEN = autentikasi()
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != VALID_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
    return credentials.credentials
@app.get('/')
def root():
    return {'code': 200, 'message':'berhasil'}

@app.post("/image") # base 64str untuk js atau app mobile mengirim JSON string, tidak perlu multipart upload.
def read_ocr(data: image):
    # Decode base64
    image_data = base64.b64decode(data.getImage)
    np_img = np.frombuffer(image_data, np.uint8)
    img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    # Preprocessing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.medianBlur(gray, 3)
    _, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((1, 1), np.uint8)
    clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # OCR
    text = pytesseract.image_to_string(clean)
    return {"text": text}

@app.post('/imgeOCR')
async def readOcr(file: UploadFile = File(...), token: str = Depends(verify_token)):
    # Baca file langsung ke numpy array
    file_bytes = np.frombuffer(await file.read(), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    # Preprocessing
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    denoised = cv2.medianBlur(gray, 3)
    _, thresh = cv2.threshold(denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((1, 1), np.uint8)
    clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # OCR
    text = pytesseract.image_to_string(clean)
    return {'code':200, 'message': text}

    ##########################################
  #fect api translator biar gak kena block dari server forum redit (azure cloude nya) || DIPINDAH KE ENV
@app.post("/translate")
def translate(payload: dict):
    try:
        response = requests.post(API_URL, json=payload)
        return response.json()
    except Exception as e:
        return {"error": str(e)}