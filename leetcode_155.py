#Leetcode 155 - Min Stack


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.current_minimums = []


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.current_minimums.append(self.current_minimums[-1] if self.current_minimums and self.current_minimums[-1] < val else val)
        self.stack.append(val)
     

    def pop(self):
        """
        :rtype: None
        """
        # popped_item = self.stack[-1]
        del self.stack[-1]
        del self.current_minimums[-1]
        # return popped_item


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.current_minimums[-1]
