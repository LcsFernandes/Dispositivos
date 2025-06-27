class ConfigurationError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'ConfigurationError'
        self.status_code = 500