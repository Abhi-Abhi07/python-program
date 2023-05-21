import pickle

l=[23,45,23,45]

file=open("write_pickle.txt","wb")

pickle.dump(l,file)

file.close()