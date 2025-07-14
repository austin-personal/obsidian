# Steps
### 1. Set up env
`curl -LsSf https://astral.sh/uv/install.sh | sh`

### 2.
```bash
# Create a new directory for our project 
uv init weather 
cd weather 
# Create virtual environment and activate it 
uv venv 
source .venv/bin/activate 
# Install dependencies 
uv add "mcp[cli]" httpx 
# Create our server file 
touch weather.py
```
