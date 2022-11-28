
# Autocomplete API

API that provides suggestions functionality given a prefix provided by the user, returns a list of suggested words to be used for completion, the list of suggested words is based in unix dictionary (`/usr/share/dict/words`) words are scored based in the level of usage given the most top words.

Current main endpoint provided is `/suggest/?prefix=<your-prefix>&limit=<your-limit>` that supports two query parameters to retrieve the suggested words:

* `prefix`: An string that contains the initial characters used to retrieve the prediction of possible words for usage.

* `limit`: An optional parameter that allows to limit the number of words in the result, if this parameter is not defined, it will use the default limit provided in the application.properties file.

For more information about the API you can use the swagger documentation provided by the application after be running the API (Section below is provided a section with additional details about how to access swagger documentation).

## Building, Testing and Running

### Requirements

Python3 is required, to run and test the application locally we suggest to use a separated python environment to install all required dependencies use your preferred environment manager ([venv](https://docs.python.org/3/library/venv.html), [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/environments.html#:~:text=A%20conda%20environment%20is%20a,NumPy%201.6%20for%20legacy%20testing.), others).

* Installing python requirements

```
pip install -r requirements/requirements.txt
```

* Running application (From the `autocomplete_api` path)

```
uvicorn app:app --reload --port 9000
```

Or running from `root path` through the script `./run.sh`

Then you can access swagger documentation for the API from `http://localhost:9000/docs`

### Running tests (`From root path`)

Using script will create/activate python environment and will install dependencies required for tests 

```
./run-tests-with-coverage.sh
```

or using directly the command line from root path use command (Environment should be already active):

```
pytest --cov
```

In both cases it will generate a report of coverage, ideally the test coverage should be maintained not lower than 80% (https://www.atlassian.com/continuous-delivery/software-testing/code-coverage)

### Running the application from Docker

* Build docker image using script (It will run test suite before build docker image):

```
./build-image.sh
```

* Running docker image will expose port 9000 by default to access the application

```
docker run -e APP_PORT=9000 -p 9000:9000 --name autocomplete --rm -d autocomplete
```

or using docker compose, run:

```
docker-compose up -d
```

To stop the docker stack after run docker-compose you can run

```
docker-compose down
```

### Testing API performace

To test the API performance, there is provided the script `test-speed.sh` that generates an report with the time consumed during the call to the endpoint locally used for suggestions, call the script:

```
./test-speed.sh
```

it will generate a report similar to (with your own results):

```
Request output:

============
Metrics result:
time_namelookup:    0.005223s
time_connect:       0.005549s
time_appconnect:    0.000000s
time_pretransfer:   0.005588s
time_redirect:      0.000000s
time_starttransfer: 0.006390s
                    ----------
time_total:         0.006442s
```


### API Documentation

You can use the API directly through the generated documentation provided by swagger via `http://localhost:9000/docs` after run the application according to previous steps provided.


## Initial words dictionary and scores

The current score of the provided list of words was built through the analysis of the top of english words used according to [www.ef.com](https://www.ef.com/wwen/english-resources/english-vocabulary/), in the folder `/data` is provided the script `build_words_scoring.py` that can be used with and the files with the top words used, that allows to score the initial words list, the `words_scored` file is already built, but if its required the rules or the top words files can be updated to build a new dictionary of scored words, for this run the script:


```
python build_words_scoring.py <your-file-with-words-to-score>
```

The output of the script will create the file `words_scored`

## Project milestones:

The functional requirements are split in different milestones, where first milestone covers the initial requirements, next milestones are future work to improve and extend the functionality of the service (Not provided in the initial scope).

## Functional requirements

### Milestone 1

* As user I want to provide a string prefix to the application that allows to me to retrieve a list of suggested words that matches with the prefix.

* As User I want that the application uses an scoring parameter to match the suggested words, that allows to me to get the most probable words to be used.

* As User I want to define the limit of suggested words as optional to retrieve only the necessary words on my autocomplete functionality

### Milestone 2

* As User I want to send to the application the selected word that allows to the application update the scores of the top words used and then improve for the future the list of suggested words

### Milestone 3

* As User I want to specify the language of the prefix to get the list of suggested words according to the provided language.

###  Milestone 4

* As User I want to have a personal dictionary of used words that allows to the application to personalize the results according to my words usage, then improve the suggested words according to my profile.

* Introduce machine learning models that allows to learn the usage of words of the application users.

## Non Functional Requirements

* Responses should not take more than <100ms 
* REST API service should be provided



