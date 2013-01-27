# A palindromic number reads the same both ways. The largest palindrome made from the 
# product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def find_palindrome():
    max_pal = 0
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            prod = i * j
            if (prod > max_pal):
                prod_str = str(prod)
                reverse_str = prod_str[::-1]
                if (prod_str == reverse_str):
                    max_pal = prod    
    
    return max_pal

print find_palindrome()

