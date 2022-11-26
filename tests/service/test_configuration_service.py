import pytest

from autocomplete_api.service.configuration_service import ConfigurationService
from autocomplete_api.model.models import ApplicationConfiguration
from tests.util.test_utils import get_resource_absolute_path


@pytest.fixture
def config_service() -> ConfigurationService:
    path = get_resource_absolute_path()
    return ConfigurationService(path)


class TestConfigurationService:


    def test_configuration_load(self, config_service: ConfigurationService):
        config: ApplicationConfiguration = config_service.load_configuration()

        assert config.default_language == 'EN'
        assert config.default_language_path == '/test/path'
        assert config.default_suggestion_limit == 4
        assert config.max_results == 80
