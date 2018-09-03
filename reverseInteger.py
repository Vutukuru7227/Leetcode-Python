class Solution(object):
    @staticmethod
    def reverse(x):
        sign = str(x)[0]
        if sign != "-":
            result = int(str(x)[::-1])
        else:
            output = sign+""+str(int(str(x)[:0:-1]))
            result = int(output)

        if result < 2147483648 and result > -2147483648:
            return result
        else:
            return 0
        return result

Solution.reverse(120)