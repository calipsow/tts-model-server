import random


def generate_hex_string(bits: int = 32):
    # Generieren einer zufälligen Zahl im Bereich von 0 bis 2^32 - 1
    random_number = random.getrandbits(bits)
    # Umwandlung der Zahl in einen Hex-String und Entfernen des "0x"-Präfixes
    hex_string = hex(random_number)[2:]
    # Rückgabe des Hex-Strings
    return hex_string
