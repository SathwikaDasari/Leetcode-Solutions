class Solution:
    def fairCandySwap(self, alice, bob):
        sumA = sum(alice)
        sumB = sum(bob)
        
        diff = (sumB - sumA) // 2
        setB = set(bob)
        
        for a in alice:
            if a + diff in setB:
                return [a, a + diff]