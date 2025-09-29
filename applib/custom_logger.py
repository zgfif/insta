from pathlib import Path
import logging




class CustomLogger:
    def __init__(self, logpath: str = 'logs/app.log', level=logging.DEBUG) -> None:
        self._logpath = logpath
        self._level = level
        self._logger = logging.getLogger(__name__)
        self._logger.setLevel(self._level)
        self._prepare_path()



    def setup(self) -> logging.Logger:
        """
        Return logger configured with console and file handlers.
        """
        console_handler = logging.StreamHandler()

        file_handler = logging.FileHandler(filename=self._logpath, mode='a', encoding='utf-8')

        # setting level, formatter for each handler and add each handler to the logger.
        for handler in console_handler, file_handler:
            handler.setLevel(self._level)

            handler.setFormatter(self._formatter())

            self._logger.addHandler(handler)
        
        return self._logger



    def _prepare_path(self) -> None:
        """
        Create directory(s) for logfile.
        """
        Path(self._logpath).parent.mkdir(parents=True, exist_ok=True)



    def _formatter(self) -> logging.Formatter:
        """
        Return formatter for console_handler and file_handler.
        """
        return logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s",)
