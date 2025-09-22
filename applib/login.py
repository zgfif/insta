class Login:
    def __init__(self, driver: WebDriver, username: str, password: str) -> None:
        self._driver = driver
        self._username = username
        self._password = password


    def perform(self) -> None:
        pass