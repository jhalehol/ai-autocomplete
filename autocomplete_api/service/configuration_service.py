import configparser as config_reader

from autocomplete_api.config.configuration import ApplicationConfiguration    

CONFIGURATION_FILE = 'application.properties'
LANGUAGES_SECTION = 'Languages'

class ConfigurationService:

    def __init__(self) -> None:
        self.__load_configuration()
    
    
    def load_configuration(self) -> ApplicationConfiguration:
        """Returns the configuration object with the configured properties in the application.configuration file

        Returns:
            ApplicationConfiguration: Application configuration object
        """
        self.config_manager = config_reader.RawConfigParser()
        self.config_manager.read(CONFIGURATION_FILE)
        config = ApplicationConfiguration()
        config.default_language = self.__load_language_parameter('language.default')
        config.default_language_path = self.__load_language_parameter('language.default.path')
        return config


    def __load_language_parameter(self, parameter: str):
        self.config_manager.get(LANGUAGES_SECTION, parameter)
