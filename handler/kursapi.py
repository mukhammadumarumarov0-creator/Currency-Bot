import httpx
import asyncio

async def get_valuta(valuta):
    valuta=f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/{valuta}/"
    async with httpx.AsyncClient() as client:
      resp=await client.get(valuta)
      return resp.json()

