import json
import os
import logging

from autocomplete_api.model.models import ApplicationConfiguration
from autocomplete_api.exception.configuration_exception import ConfigurationException
from autocomplete_api.service.search.index.word_predictor import WordPredictor
from autocomplete_api.exception.forbidden_exception import ForbiddenException


class SearchService:

    __LOGGER = logging.getLogger(__name__)
    __indexes_predictors: dict = {}

    def __init__(self, configuration: ApplicationConfiguration) -> None:
        self.configuration: ApplicationConfiguration = configuration
        self.__build_indexes()


    def search(self, prefix: str, top: int = None) -> list:
        """Executes a search of the given prefix in the current indices configured
        in the application to get the suggested words accordingly 

        Args:
            prefix (str): Prefix used for the search
            top (int, optional): If its required a limit of the results. Defaults to None.

        Returns:
            list: List of words suggested according to the given index
        """
        return self.__search(self.configuration.default_language, prefix, top)


    def __search(self, language: str, prefix: str, limit: int) -> list:
        if language not in self.__indexes_predictors.keys():
            self.__LOGGER.error('Invalid language {}'.format(language))
            raise ConfigurationException("Language {} is not supported for search!".format(language))

        limit = limit if limit else self.configuration.default_suggestion_limit
        if limit > self.configuration.max_results:
            raise ForbiddenException('Exceeded the allowed limit of suggestions, {} is the max value of results allowed'.format(self.configuration.max_results))

        predictor: WordPredictor = self.__indexes_predictors[language]
        return predictor.search(prefix, limit)


    def __build_indexes(self):
        default_language = self.configuration.default_language
        default_language_path = self.configuration.default_language_path
        self.__LOGGER.info('Building indices using language %s dictionary %s', default_language, default_language_path)
        self.__add_index(default_language, default_language_path)


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
