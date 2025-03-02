import math
import time
def delayed_square_root(number, milliseconds):
    time.sleep(milliseconds / 1000)
    return math.sqrt(number)