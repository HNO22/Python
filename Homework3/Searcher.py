from data_load import data_list
from datetime import datetime




# =====================  First Iteration (Simple Algorithm) ======================
print("First Iteration (quotes are stored in the list, the search uses \"in\" keyword)")

# read query string from user
query_str=input('query:')

# parse all keywords and the operator
(keywords, op) = parse_query(query_str)

print("Performing " + op + " search for: " + str(list(keywords.keys())) + "\n")

# mark start time of execution
dt1 = datetime.now()

for i,quote in enumerate(data_list):
	words = quote.split()
	found = True
	if op == 'or':     # we processs when operator is 'or'
		found = False
		for key in keywords.keys():
			if words.count(key) > 0:   # if a single keyword is found then there is a match
				found = True
				break
	else:              # we processs when operator is 'and'
		found = True
		for key in keywords.keys():
			if words.count(key) == 0:  # if a single keyword is not found then there is a mismatch
				found = False
				break
	if found:
		print("Found at ", i, quote[:80])

# mark end time of execution
dt2= datetime.now()
# display execution time
time1=(dt2.microsecond-dt1.microsecond)
print("\nExecution time:", time1)


# =====================  Second Iteration (Improved Algorithm) ======================
print("\nSecond Iteration (added dictionary that maps each word to a set of indices of quotes where the word was found)")

# read query string from user
query_str=input('query:')

# parse all keywords and the operator
(keywords, op) = parse_query(query_str)

print("Performing " + op + " search for: " + str(list(keywords.keys())))

# mark start time of execution
dt1 = datetime.now()

if op == 'or':
	lines=set()
	for key in keywords:
		if key in word_indices:
			indices = word_indices[key]
			lines=lines.union(set(indices))
	for i in sorted(lines):
		print("Found at ", i, data_list[i][:80])
else:
	lines=set()
	for key in keywords:
		if key in word_indices:			
			indices=word_indices[key]
			if len(lines) == 0:
				lines=set(indices)
			else:
				lines=lines.intersection(set(indices))
		else:
			lines=set()
			break
	#print(lines)
	for i in sorted(lines):
		print("Found at ", i, data_list[i][:80])


# mark end time of execution
dt2= datetime.now()
# display execution time
time2=(dt2.microsecond-dt1.microsecond)
print("\nExecution time:", time2)

# print observation
if time1 > time2:
	print("Second iteration works faster then First Iteration")
else:
	print("Second iteration works slower then First Iteration")
