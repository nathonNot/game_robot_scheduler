from app.util.web_socket import ConnectionManager
ws_manager = ConnectionManager()

from app.db import database, engine, metadata
from fastapi import FastAPI
from app.util.logger import init_log

metadata.create_all(engine)

app = FastAPI()



@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

from app.api import notes, ping, jiuyin, api_user,hook,web_scoket,api_controller

app.include_router(ping.router)
app.include_router(web_scoket.router)
app.include_router(jiuyin.router, prefix="/api/jiuyin", tags=["jiuyin"])
app.include_router(api_user.router, prefix="/api/user", tags=["user"])
app.include_router(notes.router, prefix="/notes", tags=["notes"])
app.include_router(hook.router, prefix="/api/hook", tags=["hook"])
app.include_router(api_controller.router, prefix="/api/controller", tags=["controller"])


init_log()

