import sys, pickle
model = pickle.load(open("model.pkl","rb"))
vals = list(map(float, sys.argv[1:]))
pred = model.predict([vals])[0]
print("Pass" if pred==1 else "Fail")
