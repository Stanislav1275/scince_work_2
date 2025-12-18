from typing import Any, Dict

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import logging

from process import process, u_list

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="static/templates")
logger = logging.getLogger('uvicorn.error')


@app.get("/initial_equations")
async def get_initial_equations():
    return u_list


# Точка входа в приложение
@app.get("/")
async def main(
        request: Request,
        initial_equations=Depends(get_initial_equations)
):
    return templates.TemplateResponse(name="index.html", context={
        "request": request,
        "initial_equations": initial_equations,
        "faks": ["S", "F", "G", "T", "A", "D", "I", "P", "C"],
        "equations": [
            {"f": "F1", "param": "s"},
            {"f": "F1", "param": "x8"},
            {"f": "F2", "param": "s"},
            {"f": "F2", "param": "x8"},
            {"f": "F2", "param": "x1"},
            {"f": "F2", "param": "x7"},
            {"f": "F3", "param": "x8"},
            {"f": "F3", "param": "x1"},
            {"f": "F3", "param": "x7"},
            {"f": "F4", "param": "x8"},
            {"f": "F4", "param": "x7"},
            {"f": "F4", "param": "x1"},
            {"f": "F5", "param": "s"},
            {"f": "F5", "param": "x1"},
            {"f": "F5", "param": "x7"},
            {"f": "F6", "param": "s"},
            {"f": "F6", "param": "x8"},
            {"f": "F7", "param": "x1"},
            {"f": "F8", "param": "s"},
            {"f": "F8", "param": "x4"},
            {"f": "F9", "param": "s"},
            {"f": "F9", "param": "x1"},
            {"f": "F9", "param": "x7"},
            {"f": "F10", "param": "s"},
            {"f": "F10", "param": "x1"},
            {"f": "F10", "param": "x7"},
            {"f": "F11", "param": "s"},
            {"f": "F11", "param": "x6"},
            {"f": "F12", "param": "x11"}
        ]
    })


# Метод обработки введенных пользователем значений. Возвращает статус в виде строки. Если статус = "Выполнено",
# то на других страницах будут отображаться нарисованные графики. Пока этот метод не вызван, графики отображаться не должны
@app.post("/draw_graphics")
async def draw_graphics(body: Dict[Any, Any]):
    try:
        process(body["initial_equations"], body["faks"], body["equations"], body["restrictions"])
        return {"status": "Выполнено"}
    except Exception as e:
        logger.info(e)
        return {"status": "Ошибка"}


@app.get("/graphic")
async def get_graphic(request: Request):
    return templates.TemplateResponse(name="graphic.html", context={
        "request": request
    })


@app.get("/diagrams")
async def get_diagrams(request: Request):
    return templates.TemplateResponse(name="diagrams.html", context={
        "request": request
    })
