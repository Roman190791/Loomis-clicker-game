from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Дозволити запити з гри
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://loomis-clicker-game-ljng.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/save-user")
async def save_user(request: Request):
    data = await request.json()
    telegram_id = data.get("telegram_id")
    username = data.get("username")
    print(f"Новий гравець: {telegram_id}, {username}")
    return {"status": "saved"}
