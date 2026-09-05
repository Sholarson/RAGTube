# **RAGTube**

RAGTube is a fully local, open-source RAG (Retrieval-Augmented Generation) system that explains topics from YouTube videos by **downloading**, **transcribing**, **embedding** and **retrieving** video content.  

Everything runs **100% locally** using **Ollama**, **Whisper**, and **open-source LLMs** — no APIs, no cloud, no paid services.

---

## 🚀 **1. Python & Pip Version**

This project works with:
- **Python: 3.10 and above**
- **pip: 23.x and above**

(Confirmed working on **Python 3.13.7** and **pip 25.2**.)

---

## 📦 **2. Install Python Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🤖 **3. Install Ollama & Models**

### Install Ollama
Download and install Ollama from: [https://ollama.ai](https://ollama.ai)

### Download Required Models
```bash
ollama pull llama3.2
ollama pull bge-m3
```

- **llama3.2**: Used for generating answers and summarizing content
- **bge-m3**: Used for creating vector embeddings

### Start Ollama Server on another tab
```bash
ollama serve
```


## 📹 **4. Download YouTube Videos**

Choose one based on your needs:

### For Playlists:
```bash
python youtube_video_playlist_downloader.py
```

### For Individual Videos:
```bash
python youtube_video_downloader.py
```

---

## 🎵 **5. Convert MP4 to MP3**

**Before running**, edit `mp4_mp3_conversion.py`:
- Go to **line 5** and **line 15**
- Uncomment/comment the appropriate lines based on which downloader you used:
  - `YouTube_playlist` folder (for playlist downloads)
  - `YouTube_video` folder (for individual video downloads)
```bash
python mp4_mp3_conversion.py
```

---

## 📝 **6. Transcribe Audio to Text**

**For non-English audio**, edit `speech_to_text_chunking.py`:
- Go to **line 21** 
- Follow instructions to specify language
- Language codes: [https://github.com/openai/whisper/blob/main/whisper/tokenizer.py](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py)
```bash
python speech_to_text_chunking.py
```

---

## 🧠 **7. Create Vector Embeddings**
```bash
python read_chunk_and_embedding.py
```

---

## 💬 **8. Query the System**
```bash
python process_incomming.py
```

Now ask questions about the videos and get AI-powered answers with timestamps!

---

## 📁 **Project Structure**
```
RAGTube/
├── youtube_video_downloader.py          # Download individual videos
├── youtube_video_playlist_downloader.py # Download playlists
├── mp4_mp3_conversion.py                # Convert videos to audio
├── speech_to_text_chunking.py           # Transcribe audio using Whisper
├── read_chunk_and_embedding.py          # Generate embeddings
├── process_incomming.py                 # Query interface
├── requirements.txt                      # Python dependencies
├── YouTube_video/                        # Individual video downloads
├── YouTube_playlist/                     # Playlist downloads
├── audio/                                # Extracted audio files
├── jsons/                                # Transcription chunks
└── vector_embeddings.joblib              # Vector database
```

---

## 🎯 **How It Works**

1. **Download** YouTube videos/playlists
2. **Extract** audio from videos
3. **Transcribe** using Whisper (large-v2)
4. **Embed** text chunks using bge-m3
5. **Retrieve** relevant chunks via cosine similarity
6. **Generate** answers using llama3.2

---

## ⚡ **Features**

- ✅ Fully local execution
- ✅ No API keys or subscriptions
- ✅ Open-source stack
- ✅ Timestamp-based search
- ✅ Multi-language support
- ✅ RAG-powered answers
