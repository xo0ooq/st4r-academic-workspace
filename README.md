# ST4R — Academic Workspace

**Status: experimental prototype (v0.1.0). Not production-ready.**

ST4R is an independent, student-led open-source project exploring tools for academic task organization and, eventually, educational service integrations and AI-assisted workflows. It is **not** an official university product.

## Implemented today

- A FastAPI service for creating, listing, completing and deleting academic tasks
- Optional course names and due dates
- A health endpoint
- Automated API tests and a GitHub Actions test workflow

All tasks are held **in memory** and are lost after restart. This release has no authentication, access controls, persistent storage, integrations, or AI features. **Do not deploy publicly or store real student/personal data.**

## Quick start

Python 3.10+ is required.

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS / Linux: source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m uvicorn st4r.main:app --host 127.0.0.1 --port 8000
```

Open http://127.0.0.1:8000/docs for interactive API documentation.

Example:

```bash
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Prepare presentation","course":"Management","due_date":"2026-12-01"}'
curl http://127.0.0.1:8000/tasks
```

## Development and testing

```bash
python -m pip install -e '.[dev]'
python -m pytest -q
```

The repository includes a GitHub Actions workflow that runs tests on pushes and pull requests. Test success should be verified in the **Actions** tab.

## Roadmap

See [docs/roadmap.md](docs/roadmap.md). Persistence, authorization, Google Classroom/Drive/Gmail connectors and AI functionality are **plans**, not delivered features.

## Contributing and security

Contributions are welcome: [CONTRIBUTING.md](CONTRIBUTING.md).
For security limitations and reporting: [SECURITY.md](SECURITY.md).

## License

[MIT](LICENSE).

## Project impact

ST4R is at an early stage. There are currently no verified adoption, download, or ecosystem-impact metrics. The project does not claim eligibility for any particular third-party grant or maintainer program.
