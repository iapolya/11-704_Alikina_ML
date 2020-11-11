import numpy as np
import pandas as pd

# ГОТОВО!
disease = pd.read_csv('disease.csv', delimiter=";")
symptom = pd.read_csv('symptom.csv', delimiter=";")
rand_symp = [np.random.randint(0, 2) for i in range(23)]

P_disease = []
for i in range(len(disease) - 1):
    P_disease.append(disease['количество пациентов'][i] / disease['количество пациентов'][len(disease) - 1])

P_dis_sympt = [1] * (len(disease) - 1)

for i in range(len(disease) - 1):
    P_dis_sympt[i] *= P_disease[i]
    for j in range(len(symptom) - 1):
        if rand_symp[j] == 1:
            P_dis_sympt[i] *= float(symptom.iloc[j + 1][i + 1])

dis_num = P_dis_sympt.index(max(P_dis_sympt))
print(disease['Болезнь'][dis_num])