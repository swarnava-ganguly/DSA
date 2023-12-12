# Leetcode - https://leetcode.com/problems/rotate-array/description/
# Solution 1 (Brute Force) Complexity O(N^2)
# ===========================================
#   for each element in the array, run another loop from 1 to N to check the occourance of that number in touter loop of the array.
#   If the occourance is zero then return that number which is missing from array

# Solution 2 (Better) Complexity O(2N)
# ===========================================
#   using hashing, will run a loop from 1 to N, for each element in the given array, we will store the frequency in the hash array.
#   After that, for each number between 1 to N, we will check the frequencies. And for any number, if the frequency is 0, we will return it.

# Solution 3 (optimal using sum of n natural number) Complexity O(N)
# ==================================================================
#   find the sum of n natural number ir. n(n+1)//2 and sum of all the elements in the array.
#   Substract "the sum of n natural number" and sum of all the elements in the aray

# Solution 4 (Optimal using XOR) Complexity O(N) 
# (slightly better than above as if upperbound is 10^5 , sum methord evaluate 10^10 which int cannot hold. Long can be useful. But XOR will never cross 10^5)
# ==================================================================
#   Two important properties of XOR are the following:
#   XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
#   XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2
#   Now, let’s XOR all the numbers between 1 to N.
#   xor1 = 1^2^…….^N
#   Let’s XOR all the numbers in the given array.
#   xor2 = 1^2^……^N (contains all the numbers except the missing one).
#   Now, if we again perform XOR between xor1 and xor2, we will get:
#   xor1 ^ xor2 = (1^1)^(2^2)^……..^(missing Number)^…..^(N^N)
#   Here all the numbers except the missing number will form a pair and each pair will result in 0 according to the XOR property. The result will be = 0 ^ (missing number) = missing number (according to property 2).


def missingNumber(a, N):
    xor1 = 0
    xor2 = 0

    for i in range(N - 1):
        xor2 = xor2 ^ a[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number


def main():
    N = 5
    a = [1, 2, 4, 5]
    ans = missingNumber(a, N)
    print("The missing number is:", ans)


if __name__ == '__main__':
    main()