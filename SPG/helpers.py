from rectangle import Rectangle
import random

def generate_random_rectangles(n, r=(0,1)):
    return [Rectangle(random.uniform(*r), random.uniform(*r)) for _ in range(n)]