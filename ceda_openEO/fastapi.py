from fastapi import FastAPI
import requests
import httpx

from ceda_openEO.utils import (
    ROOT, WELLKNOWN,
    ACCEPTED_COLLECTIONS
)

app = FastAPI()

@app.get('/')
async def root():
    return ROOT

@app.get('/.well-known/openeo')
async def wellknown():
    return WELLKNOWN

@app.get('/v1.0')
async def version():
    return ROOT

@app.get('/collections')
async def collections():
    req = requests.get('https://api.stac.ceda.ac.uk/collections/')

    # Filter Accepted Collections
    collections = req.json()
    openeo_collections = []
    for coll in collections['collections']:
        if coll['id'] in ACCEPTED_COLLECTIONS:
            openeo_collections.append(coll)

    collections['collections'] = openeo_collections

    return collections