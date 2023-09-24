from fastapi import APIRouter, HTTPException
import torch
from pydantic import BaseModel


# router for prediction endpoint
router = APIRouter()

model_path = "app/model/plant-disease-model-complete.pth"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.load(model_path, map_location=device)


class Payload(BaseModel):
    url: str


@router.post("/predict/")
async def predict(input_data: Payload):
    try:
        # features = input_data.features

        # prediction = model.predict([features])[0]
        prediction = "hey"
        url = input_data.url

        return {prediction, url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
