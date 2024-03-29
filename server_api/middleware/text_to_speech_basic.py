import subprocess, os
from server_api.helper.get_directory_files import list_files
from server_api.helper.create_zip import create_zip
from fastapi.responses import JSONResponse
from server_api.api_models.post_models import TextToSpeechInput
from server_api.helper.gen_random_hex import generate_hex_string
from server_api.helper.file_handler import delete_directory

server_base_url = "http://127.0.0.1:8000"
downloaded_files = []


async def text_to_speech(textToSpeechInput: TextToSpeechInput):
    print("running tts", textToSpeechInput.text_to_speech_inp)
    txt = textToSpeechInput.text_to_speech_inp
    voice = textToSpeechInput.voice or "random"
    try:
        output_dir = os.path.abspath(f"results/{generate_hex_string(128)}")
        os.makedirs(output_dir, exist_ok=True)
        # Define the command you want to execute
        command = [
            "python",
            "tortoise/do_tts.py",
            "--text",
            f"{txt if txt else 'I am going to speak this'}",
            "--voice",
            f"{voice}",
            "--preset",
            "fast",
            "--output_path",
            f"{output_dir}",
        ]

        # Use subprocess.run to execute the command
        result = subprocess.run(command, capture_output=True, text=True)

        # Check if the command was successful
        if result.returncode == 0:
            files = list_files(output_dir)
            fname = f"{generate_hex_string(128)}.zip"
            zip_file = f"./server_api/tts_results_zip/{fname}"

            create_zip(zip_file, files)
            error = delete_directory(output_dir)
            if error:
                print(f"could not delete output dir {error}")

            return JSONResponse(
                {
                    "download": f"{server_base_url}/api/tts-results/zip/{fname}",
                    "error": "",
                },
                status_code=200,
            )
        else:
            if os.path.exists(output_dir):
                delete_directory(output_dir)
            print("Error:", result.stderr)
            return JSONResponse(
                {"error": result.stderr, "download": ""}, status_code=500
            )

    except Exception as e:
        print(f"failed to process tts req {e}")
        return JSONResponse(
            {"error": "failed to process tts req", "download": ""}, status_code=500
        )
