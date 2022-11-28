


class ApplicationConfiguration:

    default_language: str
    default_language_path: str
    default_suggestion_limit: int
    max_results: int

    def __init__(self) -> None:
        pass
    

class ScoredWord:

    def __init__(self, word: str, score: int) -> None:
        self.word = word
        self.score = score
