from math import log, floor, pow
from collections import defaultdict
from block import Block
import matplotlib.pyplot as plt

class Strip:
    def __init__(self, W, alpha, width=1):
        self.blocks = defaultdict(list) # "height" : 
        self.blocks_seq = [] # For plotting and value of approximated solution 
        self.width = width
        self.opt_lower_bound = 0
        self.alpha = alpha
        self.W = W
        
    def get_opt_lower_bound(self):
        return self.opt_lower_bound
    
    def get_height(self):
        return sum(block.height for block in self.blocks_seq) 
        
    def insert(self, rectangle):
        rectangle.rotate()
        if rectangle.width > 1 or rectangle.height > 1:
            raise ValueError("Width and height cannot be greater than 1")
        self.opt_lower_bound += rectangle.get_area()
        bh = self._nearest_power(rectangle.height, self.alpha)
        # Check if rectangle is a buffer
        if rectangle.width >= self.W:
            self._insert_new_block(bh, rectangle)
        # Else try to find a viable block
        else: self._insert_small_rectangle(bh, rectangle)
        return 
                
    def _insert_small_rectangle(self, bh, rectangle):
        candidates = self.blocks.get(bh)
        if not candidates:
            self._insert_new_block(bh, rectangle)
        else:
            viable_block = self._find_viable_block(candidates, rectangle.width)
            if viable_block: viable_block.add_rectangle(rectangle)
            else: self._insert_new_block(bh, rectangle)
        
    def _find_viable_block(self, candidates, width):
        lowest_viable = None
        for i in range(len(candidates)-1, -1, -1):
            if 1-candidates[i].rectangle_widths < width:
                break
            if not candidates[i].get_full():
                lowest_viable = candidates[i]
        return lowest_viable
            
    def _insert_new_block(self, height, rectangle):
        b = Block(height, self.W)
        b.add_rectangle(rectangle)
        self.blocks[height] += [b]
        self.blocks_seq.append(b)
        return
        
    def _nearest_power(self, height, alpha):
        return pow(alpha, floor(log(height, alpha)))
    
    def plot_packing(self, scaling=1):
        height = self.get_height()
        fig = plt.figure(figsize=(2, max(10, height)))
        ax = fig.add_subplot(111)
        ax.set_xlim([0, 1])
        ax.set_ylim([0, height+0.1/scaling])
        ax.set_aspect('equal')
        cur_y = 0
        for idx, block in enumerate(self.blocks_seq):
            cur_x = 0
            if idx != len(self.blocks_seq)-1:
                ax.axhline(cur_y+block.height, color = 'r', linestyle = '--')
            for rectangle in block.rectangles:
                ax.add_patch(plt.Rectangle((cur_x, cur_y),
                                           rectangle.width,
                                           rectangle.height,
                                           linestyle="-",
                                           ec = "black",
                                           fc = "grey"))
                cur_x += rectangle.width
            cur_y += block.height
        plt.show()