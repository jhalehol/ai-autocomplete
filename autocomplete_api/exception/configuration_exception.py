
class ConfigurationException(Exception):

    def __init__(self, message) -> None:
        super(ConfigurationException).__init__()
        self.message = message
