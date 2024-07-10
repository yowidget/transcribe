import whisper

# Carga el modelo
model = whisper.load_model("small")

# Lista de names de archivos (sin extensión)
file_names = [
    "file1",
    "file2",
]


# Iterar a través de los names de archivos
for name in file_names:
    try:
        # Ruta del archivo de audio
        audio_file = f"./{name}.m4a"

        # Transcribir el audio
        result = model.transcribe(audio_file)

        # Ruta del archivo de salida
        output_file = f"{name}.txt"

        # Escribir el resultado en un archivo de texto
        with open(output_file, "w") as file:
            file.write(result["text"])

        print(f"Transcripción guardada en {output_file}")

    except Exception as e:
        print(f"No se pudo transcribir el archivo {audio_file}. Error: {e}")


