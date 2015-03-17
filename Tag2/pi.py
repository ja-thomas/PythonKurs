import numpy as np

x = np.random.random_sample(100000)
y = np.random.random_sample(100000)

d = np.sqrt(x**2+y**2)

hits = len([element for element in d if element <= 1])

pi_est = (hits / 100000.0) * 4.0


print "Pi estimation is:", pi_est
