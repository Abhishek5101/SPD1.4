"""
Question: Given a string of characters, write a function to return
the middle number in the product of each digit in the string.
"""

"""
1. Restating the problem:
If I understand this currently, you give me a string and I multiply all the numbers in that string and
return the middle number from the product.
Example: '789' -> 7, 8, 9 -> 7*8*9=504, thus 0 should be returned as an integer.
"""

"""
2. Ask Clarifying Questions
Will there be any other characters in the string, apart from numbers?
Do you want to return the middle number as an integer or a string?
What if the product is even and there is no middle number?
What if there are no numbers in the string?
"""

"""
3. State your assumptions
The string will contain all sorts of character.
I can use the built in function to check if a character is a digit
"""

"""
4(a)Brainstorm Solutions
Well we can remove all the non digit characters from the string and copy the digits to a new string.
Or we can create a new list to hold the digits that occur in the string as integers to not modify the original string.
Then we simply multiply the integer elements in the list and if the product is odd numbered, we return the middle
number, if it is even numbered, we return the middle two digits. If the list is empty, meaning there were no digits in
the input string, we return -1
"""

"""
4(b)Explain Your Rationale and 4(c) Discuss Trade-offs
I think the latter approach is better since in python strings are immutable and modifying them each time will
create a new copy. In terms of time complexity, we iterate over the string one time. And then iterate over the list
one time to multiply its elements, so it will be O(2n) which is ~ O(n)
Space complexity will be O(1)
"""

"""
4(d) Suggest Improvements
Converting back and forth from strings to ints was somewhat confusing. I should just convert the
product into a string so I can use string slicing to get the middle. Then return that as an integer.
"""


def middle_product(string):
	integers_list = []
	for character in string:
		if character.isdigit():
			integers_list.append(int(character))
	if not integers_list:
		return -1
	product = 1
	for number in integers_list:
		product *= number
	product = str(product)
	if len(product) % 2 == 0:
		return int(product[len(product)//2-1] + product[len(product)//2])
	if len(product) % 2 == 1:
		return int(product[len(product)//2])