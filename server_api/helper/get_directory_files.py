import os

def list_files(directory):
    if not os.path.exists(directory):
        print('no path found', directory)
        return []
    
    file_paths = []  # Liste, um die vollständigen Pfade aller Dateien zu speichern
    for root, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)  # Erstellen des vollständigen Pfads zur Datei
            file_paths.append(full_path)  # Hinzufügen des vollständigen Pfads zur Liste

    return file_paths
