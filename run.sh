#!/bin/env bash
set -euo pipefail

N8N_LOGFILE="n8n_log.log"
API_LOGFILE="api_log.log"

# set up Node.js dependencies and run n8n
if which npm >/dev/null 2>&1; then
  npm install

  echo "===================="
  echo "Running n8n..."
  echo "===================="

  echo -e "$(date)\n" >>"$N8N_LOGFILE"
  npx n8n | tee -a >>"$N8N_LOGFILE" &

else
  echo "NPM not installed."
  exit 1
fi

# set up Python dependencies and run project
if which uv >/dev/null 2>&1; then
  uv sync
else
  [[ -d ./.venv/ ]] || python -m venv .venv
  pip install -r requirements.txt
fi && {
  source ./.venv/bin/activate

  echo "===================="
  echo "Running API..."
  echo "===================="

  echo -e "$(date)\n" >>"$API_LOGFILE"
  fastapi dev | tee -a "$API_LOGFILE" &
}

# block until all jobs exit
wait < <(jobs -p)
