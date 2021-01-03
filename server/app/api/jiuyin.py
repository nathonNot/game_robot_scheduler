from fastapi import APIRouter
from app.util.rsa import return_respons
import json

router = APIRouter()

@router.get("/get_version")
async def get_version():
    data = {
        "version":"0.0.1.5",
        "end_time":20210104,
        "download_url":"https://fuakorm.com/download/dist.zip",
        "version_log":"更新日志：\n 1.测试优化"
        }
    return data

