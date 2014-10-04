import pickle
import os

# preprocess list of quotes to map each word to list of indices where they occur
word_indices={}
for i,quote in enumerate(data_list):
	words = quote.split()
	for w in words:
		if w in word_indices:
			if word_indices[w].count(i) == 0:
				word_indices[w].append(i)
		else:
			word_indices[w]=[i]


def parse_query(query_str):
	"""
	Parse query string and return the set of unique keywords and the operator
	as a tuple
	"""
	# unique keywords from query string
	keywords = dict()

	# operator used in query string
	operators = dict()

	# parse the query to save all unique keywords and operators
	for w in query_str.split():
		if w == 'or' or w == 'and':  # save operator
			if w not in operators:
				operators[w] = w
		elif w not in keywords:  # save keyword
			keywords[w] = w

	# identify the operator to be used
	op='and'
	if ('or' in operators)  and ('and' in operators): # if query has both 'or' and 'and' then its 'and'
		op = 'and'
	elif len(operators) == 0: # if query has neither 'or' or 'and' then its 'and'
		op = 'and'
	else:
		op = list( operators.keys())[0]

	return (keywords, op)

