import matplotlib.pyplot as plt
import numpy as np





def dd(k, x): 
    return 100 / (1 + k * x)
    # Amount = 100

parameter = np.linspace(0.1,1,4)
delay = np.linspace(0,11,100)
subject_value = []

for i in parameter:
    subject_value = []
    for d in delay:
        
        subject_value.append(dd(d,i))
    plt.plot(delay,subject_value, label = "k_value: "f"{i}")
    subject_value = []

plt.legend()
plt.title ('Delay discounting')
plt.xlabel("Delay")
plt.ylabel("Subject Value")
plt.show()