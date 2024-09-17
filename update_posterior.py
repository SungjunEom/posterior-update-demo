import matplotlib.pyplot as plt
import numpy as np

a = np.linspace(0,1,50) # Prior probability from population.
b_a = 0.8 # Likelihood of b given a; Likelihood of positive test given a.
b_na = 0.4 # Likelihood of b given not a; Likelihood of positive test given not a.
a_record = []

for i in range(1,20):
    a = (b_a) * a / (b_a * a + b_na * (1 - a))
    a_record.append(a)
    
a_record = np.array(a_record)
print(a_record)
for i in range(50):
    plt.plot(a_record[:,i], label="")
plt.xlabel("iterations (num. of independent positivie test)")
plt.ylabel("posterior probability")
plt.show()

#####################################################

a = 0.5 # Prior probability from population.
b_a = np.linspace(0,1,50) # Likelihood of b given a; Likelihood of positive test given a.
b_na = 0.4 # Likelihood of b given not a; Likelihood of positive test given not a.
a_record = []

for i in range(1,20):
    a = (b_a) * a / (b_a * a + b_na * (1 - a))
    a_record.append(a)
    
a_record = np.array(a_record)
print(a_record)
for i in range(50):
    plt.plot(a_record[:,i], label="")
plt.xlabel("iterations (num. of independent positivie test)")
plt.ylabel("posterior probability")
plt.show()

###########################################

a = 0.5 # Prior probability from population.
b_a = 0.8 # Likelihood of b given a; Likelihood of positive test given a.
b_na = np.linspace(0,1,50) # Likelihood of b given not a; Likelihood of positive test given not a.
a_record = []

for i in range(1,20):
    a = (b_a) * a / (b_a * a + b_na * (1 - a))
    a_record.append(a)
    
a_record = np.array(a_record)
print(a_record)
for i in range(50):
    plt.plot(a_record[:,i], label="")
plt.xlabel("iterations (num. of independent positivie test)")
plt.ylabel("posterior probability")
plt.show()