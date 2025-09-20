from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from simple_agent_demo import AgentOrchestrator

app = FastAPI()
orchestrator = AgentOrchestrator()

@app.get("/")
async def home():
    return HTMLResponse("<h1>🤖 Multi-Agent Research Demo</h1><p>Use /api/research to POST queries.</p>")

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
    
    # Run orchestrator synchronously for now
    result = await orchestrator.process_query(query)
    return result
