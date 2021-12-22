# Stack

```python
class Stack:
    def __init__(self,arr):
        self.arr = arr
        self.top = -1
        
    def push(self, n):
        self.top += 1
        self.arr[self.top] = n
        
    def pop(self):
        if not self.is_empty():
	        self.top -= 1
    	    return self.arr[self.top + 1]
    	else:
            return IndexError
        
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def peek(self):
        return self.arr[self.top]
```

