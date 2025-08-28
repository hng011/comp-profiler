# Comp-Prof 📸
Comp-prof, which stand for Company-Profiler, is a full-stack web app built with FastAPI and React. It scrapes a company website based on a given URL and uses [Google AI API](https://aistudio.google.com/) to generate a concise analysis based on the site's content and user-provided notes.

**The Web App**: https://meek-custard-450598.netlify.app/

## How To... 🔎

### Prerequisites
1. Python >= 3.12
2. Node.js >= v22.18.0 (which includes npm)
3. Git

### Steps
1. clone this repository
```bash
gh repo clone hng011/comp-profiler
cd comp-profiler
```

2. Back-end setup `/be`
```bash
cd be
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

3. Env Variables Configuration
```bash
cp .env.example .env
```
Then open the .env and fill in the following variables 
```bash
API_NAME=backendapp
API_VERSION=0.0.0
API_KEY=key123

AI_API_KEY="Your google AI API key"
AI_API_ENDPOINT="Your google AI API ENDPOINT"
MAX_GENERATED_SUM=5000
SYSTEM_PROMPT="your system prompt"


ALLOWED_ORIGINS='["*"]'
ALLOWED_CREDENTIALS=True
ALLOWED_METHODS='["*"]'
ALLOWED_HEADERS='["*"]'

MAX_LEN_SCRAPER=5000

# OPTIONAL SETTINGS
AZURE_REGISTERY_NAME=
AZURE_STORAGE_ACCESS_KEY=
LOCAL_REPO=
ACR_REPO=
IMAGE_NAME=

HOST_PORT=8080
APP_PORT=8080
```
4. Run the program
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

5. Front-end setup `/fe`
```bash
cd ../fe/app # navigate to the front-end dir from the project root
npm install
```

6. Env variables configuration for the front-end app
```bash
cp .env.example .env
```
Then fill in the following variables
```bash
# The full URL to your backend's generate endpoint
VITE_API_ENDPOINT=<http://localhost:8080/api/v1/insight/generate>

 # the API_KEY you set in the backend's .env file
VITE_API_KEY=key123
```

7.  Run the program
```bash
npm run dev
```