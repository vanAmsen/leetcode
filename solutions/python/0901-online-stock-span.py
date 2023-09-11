class StockSpanner:

    def __init__(self):
         # To store (price, span) pairs
        self.stack = [] 

    def next(self, price: int) -> int:
          # Initialize span to 1, as each day is at least spanned by itself
        span = 1
        while self.stack and self.stack[-1][0] <= price:
              # Pop the top element and get its span
            _, s = self.stack.pop()
             # Add the popped span to the current span
            span += s 
         # Push the new price and its span
        self.stack.append((price, span)) 
        return span
