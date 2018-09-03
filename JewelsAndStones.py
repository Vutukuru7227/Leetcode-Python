class Solution(object):
    @staticmethod
    def numJewelsInStones(J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        lj = list(J)
        count = 0
        for item in S:
            if(item in lj):
                count += 1
        return count

print(Solution.numJewelsInStones("aA", "bbBB"))

