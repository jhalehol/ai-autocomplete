

SUGGESTED_WORDS = ['mock1', 'mock2', 'mock3']

class SearchServiceMock:

    def __init__(self) -> None:
        pass
        
    def search(self, prefix: str, limit: int) -> list:
        return SUGGESTED_WORDS
