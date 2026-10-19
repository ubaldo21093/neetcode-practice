"""
Design Dynamic Array (NeetCode)

Goal: build a resizable array (like Java's ArrayList) on top of fixed-size slots.

Two numbers to keep track of the whole time:
  - size     -> how many elements you've actually put in (starts at 0)
  - capacity -> how many slots exist in total (starts at `capacity`)
  They are NOT the same thing. A brand-new array has size 0 but capacity > 0.

A Python list already grows on its own, so the point of this exercise is
to pretend it can't: pre-allocate the slots yourself and only grow them
when resize() is called.

Java -> Python reminders:
  - There is no implicit `this`. Every instance variable must be `self.something`,
    both when you set it AND when you read it.
  - Prefer `x is None` over `x == None`.
  - Fields don't get declared up top; you create them by assigning in __init__.
  - Target: every method except resize() should be O(1).
"""


class DynamicArray:
    # Requirement: create an EMPTY array (size 0) with `capacity` slots (capacity > 0).
    # Hint: besides the list itself, what other values should live on `self`
    #       so that getSize()/getCapacity() don't have to compute anything?
    # Tip: `[None] * k` gives you a list with k empty slots.
    def __init__(self, capacity: int):
        if capacity > 0:
            self.ubiarray = []
            self.size = 0
            self.capacity = capacity
            self.ubiarray += [None] * capacity

    # Requirement: return the element at index i. You can assume i is valid.
    def get(self, i: int) -> int:
        return self.ubiarray[i]

    # Requirement: overwrite the element at index i with n. You can assume i is valid.
    # Hint: what does `self[i]` refer to? Is `self` the list, or the object holding it?
    # Hint: since i is guaranteed valid, do you need the bounds check at all?
    def set(self, i: int, n: int) -> None:
            self.ubiarray[i] = n

    # Requirement: put n at the end (the next free slot) and grow the size by 1.
    #              If the array is FULL, call resize() first, then add n.
    # Hint: describe "full" using only size and capacity. Can capacity ever be < 0?
    # Hint: if you already pre-made the slots, should you be appending, or filling a slot?
    # Hint: resize() is a method on your class, not on the Python list.
    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()
            self.pushback(n)
        else:
            for i in range(0,self.getCapacity()):
                if self.ubiarray[i] == None:
                    self.ubiarray[i] = n
                    self.size +=1 
                    break
                else:
                    i += 1

    # Requirement: remove and return the last element. Assume the array isn't empty.
    #              Capacity does NOT shrink, only size does.
    # Hint: which index holds the last *real* element? (Think in terms of size.)
    # Hint: what has to be updated after you take it out?
    # Note: Python lists don't have a .getsize() method.
    def popback(self) -> int:
        temp = self.ubiarray[self.getSize() - 1]
        if temp != None:
            self.size -= 1
        self.ubiarray[self.getSize()] = None
        return temp

    # Requirement: double the capacity and keep every existing element in place.
    # Hint: two options: build a new list of the bigger size and copy over,
    #       or extend the current list with more empty slots.
    # Hint: look at the while condition. Is there a value where it ever becomes False?
    # Hint: inside a method, `ubiarray` and `self.ubiarray` are different names.
    # Hint: once capacity changes, what else needs updating?
    def resize(self) -> None:
        growth = self.capacity
        self.ubiarray += [None] * growth
        self.capacity += growth

    # Requirement: return how many elements are in the array (O(1)).
    # Hint: with pre-made slots, is len(list) the size or the capacity?
    def getSize(self) -> int:
        return self.size

    # Requirement: return the total number of slots (O(1)).
    # Hint: counting None's gives you the *free* slots, not the total.
    #       What happens when the array is full, or when someone stores None?
    # Hint: where does `count = 0` sit relative to the loop? What does that do each pass?
    def getCapacity(self) -> int:
        return self.capacity
