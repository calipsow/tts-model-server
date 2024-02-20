import uvicorn
from .views import app  # Import the FastAPI app from views.py



def run_server_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)