from importlib.resources import contents
from urllib import response
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app =  FastAPI()

@app.get("/" , response_class = HTMLResponse)
async def main():
    content = """
    <marquee width="525" behavior="alternate"><h1 style="color:red;font-family:Arial">Please Upload </h1></marquee>
    """
    return content