# ZREX GramEm: AI-Powered Grammar and Sentiment Enhancement API

## **1. Introduction**  
GramEm is an advanced text processing API that corrects grammar and spelling errors while enhancing text with sentiment-based emoji suggestions. The system is designed for developers and businesses seeking an intelligent language enhancement tool that operates efficiently in an offline environment.

### **1.1 Purpose**  
The primary objectives of GramEm are:  
- To provide automated grammar and spelling correction using deep learning models.  
- To analyze sentiment in text and enhance user expression with appropriate emojis.  
- To operate without reliance on external blockchain infrastructure for full offline functionality.  

---
![GramEm](https://github.com/user-attachments/assets/881aab86-5379-424b-8d26-57bea44cad04)
---
## **2. Technologies Used**  

### **2.1 Programming Languages & Frameworks**  
- **Python** – Core programming language  
- **Flask** – Web framework for API development  

### **2.2 Machine Learning Models**  
- **T5ForConditionalGeneration** – Grammar correction model  
- **BERT (GoEmotions)** – Sentiment analysis model  

### **2.3 Supporting Libraries**  
- **SpellChecker** – Spelling correction  
- **Regular Expressions (re)** – Text preprocessing  
- **Torch** – Deep learning framework  

---

## **3. Installation and Setup**  

### **3.1 System Requirements**  
- **Python version**: 3.8 or later  
- **Operating System**: Windows, macOS, or Linux  
- **Memory**: Minimum 4GB RAM (Recommended: 8GB)  

### **3.2 Dependency Installation**  
Before running the application, install all required dependencies using the following command:

```bash
pip install flask transformers torch regex spellchecker
```

---

## **4. Running the Application**  

### **4.1 Local Execution**  
To run the API locally, execute:

```bash
python GramEm.py
```

By default, the API will be available at:  
**http://127.0.0.1:8000/process**

---

## **5. Deploying with Docker**  

### **5.1 Creating the Docker Image**  

Build the Docker image using the following command:

```bash
docker build -t gramem-api .
```

### **5.2 Running the Docker Container**  
Execute the following command to run the API inside a Docker container:

```bash
docker run -d -p 8000:8000 --name gramem-container gramem-app
```

The API will now be accessible at:  
**http://localhost:8000/process**

---

## **6. API Usage**  

### **6.1 Endpoint**  
**POST /process**  

### **6.2 Request Format**  
The API expects a JSON payload with the following structure:

```json
{
  "text": "i'm exicited",
  "username": "test_user"
}
```

### **6.3 Response Format**  
Upon successful processing, the API will return a response in the following format:

```json
{
  "Original Text": "i'm exicited",
  "GramEm Text": " I'm excited. 🤩",
  "Hive Post Url": "Hive posting is currently disabled (offline mode)."
}
```

---

## **7. Additional Notes**  
- This version operates in **offline mode**, with no blockchain connectivity.  
- The emoji mappings are configurable in `Mapping.py`.  
- Docker deployment is recommended for production environments.  

---

## **8. Contribution Guidelines**  
Contributions are welcome. To contribute:  
1. Fork the repository.  
2. Create a feature branch.  
3. Implement your changes.  
4. Submit a pull request with a clear description of modifications.  

---

## **9. License**  
This project is licensed under the **MIT License**.  

