# brainctl 🧠⚙️
```
**brainctl** is a modular automation framework designed to orchestrate infrastructure provisioning, validation, and scoring — all driven by natural language.

At its core, brainctl connects three powerful layers:

- 🧠 **Rick's Brain**: A natural language interface that receives questions or commands and routes them to appropriate skills.
- ⚙️ **Worker Rick**: A backend logic engine that executes skills like semantic search, summarization, and deployment coordination.
- 🚀 **Infrastructure Pipeline**:
  - **Ansible**: For deploying and configuring services
  - **Go Validator**: For testing and validating infrastructure state
  - **Scoring**: For quantifying and analyzing validation output

All of this is triggered and coordinated through a chatbot interface, making DevOps more human and intelligent.


```
## 📦 Project Structure

```

brainctl/
├── rick_brain/              # Entry point and chatbot interface
│   ├── main.py              # CLI frontend
│   ├── router.py            # Routes requests to Worker Rick
│   ├── config.py            # Project-wide configuration
│   └── worker_rick/         # Skill engine
│       ├── core.py          # Dispatcher and skill loader
│       └── skills/          # Pluggable skill modules (search, summarize, etc.)
├── ansible/                 # Playbooks and roles for provisioning
├── go_validator/            # Go app for infrastructure validation and scoring
├── tests/                   # Unit tests for all skills
├── generate_tests.py        # Script to autogenerate skill tests
├── .pre-commit-config.yaml  # Auto-run test generation on commit
└── requirements.txt         # Python dependencies (in project root)

```


---

## 💡 Example Skills

- `search:` – Semantic search through local notes or knowledge base
- `summarize:` – Text summarization for large outputs
- `help:` – Lists all available commands
- `deploy:` – Triggers Ansible playbook execution (planned)
- `validate:` – Runs Go-based verification pipeline (planned)

---

## 🛠 Getting Started

```bash
# Clone the repo
git clone git@github.com:DesertBlume/brainctl.git
cd brainctl

# (Optional) Set up virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies (located in the project root)
pip install -r requirements.txt

# Run Rick's Brain
python3 rick_brain/main.py

````

---

## 🧪 Testing

```bash
# Generate unit tests for new skills
python3 generate_tests.py

# Run all tests
pytest
```

---

## 🛡️ Project Philosophy

> Infrastructure should listen before it acts.

**brainctl** turns high-level intent ("Deploy the DNS server") into verified, scored outcomes — all without writing a shell script or opening a dashboard. It’s built to empower automation with intelligence, clarity, and trust.

---

## 📍 Roadmap

* [x] Natural language routing (`Rick's Brain`)
* [x] Modular skill system (`Worker Rick`)
* [x] Auto-generated skill tests
* [x] Pre-commit hooks for test enforcement
* [ ] Ansible deployment trigger via skill
* [ ] Go-based infrastructure validation and scoring
* [ ] CLI and web UI interface options

---

## 👨💻 Author

Made by Hmoad Hajali AKA [DesertBlume](https://github.com/DesertBlume)

---

## 🗝 License

MIT — free to use, hack, and evolve.
