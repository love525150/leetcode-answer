class Solution(object):

    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = -1
        result = 0
        while i >= -len(s):
            current = s[i]
            before = None
            if i > -len(s):
                before = s[i - 1]
            
            value, dealNum = self.deal(before, current)
            result += value
            i -= dealNum
        
        return result

    def deal(self, before, current):
        if current == "I":
            return self.mapping[current], 1
            
        if current == "V":
            if before == "I":
                return self.mapping[current] - self.mapping[before], 2
            return self.mapping[current], 1

        if current == "X":
            if before == "I":
                return self.mapping[current] - self.mapping[before], 2
            return self.mapping[current], 1

        if current == "L":
            if before == "X":
                return self.mapping[current] - self.mapping[before], 2
            return self.mapping[current], 1

        if current == "C":
            if before == "X":
                return self.mapping[current] - self.mapping[before], 2
            return self.mapping[current], 1

        if current == "D":
            if before == "C":
                return self.mapping[current] - self.mapping[before], 2
            return self.mapping[current], 1

        if current == "M":
            if before == "C":
                return self.mapping[current] - self.mapping[before], 2
            return self.mapping[current], 1
