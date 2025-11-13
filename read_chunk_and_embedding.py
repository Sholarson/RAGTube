import requests
import json
import os
import pandas as pd
import joblib

def vector_embedding(text_array):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_array
    })
    embedding = r.json()["embeddings"]
    return embedding

def main():
    json_files = os.listdir("jsons")
    json_files = sorted(json_files)

    chunk_id = 0
    my_dicts = []

    for file in json_files:
        with open(f"jsons/{file}") as f:
            chunks = json.load(f)

        try:
            print(90*"=")
            print(f"Creating Embeddings for {file}")
            embeddings = vector_embedding([c['text'] for c in chunks["chunks"]])


            for i, chunk in enumerate(chunks["chunks"]):
                chunk['chunk_id'] = chunk_id
                chunk['embedding'] = embeddings[i]
                my_dicts.append(chunk)
                chunk_id += 1

            print("\n")
        except Exception as e:
            print("Error occured:", e)
        

    # vector data in our pandas database
    df = pd.DataFrame.from_records(my_dicts)
    print(90*"=")
    print(df)

    # Saving the dataframe
    joblib.dump(df, "vector_embeddings.joblib")
    print("Dataframe Successfully Dumped")

if __name__ == "__main__":
    main()