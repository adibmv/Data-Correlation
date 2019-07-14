#python3
#program mencari korelasi dengan python
import numpy as np
import math

def mean(a):
	jml=0
	for i in range(len(a)):
		jml=jml+a[i]
	hasil=jml/len(a)
	return hasil
def correl(a,b):
	if(len(a)!=len(b)):
		print("jumlah data harus sama!")
	else:
		ma=mean(a)
		mb=mean(b)
		hasila=0
		amin2=0
		bmin2=0
		for i in range(len(a)):
			rumusa=(a[i]-ma)*(b[i]-mb)
			hasila=hasila+rumusa
		for i in range(len(a)):
			amin=(a[i]-ma)**2
			bmin=(b[i]-mb)**2
			amin2=amin2+amin
			bmin2=bmin2+bmin
		korelasi=hasila/math.sqrt(amin2*bmin2)
		return korelasi
alice = np.loadtxt("alice.csv")
bob = np.loadtxt("bob.csv")
kor=correl(alice,bob)