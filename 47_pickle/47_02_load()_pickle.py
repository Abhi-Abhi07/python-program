import pickle

file=open("47 write_pickle.txt", "rb")

l=pickle.load(file)

print(l)

file.close()