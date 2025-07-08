#!/bin/env bash
set -euo pipefail

# set up Node.js dependencies and run n8n
if which npm >/dev/null 2>&1; then
  npm install

  echo "===================="
  echo "Running n8n..."
  echo "===================="
  npx n8n | tee -a n8n_log.log &
	PIDARRAY+=("$!")

else
  echo "NPM not installed."
  exit 1
fi

# set up Python dependencies and run project
if which uv >/dev/null 2>&1; then # using UV
  uv sync

  echo "===================="
  echo "Running API..."
  echo "===================="
  uv run ./main.py | tee -a api_log.log &

else # using virtual env
  [[ -d ./.venv/ ]] || python -m venv .venv
  source ./.venv/bin/activate
  pip install -r requirements.txt

  echo "===================="
  echo "Running API..."
  echo "===================="
  python3 ./main.py | tee -a api_log.log &
fi

# wait until all jobs exit
wait < <(jobs -p)
