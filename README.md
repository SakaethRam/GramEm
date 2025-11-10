# GramEm Engine: Messaging -> AI Messageing 

**The world's first inline AI tone-trigger engine.**  
Type `{Formal}`, `{Casual, Emojis}`, `{Casual, Emojis, Translate}`, or `{Phrase: Professional}`, GramEm Engine instantly rephrases, completes (auto-phrases), and translates your text.  
Available as Chrome extension, desktop widget, and API || Powered By ARKIN X ENGINE

---
![GramEm](https://github.com/user-attachments/assets/881aab86-5379-424b-8d26-57bea44cad04)
---

---

## GramEm Engine Tiers Comparison


| Feature                          | **Basic** | **Premium** | **Advance** |
|----------------------------------|-----------|-------------|-------------|
| **LOC (approx)**                 | ~380      | ~510        | ~570        |
| `{Tone}` (Formal, Casual, etc.)  | Yes       | Yes         | Yes         |
| `{Tone, Emojis}`                 | No        | Yes         | Yes         |
| `{Tone, Translate}`              | No        | Yes         | Yes         |
| `Context ("Role=..., Company=...")` | No     | Yes         | Yes         |
| `{Phrase: Tone}` (Auto-complete) | No        | No          | Yes         |
| **Job Application Mode**         | No        | Yes         | Yes         |
| **Greeting Logic**               | No        | Yes         | Yes         |
| **Two-Step Translation Pipeline**| No        | Yes         | Yes         |
| **UI**                           | Modal     | Inline Popup| Modal       |
| **Debounce**                     | 600ms     | 500ms       | 600ms       |
| **Site Restriction**             | Yes       | Yes         | Yes         |
| **Encrypted API Key**            | Yes       | Yes         | Yes         |

---

## Features

GramEm is a **secure, intelligent, context-aware writing co-pilot** with **zero external dependencies** beyond encrypted Gemini API.

### Core Innovations
- **Trigger Syntax**: `{Tone}`, `{Tone, Emojis}`, `{Tone, Translate}`, `{Phrase: Tone}`
- **Auto-Complete Engine**: `{Phrase: Professional}` → expands incomplete thoughts
- **Context Parsing**: `"Role=Engineer, Company=Google"` → generates tailored emails
- **Smart Emoji Placement**: Tone-aware, contextual, never spammy

### Security & Privacy
- **AES-GCM Encrypted API Key** with PBKDF2-derived keys
- **Default Password**: `GramEm` (user-changeable)
- **Decryption at Runtime Only** — never stored in memory
- **Site Whitelisting**: Works only on Gmail, WhatsApp Web, Outlook

### UI/UX
- **Draggable Floating Action Button** (double-click to drag)
- **Smart Modal Positioning** (above/below based on viewport)
- **Inline Popup (Premium)** for faster interaction
- **Replace / Copy / Close** actions with hover effects

### Input Handling
- Listens to `input`, `keyup` on `textarea`, `input`, `contenteditable`
- **Debounce**: 600ms (Basic/Advance), 500ms (Premium)
- **Language Detection**: Lightweight English keyword regex

### Prompt Engineering
- **Strict Output Rules**:
  - No greetings unless in input
  - No exclamation marks
  - No emojis unless requested
  - Preserve question structure
- **Job Mode**: Auto-adds `Dear Hiring Manager,`
- **Completion Mode**: Uses `"Complete"` prefix instead of `"Rephrase"`

### Error Resilience
- Graceful handling of:
  - Decryption failure
  - API timeout / invalid response
  - Malformed context
  - Unsupported syntax

### Performance
- **Zero bundle bloat** — only essential code
- **No external libraries**
- **Fast cold-start** — activates in <100ms

---

## Project Structure

```
gramem-basic/
├── .github/
│   ├── workflows/
│   │   └── test.yml
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── feature_request.md
├── docs/
│   ├── index.md
│   ├── api.md
│   └── examples.md
├── examples/
│   └── cli_demo.py
├── tests/
│   └── test_core.py
├── gramem_basic/
│   ├── __init__.py
│   ├── core.py
│   ├── cli.py
│   └── __main__.py
├── GramEm.html
├── LICENSE
├── .gitignore
├── pyproject.toml
├── README.md
├── CODE_OF_CONDUCT.md
└── CHANGELOG.md
```

---

## Installation (Local)

1. **Install from Source (Developers)**
```bash
git clone "https://github.com/SakaethRam/GramEm.git"
cd gramem-basic
pip install .
```
>Enables editing, forking, and extending.

2. **Install via pip (Recommended)**
```bash
pip install gramem-basic
```
>Installs the open-source {TONE TYPE} engine in <2 seconds.

3. **Python API Usage**
```bash
>>> from gramem_basic import rephrase, ToneEngine

>>> rephrase("Hey {Casual}")
'Hey! How\'s it going? GRAMEM ENGINE'

>>> engine = ToneEngine()
>>> engine.add_tone("Pirate", {"hello": "ahoy"})
>>> engine.rephrase("hello {Pirate}")
'Ahoy. GRAMEM ENGINE'
```

---

## Running with Docker

### Build the Docker image
```bash
cd gramem-basic  # Your project root
docker build -t gramem-basic:latest .
```

---

### Dockerfile

```dockerfile
# gramem-basic/Dockerfile
# Official Docker image for GramEm Basic - Open-Source {TONE TYPE} Engine
# Runs CLI demo by default; extend for custom apps

FROM python:3.11-slim

# Set metadata
LABEL maintainer="GramEm Team <hello@gramem.dev>"
LABEL version="0.2.0"
LABEL description="Open-source core of GramEm Engine: {TONE TYPE} trigger command parser"

# Install system dependencies (minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Python package
RUN pip install --no-cache-dir gramem-basic

# Create app directory
WORKDIR /app

# Copy entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Expose port (for API extensions)
EXPOSE 8080

# Run interactive CLI demo by default
ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "-c", "from gramem_basic.examples.cli_demo import *; main()"]
```

---

## **Contribution Guidelines**  
Contributions are welcome. To contribute:  
1. Fork the repository.  
2. Create a feature branch.  
3. Implement your changes.  
4. Submit a pull request with a clear description of modifications.  

---

Built by `S A M` – Bringing emotion and intelligence to message.

