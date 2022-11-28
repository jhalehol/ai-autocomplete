import pytest

from service.search.index.node_scored_word import NodeScoredWord
from model.models import ScoredWord


WORD_TESTED = 'word'
WORD_TESTED_2 = 'worst'
WORD_SCORE = 5
WORD_SCORE_2 = 2


@pytest.fixture
def node_score_word() -> NodeScoredWord:
    return NodeScoredWord()


class TestNodeScoredWord:


    def test_insert_scored_word(self, node_score_word: NodeScoredWord):
        scored_word = ScoredWord(WORD_TESTED, WORD_SCORE)
        scored_word2 = ScoredWord(WORD_TESTED_2, WORD_SCORE_2)

        node_score_word.insert(scored_word)
        node_score_word.insert(scored_word2)

        scored_word_result: ScoredWord = node_score_word.children['w'] \
            .children['o'] \
            .children['r'] \
            .children['d'].scored_word

        scored_word_result_2: ScoredWord = node_score_word.children['w'] \
            .children['o'] \
            .children['r'] \
            .children['s'] \
            .children['t'].scored_word

        assert scored_word_result.word == WORD_TESTED
        assert scored_word_result.score == WORD_SCORE
        assert scored_word_result_2.word == WORD_TESTED_2
        assert scored_word_result_2.score == WORD_SCORE_2

