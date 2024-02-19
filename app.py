from fastapi import FastAPI
import datetime

from starlette.templating import Jinja2Templates

from Message import MessageState

app = FastAPI()
Message = MessageState("", 1, str(datetime.datetime.now()),20)


from fastapi import Request


@app.get("/send/{mes}")
async def send_message(mes: str):
    message = mes.replace("_", " ")
    # zebranie danych z requesta
    Message.message = message
    Message.time = str(datetime.datetime.now())
    Message.power = 1

    return {"message": "wyslano"}


@app.get("/get")
async def display():
    context = {
        "message": Message.message,
        "time": Message.time,
        "power": Message.power,
        "distance": Message.distance
    }

    return context


@app.get("/distance")
async def display_distance():
    context = {
        "message": Message.distance
    }

    return context

@app.get("/setdistance/{dsc}")
async def display_distance(dsc:int):
    Message.distance = dsc

    return {"message": "ustawiono"}
@app.get("/emoi")
async def display_emoi():
    context = {
        "message": Message.power
    }

    return context

@app.get("/setemoi/{emi}")
async def display_emoi(emi: int):
    Message.power = emi

    return {"message": "ustawiono"}
