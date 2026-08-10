from collections import defaultdict
class FreqStack:

    def __init__(self):
        self.freqs_stack = defaultdict(list)
        self.vals_to_freqs = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = (self.vals_to_freqs.get(val) or 0) + 1
        self.vals_to_freqs[val] = freq
        self.freqs_stack[freq].append(val)
        self.max_freq = max(self.max_freq, freq)
    
    def pop(self) -> int:
        max_freq = self.max_freq
        val = self.freqs_stack[max_freq].pop()
        self.vals_to_freqs[val] -= 1
        if len(self.freqs_stack[max_freq]) == 0:
            self.max_freq -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()