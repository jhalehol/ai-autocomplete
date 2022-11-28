import configparser as config_reader
import logging
from os import path

from model.models import ApplicationConfiguration    

CONFIGURATION_FILE = 'application.properties'
LANGUAGES_SECTION = 'Languages'
SEARCH_SECTION = 'Search'

class ConfigurationService:

    __LOGGER = logging.getLogger(__name__)

    def __init__(self, base_path: str) -> None:
        self.base_path = base_path
        self.load_configuration()
    
    
    def load_configuration(self) -> ApplicationConfiguration:
        """Returns the configuration object with the configured properties in the application.configuration file

        Returns:
            ApplicationConfiguration: Application configuration object
        """
        config_file_path = path.join(self.base_path, CONFIGURATION_FILE)
        self.__LOGGER.debug('Using configuration file %s', config_file_path)
        self.config_manager = config_reader.RawConfigParser()
        self.config_manager.read(config_file_path)
        config = ApplicationConfiguration()
        config.default_language = self.__load_language_parameter('language.default')
        config.default_language_path = self.__load_language_parameter('language.default.path')
        config.default_suggestion_limit = self.__load_search_parameter('limit.suggestion')
        config.max_results = self.__load_search_parameter('search.max')

        return config


    def __load_language_parameter(self, parameter: str):
        return self.config_manager.get(LANGUAGES_SECTION, parameter)


    def __load_search_parameter(self, parameter: str):
        return self.config_manager.getint(SEARCH_SECTION, parameter)
