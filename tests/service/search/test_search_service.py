import pytest

from autocomplete_api.config.configuration import ApplicationConfiguration
from autocomplete_api.service.search.search_service import SearchService
from tests.util.test_utils import build_resource_absolute_path
from tests.common.constants import *


@pytest.fixture
def configuration() -> ApplicationConfiguration:
    config = ApplicationConfiguration()
    config.default_language = WORDS_LANGUAGE
    config.default_language_path = build_resource_absolute_path(SCORED_WORDS_FILE)
    return config


@pytest.fixture
def search_service(configuration: ApplicationConfiguration) -> SearchService:
    return SearchService(configuration)


class TestIndexService:

    def test_search_service(self, search_service: SearchService):
        suggestions = search_service.search("wi")

        assert suggestions == ['wild', 'wish']


    def test_search_service_top(self, search_service: SearchService):
        suggestions = search_service.search("wi", 1)

        assert suggestions == ['wild']


