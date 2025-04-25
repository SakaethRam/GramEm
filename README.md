# ZREX GramEm: AI-Powered Grammar and Sentiment Enhancement API

GramEm is an intelligent text-enhancement tool that not only corrects grammar using a T5 transformer but also analyzes sentence emotions using a BERT-based model. It then adds relevant emojis to match the sentiment of the text—bringing more life and personality to user messages.

---
![GramEm](https://github.com/user-attachments/assets/881aab86-5379-424b-8d26-57bea44cad04)
---
## Features

- Grammar correction using T5 Transformer.
- Emotion classification using BERT (Happy, Sad, Angry, etc.).
- Emoji injection based on emotion context.
- Easy to run in Docker for consistent environments.

---

## Project Structure

```
├── GramE - Emotion Classification Model (BERT).ipynb
├── GramEm - Grammar Correction Model (T5).ipynb
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## Installation (Local)

1. **Clone the Repository**
```bash
git clone https://github.com/your-username/GramEm.git
cd GramEm
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the Notebooks**
Open both notebooks using Jupyter:
```bash
jupyter notebook
```

---

## Running with Docker

### Build the Docker image
```bash
docker build -t gramem .
```

### Run the container
```bash
docker run -p 8888:8888 gramem
```

Then open the link provided in your terminal (e.g., `http://127.0.0.1:8888/?token=...`) to access the Jupyter notebooks in your browser.

---

## Requirements

- Python 3.8+
- Transformers
- Torch
- Scikit-learn
- Jupyter
- Emoji
- TextBlob

Make sure to have a `requirements.txt` with the following:

```
transformers
torch
scikit-learn
emoji
textblob
jupyter
```

### Dockerfile

```dockerfile
# Use an official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install required system packages
RUN apt-get update && apt-get install -y git && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Jupyter Notebook port
EXPOSE 8888

# Run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

---

## **Contribution Guidelines**  
Contributions are welcome. To contribute:  
1. Fork the repository.  
2. Create a feature branch.  
3. Implement your changes.  
4. Submit a pull request with a clear description of modifications.  

---

## License

MIT License

---

Built by `S A M` – Bringing emotion and intelligence to text.

---
