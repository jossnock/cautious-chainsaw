import time

#Converts a positive number to a binary represented as a list of 0s and 1s.
#using the algorithm of divide by 2 and put the remainder in the small column then start again with the quotient as input
def pos_dec_to_binary(decimal,bit_list):
    if decimal<=1:
        bit_list.append(decimal%2)
        return list(reversed(bit_list))
    else:
        bit_list.append(decimal%2)
        return pos_dec_to_binary(decimal//2,bit_list)
    
def countdown(number):
    #base case
    if number<=0:
        return
    #recursion case
    else:
        print(number)
        time.sleep(1)
        countdown(number-1)

def fibonacci(n):
    #base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #recursive case: the fibonacci number is the sum of the previous 2
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def triangular(n):
    #base case
    if n == 1:
        return 1
    #recursive case
    else:
        return n + triangular(n-1)

def factorial(input_number):
    #base case
    if input_number == 1:
        return 1
    #recursive case
    else:
        return input_number*factorial(input_number-1)

def is_palendromic(string):
    #filter out whitespace and makes all characters lowercase
    string=string.replace(' ','')
    string=string.lower()
    #find string length
    end_letter_pos = len(string)-1
    #base case
    if end_letter_pos == 0:
        return "It is a palendrome"
    if string == '':
        return "It is a palendrome"
    if string == "It is a palendrome":
        return "It is a palendrome"
        #recursive case
    elif string[0]==string[end_letter_pos]:
        string=string.replace(string[0],'')
        string=' '.join(list(reversed(string)))
        string=string.replace(' ','')
        string=string.replace(string[0],'')
        string=' '.join(list(reversed(string)))
        string=string.replace(' ','')
        return is_palendromic(string)
        
    else: 
        return "It isn't a palendrome"

#try to complete a recursive linear search, returning the index of the item, or -1
def linear_search_recursive(items, start_index, end_index, search_item):
    #base cases
    #recursive case:

    pass


def binary_search_recursive(items, start_index, end_index, search_item):
  """ a recursive binary search, returning the index of the item, or -1 if not in list. 
  The start index should be 0 and the end index should be 1 less than the length of the list."""
  # base case 1: item not in list
  # TODO use start_index and end_index to find out if the sublist is of size 0 or less and return appropriate int
  #if ______:
  #  return _____
  # TODO work out middle index of the sublist
  # middle_index = 
  # TODO from that, set current item
  #current_item = 
  # TODO base case 2: find out if current item is the search item and return the appropriate index
  # recursive cases: do a BS on a subset of the list by tweaking appropriate start or end index
  #if current_item < search_item:
  #  return binary_search_recursive(items, ????????????, ????????????, search_item)
  #else:
  #  return binary_search_recursive(items, ????????????, ????????????, search_item)
  pass

"""EXTENSION: Euclid's algorithm. The greatest common divisor (gcd) of two positive integers is the largest integer
that divides evenly into both of them. For example, the gcd(102, 68) = 34.
We can efficiently compute the gcd using the following property, which holds for positive integers p and q:

If p > q, the gcd of p and q is the same as the gcd of q and p % q."""

#tests
#print (fibonacci(8))
#countdown(10)
#print(triangular(6))
#print (factorial(5))
print(is_palendromic("yelloolley"))

#print(pos_dec_to_binary(1234,[]))
##or, neater (using a generator expression (outside scope of A-level CS))
#print("".join(str(i) for i in pos_dec_to_binary(1234,[])))
#print(binary_search_recursive([1,2,3,4,54,56,58],0,6,1))







