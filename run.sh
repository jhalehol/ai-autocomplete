# usr/local/bin/bash

echo "Preparing environment"
python3 -m venv .venv 
source .venv/bin/activate
pip install -r requirements/requirements.txt

pushd autocomplete_api
uvicorn app:app --reload




