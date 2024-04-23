from fastapi import FastAPI, UploadFile, Form
from fastapi.responses import FileResponse
from app.textart.text_art import create_image_from_text

app = FastAPI()

@app.get("/", response_class=FileResponse)
async def root():
    return FileResponse('index.html')

@app.post("/create-image-from-text/")
async def image_from_text_view(image: UploadFile = Form(...), word: str = Form(...)):
    image_stream = create_image_from_text(image, word)
    return FileResponse(image_stream, media_type='image/png', filename="text_image.png")
