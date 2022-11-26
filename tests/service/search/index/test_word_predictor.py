import pytest

from autocomplete_api.service.search.index.word_predictor import WordPredictor
from tests.util.test_utils import load_json_data
from tests.common.constants import *


@pytest.fixture
def word_predictor() -> WordPredictor:
    scored_words = load_json_data(SCORED_WORDS_FILE)
    return WordPredictor(WORDS_LANGUAGE, scored_words)


class TestWordsPredictor:

    def test_words_predictions_non_top(self, word_predictor: WordPredictor):
        predictions = word_predictor.search('fr')

        assert len(predictions) == 7
        assert predictions[0] == 'free'
        assert predictions[1] == 'fries'
        assert predictions[2] == 'freedom'
        assert predictions[3] == 'fry'
        assert predictions[4] == 'frequency'
        assert predictions[5] == 'fresh'
        assert predictions[6] == 'freeze'


    def test_words_predictions_top_3(self, word_predictor: WordPredictor):
        predictions = word_predictor.search('fr', 3)

        assert len(predictions) == 3
        assert predictions[0] == 'free'
        assert predictions[1] == 'fries'
        assert predictions[2] == 'freedom'


    def test_words_predictions_not_found(self, word_predictor: WordPredictor):
        predictions = word_predictor.search('nor', 3)

        assert len(predictions) == 0
