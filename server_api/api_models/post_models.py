from pydantic import BaseModel

# Definieren eines Pydantic-Modells, das die Struktur der Anfragedaten repräsentiert
class TextToSpeechInput(BaseModel):
    text_to_speech_inp: str
    voice: str or None
    
