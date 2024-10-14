# 1. Check Palindrome is valid or not.

```
def is_palindrome(s: str) -> bool:
    
    str1 = ''.join(char.lower() for char in s if char.isalnum())
    return str1 == str1[::-1]
print(is_palindrome("A man, a plan, a canal: Panama")) 
print(is_palindrome("race a car"))
print(is_palindrome(" right to now"))     
```
Output:- True
         False
         False
# 2. Find Majority of Element 

```
def majority_element(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num 
            count = 1        
        elif num == candidate:
            count += 1       
        else:
            count -= 1       
    return candidate 
nums = [3,1,2,3,1,1,4]
print(majority_element(nums))
```
Output:- 1

# 3. stock Maximum profit.

```
def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit
#prices = [7, 1, 5, 3, 6, 4]
prices= [2 , 7, 1, 5]
print(maxProfit(prices)) 
```
Output:- 5