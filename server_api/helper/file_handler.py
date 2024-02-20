import os, shutil

def remove_file(file_path: str):
    """Hintergrundfunktion zum Löschen einer Datei."""
    if os.path.exists(file_path):
        os.remove(file_path)

def delete_directory(dir_path):
    # Überprüfen, ob das Verzeichnis existiert
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        try:
            # Löschen des Verzeichnisses und aller enthaltenen Dateien und Unterverzeichnisse
            shutil.rmtree(dir_path)
            # print(f"Das Verzeichnis {dir_path} wurde erfolgreich gelöscht.")
            return None
        except Exception as e:
            # Fehlermeldung, falls das Löschen fehlschlägt
            # print(f"Fehler beim Löschen des Verzeichnisses {dir_path}: {e}")
            return e
    else:
        # print(f"Das Verzeichnis {dir_path} existiert nicht oder ist kein Verzeichnis.")
        return None