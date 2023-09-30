import pickle

l=[23,45,23,45]

file=open("47 write_pickle.txt", "wb")

pickle.dump(l,file)

file.close()