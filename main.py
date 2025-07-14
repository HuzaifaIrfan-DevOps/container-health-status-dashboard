from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from python_on_whales import docker
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

def get_container_status():
    data = []
    for container in docker.ps(all=True):
        health = container.state.health.status if container.state.health else "none"
        started = container.state.started_at
        data.append({
            "name": container.name,
            "id": container.id[:12],
            "status": health,
            "started": started.strftime("%Y-%m-%d %H:%M:%S") if started else "N/A"
        })
    return data

@app.get("/", response_class=HTMLResponse)
async def status_page(request: Request):
    containers = get_container_status()
    return templates.TemplateResponse("status.html", {
        "request": request,
        "containers": containers
    })
