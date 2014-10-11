import searcher
import data_load
import indexer

d= indexer.process_data(data_load.data_list)
searcher.search(d)
