from fastapi import FastAPI, BackgroundTasks
import os
from server_api.helper.create_zip import create_filename
from fastapi.responses import FileResponse
from server_api.helper.file_handler import remove_file

server_base_url = "http://127.0.0.1:8000"
app = FastAPI()
downloaded_files = []


async def resolve_tts_result(zip_file: str, background_tasks: BackgroundTasks):
    fpath = os.path.join(os.path.abspath("server_api/tts_results_zip"), zip_file)

    if not os.path.exists(fpath):
        return 401
    else:
        response = FileResponse(
            fpath, status_code=200, filename=create_filename(), media_type="audio/wav"
        )
        background_tasks.add_task(remove_file, fpath)
        return response
