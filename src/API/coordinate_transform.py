from pyproj import transform
from fastapi import responses
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=['*'], 
                    allow_credentials=True,
                    allow_methods=["*"], 
                    allow_headers=["*"])

@app.get("/")
async def basisverzeichnis():
    return {"status": "alles gut, es funktioniert"}

@app.get("/lv95towgs84")
async def lv95towgs84(easting, northing):
    return {"easting": transform(2056, 4326, float(easting), float(northing))[0], 
            'northing': transform(2056, 4326, float(easting), float(northing))[1]}

@app.get("/wgs84tolv95")
async def wgs84tolv95(easting, northing):
    return {"easting": transform(4326, 2056, float(easting), float(northing))[0],
            'northing': transform(4326, 2056, float(easting), float(northing))[1]}