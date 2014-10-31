import searcher1
import data_load
import indexer

d= indexer.process_data("raw_data.pickle","crawler1.pickle")
#print(d)
searcher1.search(d)
