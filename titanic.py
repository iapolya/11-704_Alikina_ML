import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# возраст пассажиров
ages = pd.read_csv("test.csv").Age
# выжил/не выжил
survived = pd.read_csv("gender_submission.csv").Survived

sns.kdeplot(ages[survived == 1], color="darkturquoise", shade=True)
sns.kdeplot(ages[survived == 0], color="lightcoral", shade=True)
plt.legend(['Survived', 'Died'])
plt.show()

n, bins, patches = plt.hist(ages, density=True, facecolor='g', alpha=0.75)
plt.xlabel('Age')
plt.ylabel('Probability')
plt.grid(True)
plt.show()
