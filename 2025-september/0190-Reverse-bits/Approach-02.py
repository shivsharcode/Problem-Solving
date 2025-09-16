class Solution:
    # APPROACH - 02: LOGICAL APPROACH
    def reverseBits(self, n: int) -> int:
        
        def decimal_to_binary(num:int) -> str:
            binarystr = ""

            while num != 0:
                rem = num % 2
                binarystr = str(rem) + binarystr
                num = num // 2

            return binarystr

        def binary_to_decimal(binarystr: str)-> int:
            e = 0
            decimalnum = 0
            for i in binarystr[::-1]:
                decimalnum += (2**e) * int(i)
                e += 1

            return decimalnum
        
        binarystr = decimal_to_binary(n)
        preceeding_zero = (32 - len(binarystr)) * '0'
        binarystr = preceeding_zero + binarystr

        rev_binarystr = binarystr[::-1]

        ans = binary_to_decimal(rev_binarystr)
        return ans


