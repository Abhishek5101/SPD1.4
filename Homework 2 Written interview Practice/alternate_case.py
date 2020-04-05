"""
Problem: Given a string, alternate the cases in that string.
E.g. --> altERnaTIng cAsE <=> ALTerNAtiNG CaSe
"""

"""
1. Restating the problem:
So given a string my job is to alternate its characters from lower case to
upper case and Vice Versa, right?
"""

"""
2: Ask Clarifying Questions
Will I be given just a single string? or a list of strings?
What should I do with whitespaces?
What should I do with punctuation marks?
Can I use the in built case converter function?
"""

"""
3: State Assumptions
I can use the built in upper() and lower() functions
strings are stored in memory
I leave out whitespaces as they are
I leave out punctuations as they are
"""

"""
4(a)Brainstorm Solutions
Well the simplest possible way would be just using the built in functions,
but I am assuming you would want me to create my own function.
Let's take an example. ("AppLE") we would want this to convert to ("aPPle")
I can think of two ways to solve this.
1) I could create an empty string and iterate over the original string. And each
time I go over a new character, add it's alternative case character to that new string.
2) I perform the approach except instead of appending to a string each time, I can append to a list and then
return the list as a string and if the character is neither uppercase, nor lowercase like a whitespace or
punctuation mark , I would append it as is.
"""

"""
4(b)Explain Your Rationale and 4(c) Discuss Trade-offs
I would like to choose the second approach from my two listed approaches. This is because since in python
strings are immutable, each time we append to a string it will create a new string and it quite costly memory
wise. You can append to a list in constant time and then simply return the list as a string.
This way, you wouldn't have to waste a lot of memory
Hence overall, I would only have to iterate over the string one time so my Time Complexity would be O(n)
Space complexity could be O(1)

"""

"""
4(d) Suggest Improvements
This version will work for only one string at a time. We could use the same approach to make it
work for a list of strings or a file as well.
"""


def alternate_case(string):
	solution_list = []
	for character in string:
		if character.islower():
			solution_list.append(character.upper())
		elif character.isupper():
			solution_list.append(character.lower())
		else:
			solution_list.append(character)
	return "".join(solution_list)


"""
Tests-->
"""
print(alternate_case("AppLE"))
print(alternate_case("Ap p!LE"))
print(alternate_case("A @Pp  LE5"))
print(alternate_case("altERnaTIng cAsE"))
print(alternate_case("ALTerNAtiNG CaSe"))

