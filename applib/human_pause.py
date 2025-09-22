import random
from time import sleep


def human_pause() -> None:
    """
    Human pause 1 .. 11 seconds.
    """
    seconds = random.random() * 12
    print(f'waiting {seconds}...')
    sleep(seconds)
