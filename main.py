from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://loomis-clicker-game-ljng.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

users_db = {}

@app.post("/api/user")
async def save_user(request: Request):
    data = await request.json()
    user_id = data.get("id")
    username = data.get("username")
    users_db[user_id] = {"username": username, "balance": 0}
    print(f"[LOG] Гравець: {username} ({user_id}) доданий.")
    return {"status": "saved"}
