import json
import os
import logging

from autocomplete_api.config.configuration import ApplicationConfiguration
from autocomplete_api.exception.configuration_exception import ConfigurationException
from autocomplete_api.service.search.model.word_predictor import WordPredictor


class SearchService:

    __LOGGER = logging.getLogger(__name__)
    __indexes_predictors: dict = {}

    def __init__(self, configuration: ApplicationConfiguration) -> None:
        self.configuration = configuration
        self.__build_indexes()


    def search(self, prefix: str, top: int = None) -> list:
        return self.__search(self.configuration.default_language, prefix, top)


    def __search(self, language: str, prefix: str, top: int) -> list:
        if language not in self.__indexes_predictors.keys():
            self.__LOGGER.error('Invalid language {}'.format(language))
            raise ConfigurationException("Language {} is not supported for search!".format(language))

        predictor: WordPredictor = self.__indexes_predictors[language]
        return predictor.search(prefix, top)


    def __build_indexes(self):
        self.__add_index(self.configuration.default_language, self.configuration.default_language_path)


    def __add_index(self, language:str, source_path:str):
        words_scores: dict = self.__get_scores_from_source(source_path)
        index_predictor = WordPredictor(language, words_scores)
        self.__indexes_predictors[language] = index_predictor
        

    def __get_scores_from_source(self, source_path:str) -> dict:
        if not os.path.exists(source_path):
            raise ConfigurationException("Language data source '{}' does not exist!")

        with open(source_path) as source_file:
            source_data = json.load(source_file)

        return source_data
