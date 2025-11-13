import numpy as np
from read_chunk_and_embedding import vector_embedding
import joblib
import requests
from sklearn.metrics.pairwise import cosine_similarity


def inference(prompt):
    r = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    })
    response = r.json()
    return response


# load the dataframe
df = joblib.load("vector_embeddings.joblib")

# Query from the user
incomming_query = input("Ask a Question: ")
question_embedding = vector_embedding([incomming_query])[0]


# Finding the cosine similarity between query_embedding and the chunk_embeddings
similarities = cosine_similarity(np.vstack(df["embedding"]), [question_embedding]).flatten()


top_result = 7
max_indx = similarities.argsort()[::-1][0:top_result]


new_df = df.loc[max_indx]

prompt = f"""
You are an AI assistant specialized in answering questions about the *Sigma Web Development Course*.

Below is a JSON object containing the **top 7 most relevant video chunks** retrieved using vector embeddings based on the user's query.

Each chunk includes:
- video_number: The video number in the course
- title: The title of the video
- start: The start time of the segment in seconds
- end: The end time of the segment in seconds
- text: The transcript text from that time range

Use this information to identify **which video**, **video number**, and **time range** best answer the user's question.

------------------------------
🔹 **Retrieved Chunks:**
{new_df[["video_number", "title", "start", "end", "text"]].to_json(orient="records")}

------------------------------
**User Query:**
"{incomming_query}"

------------------------------
**Your Task:**
1. Analyze the retrieved chunks and determine **where in the course** the topic or phrase mentioned in the query appears.  
2. Give a **concise and direct answer** containing:
   - Video title  
   - Video number  
   - Approximate time range (start–end in minutes)  
3. If multiple videos discuss the same topic, summarize them all clearly.  
4. If the retrieved text does **not** contain anything related to the query, respond with:
   > "I couldn’t find this topic in the retrieved videos. It might not be covered in the Sigma Web Development Course."

5. If the user asks about something **unrelated to the Sigma Web Development Course**, respond with:
   > "I can only answer questions related to the Sigma Web Development Course."

Make sure your final answer is **factual**, **context-aware**, and easy to understand.
AND THE RESPONSE SHOULD BE IN HUMAN READABLE FORM
"""


print(inference(prompt)["response"])