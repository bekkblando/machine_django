import sys
import os
import pickle
sys.path.append(os.path.join(os.path.dirname(__file__), 'machinedjango'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "machinedjango.settings")
from django.conf import settings
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from learndjango.models import Graph

ground_cricket_data = {"Chirps/Second": [20.0, 16.0, 19.8, 18.4, 17.1, 15.5, 14.7,
                                         15.7, 15.4, 16.3, 15.0, 17.2, 16.0, 17.0,
                                         14.4],
                       "Ground Temperature": [88.6, 71.6, 93.3, 84.3, 80.6, 75.2, 69.7,
                                              71.6, 69.4, 83.3, 79.6, 82.6, 80.6, 83.5,
                                              76.3]}
df = pd.DataFrame(ground_cricket_data)
chirp = np.array(ground_cricket_data["Chirps/Second"]).reshape(15,1)
ground_temp = np.array(ground_cricket_data["Ground Temperature"]).reshape(15,1)

regr1 = linear_model.LinearRegression()
regr1.fit(ground_temp, chirp)
print(regr1.score(ground_temp, chirp))
plt.scatter(ground_temp, chirp,  color='black')
plt.plot(ground_temp, regr1.predict(ground_temp), color='blue', linewidth=3)
filename = "figure.png"
path = "learndjango/static/"
fullpath = os.path.join(path, filename)
plt.savefig(fullpath)
equation = pickle.dumps(regr1)
newg = Graph.objects.create(title="Crickets", fitequation=equation, image="/learndjango/static/figure.png")


newg.save()
