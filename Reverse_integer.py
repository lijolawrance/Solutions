class Solution:
    def reverse(self, x: int) -> int:
        if (x >= 0):
            my_num = str(x)
            return_val = int(my_num[::-1])
        else:
            my_num = str(abs(x))
            return_val = int("-" + my_num[::-1])
        if return_val in range(-2147483647, 2147483647):
            return return_val
        else:
            return 0
