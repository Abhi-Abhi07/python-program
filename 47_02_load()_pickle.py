import pickle

file=open("write_pickle.txt","rb")

l=pickle.load(file)

print(l)

file.close()