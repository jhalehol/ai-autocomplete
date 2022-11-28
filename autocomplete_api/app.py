import uvicorn
import sys
import logging
import os
from fastapi import FastAPI

from router.suggest_router import router as suggestions_router
from service.configuration_service import ConfigurationService
from service.search.search_service import SearchService
import context

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)
logger = logging.getLogger()
path_base = os.path.dirname(__file__)


app = FastAPI(title="Autocomplete Application", description="Endpoints provided for autocomplete operations", version="1.0")

def initialize_context():
    logger.info('Initializing application context!')
    config_service = ConfigurationService(path_base)
    config = config_service.load_configuration()
    context.app_config = config
    context.search_service = SearchService(config)


def initialize_router():
    app.include_router(suggestions_router)


def initialize_app():
    initialize_context()
    initialize_router()
    

@app.on_event("startup")
async def app_started():
    initialize_app()

if __name__ == "__main__":
    initialize_app()
    uvicorn.run(app)
