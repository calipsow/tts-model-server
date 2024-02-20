from fastapi import FastAPI, BackgroundTasks
import subprocess, os, sys
from server_api.helper.get_directory_files import list_files
from server_api.helper.create_zip import create_zip
from fastapi.responses import FileResponse, JSONResponse
from server_api.api_models.post_models import TextToSpeechInput
from server_api.helper.gen_random_hex import generate_hex_string
from server_api.helper.file_handler import remove_file, delete_directory
server_base_url = "http://127.0.0.1:8000"
app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post('/tts/test')
async def text_to_speech(textToSpeechInput: TextToSpeechInput):
    print('running tts', textToSpeechInput.text_to_speech_inp)
    txt = textToSpeechInput.text_to_speech_inp
    voice = textToSpeechInput.voice or "random"
    try:
        output_dir = os.path.abspath(f'results/{generate_hex_string(128)}')
        os.makedirs(output_dir, exist_ok=True)
        # Define the command you want to execute
        command = ['python', 'tortoise/do_tts.py', '--text', f"{txt if txt else 'I am going to speak this'}", '--voice', f'{voice}', '--preset', 'fast', '--output_path', f'{output_dir}']

        # Use subprocess.run to execute the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            files = list_files(output_dir)
            zip_file = f"./server_api/tts_results_zip/{generate_hex_string(128)}.zip"
            
            create_zip(zip_file, files)
            error = delete_directory(output_dir)
            if error:
                print(f"could not delete output dir {error}")

            return JSONResponse({"download": f"{server_base_url}/api/tts-results/zip/{zip_file}", "error": ""}, status_code=200)
        else:
            if os.path.exists(output_dir): delete_directory(output_dir)
            print("Error:", result.stderr)
            return JSONResponse({'error':result.stderr, "download":""}, status_code=500)
        
    except Exception as e:
        print(f'failed to process tts req {e}')
        return JSONResponse({'error': "failed to process tts req", "download":""}, status_code=500)

@app.get("/api/tts-results/zip/{zip_file}")
async def read_item(zip_file: str, background_tasks: BackgroundTasks):
    fpath = os.path.join(os.path.abspath('server_api/tts_results_zip'), zip_file)
    if not os.path.exists(fpath):
        return 401
    else:
        background_tasks.add_task(remove_file, fpath)
        return FileResponse(fpath, status_code=200, filename=fpath.split('.')[-1], media_type="audio/wav")