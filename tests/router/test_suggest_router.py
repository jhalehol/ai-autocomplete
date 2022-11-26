import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from tests.mocks.search_service_mock import SearchServiceMock, SUGGESTED_WORDS
import autocomplete_api.context as context
from autocomplete_api.router.suggest_router import router as suggest_router

search_service = SearchServiceMock()
context.search_service = search_service

app = FastAPI()
app.include_router(suggest_router)

client = TestClient(app)


class TestSuggestRouter:

    def test_suggest_endpoint(self):
        response = client.get('/suggest?prefix=fr')
        assert response.status_code == 200
        assert response.json() == SUGGESTED_WORDS

    

