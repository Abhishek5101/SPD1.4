"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false

{'e': {a}, 'g': {d}}
{'f': [b], 'o'[b, a]}
"""


# def is_isomorphic(word1, word2):
# 	if len(word1) != len(word2):
# 		return False
# 	ans_dict = {}
# 	for index in range(len(word1)):
# 		ans_dict[word1[index]] = []
#
# 	for index in range(len(word1)):
# 		ans_dict[word1[index]] += [word2[index]]
#
# 	for k, v in ans_dict.items():
# 		ans_dict[k] = set(v)
#
# 	for key, value in ans_dict.items():
# 		if len(key) != len(value):
# 			return False
#
# 	return True


def fibonacci_1000():
	fib = [0, 1]
	keepgoing = True
	while keepgoing:
		new_term = fib[-1] + fib[-2]
		fib.append(new_term)
		str_new_term = str(new_term)
		if len(str_new_term) > 1000:
			return fib.index(new_term)


print(fibonacci_1000())
