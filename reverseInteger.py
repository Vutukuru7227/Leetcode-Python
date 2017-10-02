class Solution(object):
    def reverse(self, x):
        input_to_str = str(x)
        input_sign = str[0]
        input_str_int =  str[1:]
        str_int_reverse = input_str_int[::-1]
        result_string = input_sign+""+str_int_reverse
        result = int(result_string)
        print(result)


def main():
    sln = Solution
    sln.reverse(-123)


if __name__ == '__main__':
    main()