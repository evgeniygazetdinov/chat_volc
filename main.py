from fastapi import FastAPI

app = FastAPI()

from chat_volc.routers.chats import router as private_chat_router
from chat_volc.routers.users import router as users_router
from chat_volc.routers.messages import router as message_router

app.include_router(private_chat_router)
app.include_router(users_router)
app.include_router(message_router)


@app.get("/healf_check")
async def healf_check():
    return {"message": "alive"}



if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8010, reload=True)
