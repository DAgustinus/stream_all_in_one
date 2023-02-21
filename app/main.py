from datetime import datetime, timedelta
from fastapi import FastAPI
from typing import Optional
from api_util import ApiGenerator

import time

gen = ApiGenerator()
app = FastAPI()   

@app.get("/")
async def get_data():
    return gen.get_data()
