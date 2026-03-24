from fastapi import FastAPI
from routers import predict

app = FastAPI(title="Sentiment Analysis Prediction API")

app.include_router(predict.router)




