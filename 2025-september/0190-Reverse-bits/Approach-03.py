class Solution:
    # APPROACH - 03 (BIT MANIPULATION) - OPTIMAL FOR INTERVIEW
    def reverseBits(self, n: int) -> int:
        
        reverse_binary = 0

        for _ in range(32):
            lastbit = n & 1    # gives the last bit of bin(n)

            reverse_binary = reverse_binary << 1    # left shift  (shift everything left), adds a zero bit in the last

            reverse_binary = reverse_binary | lastbit    # since the last bit of reverse_binary  is zero due to left shift, this will replace that with the lastbit of bin(n)

            # shifting n right, so as to remove bit from last
            n = n >> 1

        return reverse_binary