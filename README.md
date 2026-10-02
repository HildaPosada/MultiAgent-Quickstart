# [Multi-Agent Data Review](https://multiagent-demo-sigma.vercel.app/)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=111111)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Vercel](https://img.shields.io/badge/Vercel-171717?style=for-the-badge&logo=vercel&logoColor=white)](https://vercel.com/)

Paste JSON records and inspect a working data-review pipeline.

## Workers

1. Intake identifies record count and fields.
2. Quality checks missing values and duplicate records.
3. Summary calculates numeric ranges and means.
4. Validation reconciles the findings.

Each role runs in an independent browser Web Worker. The interface shows handoffs, actual findings, and a downloadable report. Input stays in the browser.

This deployed workflow uses deterministic rules. It does not call an LLM or verify real-world claims. The repository also contains separate Python agent prototypes.

## Run locally

Serve `web/` with a local HTTP server, then open it in a browser:

```bash
python -m http.server 8000 --directory web
```
