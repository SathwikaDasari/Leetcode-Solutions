class Solution(object):
    def totalNumbers(self, digits):
        unique = set()
        n = len(digits)

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and i != k and j != k:
                        if digits[i] != 0:
                            if digits[k] % 2 == 0:
                                num = digits[i]*100+digits[j]*10+digits[k]
                                unique.add(num)


        return len(unique)