# /usr/local/bin/bash

echo "Preparing tests environment"
python3 -m venv .venv 
source .venv/bin/activate
pip install -r requirements/test_requirements.txt

echo "Running tests with coverage"
pushd autocomplete_api
pytest --cov

popd
