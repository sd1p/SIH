from fastapi import APIRouter, HTTPException

from pydantic import BaseModel


# router for prediction endpoint
router = APIRouter()


# using pydantic for type safety
class Payload(BaseModel):
    url: str


@router.post("/predict/")
async def predict(input_data: Payload):
    try:
        # features = input_data.features

        # prediction = model.predict([features])[0]
        prediction = "hey1"
        url = input_data.url

        return {"prediction": prediction, "url": url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
