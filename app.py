from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from simple_agent_demo import AgentOrchestrator

app = FastAPI()
orchestrator = AgentOrchestrator()

# Load the full HTML UI (copied from DemoWebHandler)
HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Internet of Agents - Multi-Agent Research Demo</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sanitize.css">
  <style>
    body { font-family: system-ui, sans-serif; background: linear-gradient(135deg,#667eea,#764ba2); margin:0; padding:20px; }
    .container { max-width:1000px; margin:0 auto; background:#fff; border-radius:20px; padding:30px; }
    h1 { text-align:center; margin-bottom:10px; }
    .subtitle { text-align:center; color:#666; margin-bottom:30px; }
    /* keep your CSS from simple_agent_demo.py here */
  </style>
</head>
<body>
  <div class="container">
    <h1>🤖 Internet of Agents</h1>
    <p class="subtitle">Multi-Agent Research Assistant Demo</p>
    <div id="app"></div>
  </div>
  <script>
    // copy the JavaScript from your simple_agent_demo.py here
  </script>
</body>
</html>
"""

@app.get("/")
async def home():
    return HTMLResponse(HTML_PAGE)

@app.get("/health")
async def health():
    return {"status": "running", "agents": 3}

@app.get("/api/results")
async def get_results():
    return {"results": orchestrator.results_history}

@app.post("/api/research")
async def research(request: Request):
    body = await request.json()
    query = body.get("query", "").strip()
    if not query:
        return JSONResponse({"error": "Query required"}, status_code=400)
    
    result = await orchestrator.process_query(query)
    return result
