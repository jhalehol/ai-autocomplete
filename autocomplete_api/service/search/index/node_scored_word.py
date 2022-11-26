from autocomplete_api.model.models import ScoredWord


class NodeScoredWord:

    scored_word: ScoredWord = None

    def __init__(self) -> None:
        self.children: dict = {}


    def insert(self, scored_word: ScoredWord) -> None:
        """Process the given scored word and all their chars to assign them into the trie

        Args:
            scored_word (ScoredWord): Original word already scored to insert in the trie
        """
        self.__insert_node(scored_word, None)


    def __insert_node(self, scored_word: ScoredWord, pending_chars: str) -> None:
        word = pending_chars if pending_chars is not None else scored_word.word
        # If its last char of the word, store the metadata of the scored word base
        if len(word) <= 0:
            self.scored_word = scored_word
            return 

        char = word[0]
        if char not in self.children:
            self.children[char] = NodeScoredWord()

        pending_chars = word[1:]
        self.children[char].__insert_node(scored_word, pending_chars)


    def __str__(self):
        objects_str: list = []
        for key, value in self.children.items():
             objects_str.append('{}: {}'.format(key, value))

        return str(objects_str)
