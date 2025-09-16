class Solution:
    # APPROACH-01: PYTHONIC APPROACH
    def reverseBits(self, n: int) -> int:
        
        binary_num = bin(n)
        binary_num = binary_num[2:]   # removing the preceeding '0b' string

        preceeding_zero = (32 - len(binary_num)) * '0'     #  making the binary string 32 bit

        binary_num = preceeding_zero + binary_num

        reverse_bin = binary_num[::-1]
        return int(reverse_bin, 2)