from strip import Strip 
from helpers import generate_random_rectangles

if __name__ == "__main__":
    r = (0.01,0.22)
    n = 50
    rectangles = generate_random_rectangles(n, r=r)
    strip = Strip(1/4, 2/3)
    for rectangle in rectangles:
        strip.insert(rectangle)
        
    strip.plot_packing()

    print(f"Lower bound on height: {strip.get_opt_lower_bound()}")
    print(f"Height produced by the algorithm: {strip.get_height()}")
