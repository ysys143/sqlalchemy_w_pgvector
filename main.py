from fastapi import FastAPI
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
import models
from database import engine 
from service import router
import uvicorn

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "건설산업정보원 챗봇 서버 입니다."}

@app.get("/favicon.ico")
async def favicon():
    return Response(content="", media_type="image/x-icon")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
