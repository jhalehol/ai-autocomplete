

SUGGESTED_WORDS = ['mock1', 'mock2', 'mock3']

class SearchServiceMock:

    def __init__(self, exception = None) -> None:
        self.exception = exception


    def search(self, prefix: str, limit: int) -> list:
        if self.exception:
            raise self.exception
            
        return SUGGESTED_WORDS
