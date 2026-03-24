from fastapi import FastAPI
from routers import predict

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Sentiment Analysis Prediction API")




app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(predict.router)




