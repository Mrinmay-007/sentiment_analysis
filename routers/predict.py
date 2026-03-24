from fastapi import APIRouter, HTTPException
from schemas.predict_schema import PredictRequest, PredictResponse
from services.model_loader import predict_sentiment

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)

@router.post("/", response_model=PredictResponse)
def predict(data: PredictRequest):
    try:
        prediction = predict_sentiment(data.text)
        return {"prediction": prediction}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))