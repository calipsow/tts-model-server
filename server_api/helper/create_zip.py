import zipfile, os, datetime


def create_zip(zip_name, files):
    print("creating zip archive")
    with zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
        for file in files:
            if not os.path.exists(file):
                print(file, "not exists")
                continue

            file_name = os.path.basename(file)
            zipf.write(file, arcname=file_name)

    print("zip archive created")


def create_filename():
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    # String mit Präfix und aktueller Uhrzeit zusammenstellen
    filename = f"text-to-speech-{timestamp}_.zip"

    return filename
