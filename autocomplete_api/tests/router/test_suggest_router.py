import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from exception.configuration_exception import ConfigurationException
from exception.forbidden_exception import ForbiddenException
from tests.mocks.search_service_mock import SearchServiceMock, SUGGESTED_WORDS
import context as context
from router.suggest_router import router as suggest_router


app = FastAPI()
app.include_router(suggest_router)

client = TestClient(app)

@pytest.fixture(autouse=False)
def service_search_ok():
    search_service = SearchServiceMock()
    context.search_service = search_service


@pytest.fixture(autouse=False)
def service_search_config_exception():
    search_service = SearchServiceMock(ConfigurationException("Config exception"))
    context.search_service = search_service


@pytest.fixture(autouse=False)
def service_search_forbidden_exception():
    search_service = SearchServiceMock(ForbiddenException("Limit Exception"))
    context.search_service = search_service

class TestSuggestRouter:


    @pytest.mark.usefixtures('service_search_ok')
    def test_suggest_endpoint(self):
        response = client.get('/suggest?prefix=fr')
        assert response.status_code == 200
        assert response.json() == SUGGESTED_WORDS

    
    @pytest.mark.usefixtures('service_search_config_exception')
    def test_suggest_endpoint(self):
        response = client.get('/suggest?prefix=fr')
        assert response.status_code == 500
        assert response.json() == {
            "detail": "Server configuration error"
        }

    
    @pytest.mark.usefixtures('service_search_forbidden_exception')
    def test_suggest_endpoint(self):
        response = client.get('/suggest?prefix=fr')
        assert response.status_code == 403
        assert response.json() == {
            "detail": "Limit Exception"
        }
