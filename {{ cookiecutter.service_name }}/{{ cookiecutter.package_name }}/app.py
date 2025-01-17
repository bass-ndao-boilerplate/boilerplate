import os
from fastapi import FastAPI
from fastapi import Path
from fastapi.responses import RedirectResponse
from http import HTTPStatus
import json
from pydantic import BaseModel

import config

app = FastAPI(
    title="app",
    description="",
    version="1.0.0",
)


@utils.construct_response
@app.get("/")
async def _index():
    response = {
        'message': HTTPStatus.OK.phrase,
        'status-code': HTTPStatus.OK,
        'data': {}
    }
    config.logger.info(json.dumps(response, indent=2))
    return response


@utils.construct_response
@app.get("/experiments")
async def _experiments():
    pass


@utils.construct_response
@app.get("/experiment/details/{experiment_id}")
async def _experiment_details(experiment_id: str = Path(default='latest', title="ID of experiment")):
    pass


@app.get("/tensorboard")
async def _tensorboard():
    """Ensure TensorBoard is running on port 6006
    via `tensorboard --logdir tensorboard`."""
    return RedirectResponse("http://localhost:6006/")


class PredictPayload(BaseModel):
    pass


@utils.construct_response
@app.post("/predict")
async def _predict(payload: PredictPayload):
    pass
