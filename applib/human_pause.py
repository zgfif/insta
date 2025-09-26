import random
from time import sleep


def human_pause(a: int|float = 0, b: int|float = 1) -> None:
    """
    Human pause random seconds in a .. b seconds. Default: a = 0, b = 1.
    """
    seconds = random.uniform(a, b) 
    sleep(seconds)
