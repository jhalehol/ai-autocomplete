from .node_scored_word import NodeScoredWord
from autocomplete_api.model.models import ScoredWord


SCORE_FIELD = 'score'
WORD_FIELD = 'word'


class WordPredictor:


    def __init__(self, language: str, scored_words: list) -> None:
        self.language = language
        self.root = NodeScoredWord()
        self.__initialize(scored_words)


    def search(self, prefix: str, top: int = -1) -> list[str]:
        """Search into the internal index the given prefix and returns the probable words suggested according to the prefix

        Args:
            prefix (str): Prefix used to search into the index
            top (int, optional):Allows to limit the suggestion to the given number if it's not provided it will return all suggested words. Defaults to -1.

        Returns:
            list[str]: List of suggested words that match with the index and the given threshold
        """
        if len(prefix) > 0:
            shared_node: NodeScoredWord = self.__find_shared_node(prefix, self.root)
            if shared_node:
                leaves: list[NodeScoredWord] = self.__get_node_leaves(shared_node)
                leaves_sorted: list[NodeScoredWord] = sorted(leaves, key = lambda node: node.scored_word.score, reverse=True)
                suggested_words = list(map(lambda node : node.scored_word.word, leaves_sorted))
                return suggested_words if top == -1 else suggested_words[:top]

        return []

        
    def __initialize(self, scored_words: list) -> None:
        sorted_scores = self.__order_scored_words(scored_words)
        for word_score in sorted_scores:
            scored_word = ScoredWord(word_score[WORD_FIELD], word_score[SCORE_FIELD])
            self.root.insert(scored_word)


    def __order_scored_words(self, scored_words: list) -> list:
        sorted_scores = sorted(scored_words, key=lambda item:(item[WORD_FIELD], -item[SCORE_FIELD]))
        return sorted_scores


    def __find_shared_node(self, prefix: str, node: NodeScoredWord) -> NodeScoredWord:
        if len(prefix) <= 0:
            return node

        char = prefix[0]
        if char not in node.children:
            return None

        search_node = node.children[char]
        pending_chars = prefix[1:]
        return self.__find_shared_node(pending_chars, search_node)


    def __get_node_leaves(self, node: NodeScoredWord) -> list[NodeScoredWord]:
        if node.scored_word:
            yield node

        for key in node.children.keys():
            child_leaves: list[NodeScoredWord] = self.__get_node_leaves(node.children[key])
            for leave in child_leaves:
                yield leave

