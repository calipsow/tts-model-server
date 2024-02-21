from fastapi import FastAPI
from server_api.api_models.post_models import TextToSpeechInput


async def txt_file_based_tts(tts_input: TextToSpeechInput):
    return 200


def initialize_advanced_server_routes(app: FastAPI):
    app.post('/a')(txt_file_based_tts)

__all__ = ['initialize_advanced_server_routes']