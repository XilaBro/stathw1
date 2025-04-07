import math
import numpy as np
kb = 1.38*10**(-23)

# z1 = 1+ 3*math.exp(-1)+5*math.exp(-2)

# p1 = 1/ z1
# p2 = 3*math.exp(-1)/ z1
# p3 = 5*math.exp(-2)/z1

# print(z1)
# avge1 = 0
# avge2 = 300 *p2
# avge3 = 600*p3

# print(avge1)
# print(avge2)
# print(avge3)
# print(avge2+avge3)

# e = 1.4*10**(-23)
# z1 = 1+ math.exp(-e/kb)+math.exp(-(2*e)/kb)

# p1 = 1/ z1
# p2 = math.exp(-e/kb) / z1
# p3 = math.exp(-(2*e)/kb) / z1
# print(z1)
# print(p1)
# print(p2)
# print(p3)


# mp = 1.67262192 * 10**(-27)
# mn = 1.67492749804 * 10**(-27)

# m235 = 92*mp + 143*mn + 6*(9*mp+10*mn)
# m238 = 92*mp + 146*mn + 6*(9*mp+10*mn)
# kb = 1.38*10**(-23)
# T = 300
# V235 = ((T*kb*3)/m235)**(0.5)
# V238 = ((T*kb*3)/m238)**(0.5)
# DV = V235 - V238
# print(V235)
# print(V238)

# print(DV)


# ### Q1
#Conditions
etot = 7
possible_combos = []

#For loop to find every combination (Brute Force)
for a in range(0,9):
    for b in range(0,9):
        for c in range(0,9):
            for d in range(0,9):
                for e in range(0,9):
                    for f in range(0,9):
                        for g in range(0,9):
                            for h in range(0,9):
                                result = a*7 + b*6 + c*5 + d*4 + e*3 + f*2 + g*1 + h*0
                                num_of_part = a+b+c+d+e+f+g+h
                                if result == etot and num_of_part==8: #checks if the two conditions are met
                                    possible_combos.append([a,b,c,d,e,f,g,h]) #adds valid combinations to list
 #print(possible_combos)

def multi(list,particles): #function to calculate multiplicity
    result = math.factorial(particles)
    index = 0
    for i in list[::-1]:
        if i != 0:
            result = result / math.factorial(i)
            
        index += 1  
    return result

#Calculates multiplicity
wk = []
for element in possible_combos:
    wk.append(multi(element,8))

 # print("the list",wk)
 # print("sum of wk",sum(wk))

#Calculates probablity
prob = []
for i in wk:
    prob.append(i/sum(wk))

#Converting to np arrays because more versitile
prob = np.array(prob)
possible_combos= np.array(possible_combos).T

#print(possible_combos)
#Finding the average position of particles. this first part is getting the total percentage to be used to find the actual average position
avg_position = []
for index in range(8):
    avg_position.append(np.dot(prob,possible_combos[index]))

#putting it all together into one matrix
complete_matrix = np.vstack([possible_combos,wk])
complete_matrix = np.vstack([complete_matrix,prob])

a = np.append(avg_position,[0,0])
a = a.reshape(-1,1)
b =np.append(avg_position,[0,0])/np.sum(avg_position)
b =b.reshape(-1,1)
complete_matrix = np.hstack([complete_matrix,a])
complete_matrix = np.hstack([complete_matrix,b])
#Exports to CSV file
np.savetxt("Q1.csv", complete_matrix, delimiter=",", fmt="%4f")

#Q1.D
etot = 6
possible_combos2 = []
for a in range(0,9):
    for b in range(0,9):
        for c in range(0,9):
            for d in range(0,9):
                for e in range(0,9):
                    for f in range(0,9):
                        for g in range(0,9):
                            for h in range(0,9):
                                result = a*7 + b*6 + c*5 + d*4 + e*3 + f*2 + g*1 + h*0
                                num_of_part = a+b+c+d+e+f+g+h
                                if result == etot and num_of_part==8:
                                    possible_combos2.append([a,b,c,d,e,f,g,h])

wk2 = []
for element in possible_combos2:
    wk2.append(multi(element,8))

#Calculated entropy via stephen boltzman
S1 = kb*math.log(sum(wk))
S2 = kb*math.log(sum(wk2))
ds = S1-S2
print(ds)


#Q3

etot = 6
classical = []
for d in range(0,9):
    for e in range(0,9):
        for f in range(0,9):
            for g in range(0,9):
                for h in range(0,9):
                    result = d*4 + e*3 + f*2 + g*1 + h*0
                    num_of_part = d+e+f+g+h
                    if result == etot and num_of_part==3 and d <=2 and e <=1 and f <=2 and g <=3 and h <=2:
                        classical.append([d,e,f,g,h])

classwk = []
for element in classical:
    classwk.append(multi(element,3))

classprob = []
for i in classwk:
    classprob.append(i/sum(classwk))

classprob = np.array(classprob)
classical= np.array(classical).T

classavg_position = []
for index in range(5):
    classavg_position.append(np.dot(classprob,classical[index]))

complete_matrix_class = np.vstack([classical,classwk])
complete_matrix_class = np.vstack([complete_matrix_class,classprob])

a = np.append(classavg_position,[0,0])
a = a.reshape(-1,1)
b =np.append(classavg_position,[0,0])/np.sum(classavg_position)
b =b.reshape(-1,1)
complete_matrix_class = np.hstack([complete_matrix_class,a])
complete_matrix_class = np.hstack([complete_matrix_class,b])

np.savetxt("Classical.csv", complete_matrix_class, delimiter=",", fmt="%4f")

etot = 6
fermi = []
for d in range(0,9):
    for e in range(0,9):
        for f in range(0,9):
            for g in range(0,9):
                for h in range(0,9):
                    result = d*4 + e*3 + f*2 + g*1 + h*0
                    num_of_part = d+e+f+g+h
                    if result == etot and num_of_part==3 and d <=1 and e <=1 and f <=1 and g <=1 and h <=1:
                        fermi.append([d,e,f,g,h])
            


fermiwk = []
for element in fermi:
    fermiwk.append(multi(element,3))

fermiprob = []
for i in fermiwk:
    fermiprob.append(i/sum(fermiwk))

fermiprob = np.array(fermiprob)
fermi= np.array(fermi).T


fermiavg_position = []
for index in range(5):
    fermiavg_position.append(np.dot(fermiprob,fermi[index]))

complete_matrix_fermi = np.vstack([fermi,fermiwk])
complete_matrix_fermi = np.vstack([complete_matrix_fermi,fermiprob])

a = np.append(fermiavg_position,[0,0])
a = a.reshape(-1,1)
b =np.append(fermiavg_position,[0,0])/np.sum(fermiavg_position)
b =b.reshape(-1,1)
complete_matrix_fermi = np.hstack([complete_matrix_fermi,a])
complete_matrix_fermi = np.hstack([complete_matrix_fermi,b])
print(complete_matrix_fermi)

np.savetxt("fermi.csv", complete_matrix_fermi, delimiter=",", fmt="%4f")