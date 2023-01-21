import math
import sys
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
print("C- orbit circumference [km]\nP- period of orbit [s]")

G=1.327*10**11 

def mass_of_black_hole (C,P):
    mass=C**3/(2*math.pi*G*(P**2))
    return mass
    print("Mass of black hole is"+str(mass))

# C=float(input("C: "))
# P=float(input("P: "))

# result=mass_of_black_hole(C,P)
# print("Mass of black hole is "+str(result)+" solar mass")

orb_1=1*10**5
orb_2=3*10**5
orb_3=5*10**5
orb_4=7*10**5

t_1=200
t_2=400
t_3=600
t_4=800
t_5=1000

data_1=[(orb_1,t_1),(orb_1,t_2),(orb_1,t_3),(orb_1,t_4),(orb_1,t_5)]
data_2=[(orb_2,t_1),(orb_2,t_2),(orb_2,t_3),(orb_2,t_4),(orb_1,t_5)]
data_3=[(orb_3,t_1),(orb_3,t_2),(orb_3,t_3),(orb_3,t_4),(orb_1,t_5)]
data_4=[(orb_4,t_1),(orb_4,t_2),(orb_4,t_3),(orb_4,t_4),(orb_1,t_5)]

data_set=[]
data_set2=[]
data_set3=[]
data_set4=[]
for d in data_1:
    res=mass_of_black_hole(*d)
    data_set.append(res)
for d in data_2:
    res=mass_of_black_hole(*d)
    data_set2.append(res)
for d in data_3:
    res=mass_of_black_hole(*d)
    data_set3.append(res)
for d in data_4:
    res=mass_of_black_hole(*d)
    data_set4.append(res)



print(data_set2)


# plt.plot([t_1, t_2, t_3, t_4],data_set)
# plt.ylabel('some numbers')
# plt.show()

# fig,ax= plt.subplots()
# plt.plot([t_1, t_2, t_3, t_4],data_set)
# plt.show()

df=pd.DataFrame(
    {'okres_orbity':[t_1, t_2, t_3, t_4,t_5],'masa1':data_set,'masa2':data_set2,
    'masa3':data_set3,'masa4':data_set4 }
)

ax=plt.gca()
df.plot(kind='line',x='okres_orbity',y='mass1',ax=ax)
df.plot(kind='scatter',x='okres_orbity',y='mass2',color='red',ax=ax)
df.plot(kind='line',x='okres_orbity',y='mass3',color='green',ax=ax)
df.plot(kind='line',x='okres_orbity',y='mass4',color='orange',ax=ax)
plt.grid()
# plt.xscale("log")

plt.show()