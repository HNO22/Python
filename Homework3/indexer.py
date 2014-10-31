import pickle
import shelve

# preprocess list of quotes to map each word to list of indices where they occur
def process_data(info):
	word_indices={}
	f=open(info,"br")
	reading_list= pickle.load(f)
	for t1 in reading_list:
		f1=open(t1[0])
		data_list=f1.read()
		a= data_list.split()
		for word in a:
			if word in word_indices.keys():
				word_indices[word]=word_indices[word]|{t1[0]}
			else:
				word_indices[word]= {t1[0]}
		f1.close()

	f.close()
	#print(word_indices)

	a="fortunes_shelve"
	s=shelve.open(a)
	for key, value in word_indices.items():
		s[key]= value
	
	s.close()

	return a

#process_data("raw_data.pickle")
