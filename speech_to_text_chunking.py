import whisper
import json
import os

print("Loading Model...")
model = whisper.load_model("large-v2")
print("Model loaded successfully.")

audios = os.listdir("audio")

os.makedirs("jsons", exist_ok=True)

for audio in audios:
    if ("_" in audio):
        chunks = []
        video_number = audio.split("_")[0]
        title = audio.split("_")[1:]
        title = ",".join(title)[:-4]
        try:
                print(f"Transcribing audio: {audio} to text...")
                # Select the language from here "https://github.com/openai/whisper/blob/main/whisper/tokenizer.py" like {language = 'hi'} for hindi
                # result = model.transcribe(audio=f"audio/{audio}", language='{speech language}', task='translate', word_timestamps=False)
                result = model.transcribe(audio=f"audio/{audio}", task='translate', word_timestamps=False)
                print(f"Audio to text transcribe successfully.")
                for segment in result["segments"]:
                        chunks.append({"video_number": video_number, "title": title,"start": segment["start"], "end": segment["end"], "text": segment["text"]})

                chunks_with_metadata = {"chunks":chunks, "text": result["text"]}

                print(f"Saving the text on json1 as {audio[:-4]}.json")
                with open(f"jsons/{audio[:-4]}.json", "w") as f:
                        json.dump(chunks_with_metadata, f)
                print(120*"=")
        except Exception as e:
              print("Error occured:", e)



