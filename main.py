from fastapi import FastAPI, Request
import uvicorn
from utils.logger import create_logger
import time
from api.v1.books import model
from database.connection import engine
from api.v1.books.app import router as books

logging = create_logger(__name__)

app = FastAPI(docs_url="/api/docs")
app.include_router(books,prefix="/books", tags=["Books"])

model.Base.metadata.create_all(bind=engine)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    logging.info(f"Incoming Request: {request.method} {request.url}")
    response = await call_next(request)
    if response.status_code != 200:
        logging.error(f"Status Code: {response.status_code}")
    process_time = (time.time() - start_time) * 1000
    logging.info(f"process_time: {process_time}")
    return response


@app.get("/health")
def endpoint_check_health_status():
    return {"success": True}


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000)
