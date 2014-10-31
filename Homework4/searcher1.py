from datetime import datetime
import shelve
import urllib.request
import json
from pprint import pprint

def parse_query(query_str):
	"""
	Parse query string and return the set of unique keywords and the operator
	as a tuple
	"""
	# unique keywords from query string
	keywords = set()

	# operator used in query string
	operators = set()

	# parse the query to save all unique keywords and operators
	for w in query_str.split():
		if w == 'or' or w == 'and':  # save operator
			if w not in operators:
				operators= {w}|operators
		elif w not in keywords:  # save keyword
			keywords= {w}|keywords

	# identify the operator to be used
	op='and'
	if(len(operators)!=0 and 'and' not in operators):
		op = 'or'
	return (keywords, op)
def search(query):
	dict1=shelve.open(query)
	# read query string from user
	query_str=input('query:')

	page = urllib.request.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+str(query_str))
	content=page.read()
	content_string = content.decode("utf-8")

	json_data = json.loads(content_string)
	if(json_data['cod']!='404'):
		print(json_data['weather'])
	else:
		pass

	# parse all keywords and the operator
	(keywords, op) = parse_query(query_str)

	print("Performing " + op + " search for: " + str(list(keywords)) + "\n")

	# mark start time of execution
	dt1 = datetime.now()
	result =set()
	if op == 'or':     # we processs when operator is 'or'
		for key in keywords:
			if key in dict1.keys():   # if a single keyword is found then there is a match
				result=result|dict1[key]
				#print(result)
	else:              # we processs when operator is 'and'
		one =keywords.pop()
		if(one in dict1.keys()):
			result=dict1[one]
		else:
			return
		for key in keywords:
			if key not in dict1.keys():  # if a single keyword is not found then there is a mismatch
				return
			else:
				result=result&dict1[key]
	#print(result)
	if (len(result)>=1):
		for i in result:
			print("Found at ", i)

	# mark end time of execution
	dt2= datetime.now()
	# display execution time
	time1=(dt2.microsecond-dt1.microsecond)
	print("\nExecution time:", time1)