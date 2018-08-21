import pickle

d=dict(name='Bob',age='22',score='99')
pickle.dumps(d)

with open('dump.txt','wb') as f:
    pickle.dump(d,f)