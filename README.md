# Compose.AI Backend Engineer Takehome Test
The instructions for this test can be found at https://docs.google.com/document/d/13pKrfrBF0-PRGc16JMT6QRjinOiDnbaf7XU5rnJ5GzE .
This repository serves as a convenient skeleton to start building your app.  It includes a Dockerfile, build scripts, test setup, dictionary, and hello-world CLI application.  You will be responsible for converting this into a containerized python server that can respond to REST requests as described in the test outline.  Please make your own copy of this repo, and don't publish it to any public accounts.

This skeleton was adapted from https://github.com/mozilla/generic-python-docker .

## Development and Testing

While iterating on development, we recommend using virtualenv
to run the tests locally.

### Run tests locally

Install requirements locally:
```
python3 -m virtualenv venv
source venv/bin/activate
make install-requirements
```

Run tests locally:
```
python -m pytest tests/
```

### Run tests in docker

You can run the tests just as CI does by building the container
and running the tests.

```
make clean && make build
make test
```
