import pandas as pd
import matplotlib.pyplot as plt

# Пример DataFrame
dt = {
    'id': {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 11, 11: 12,
           12: 13, 13: 14, 14: 15, 15: 16, 16: 17, 17: 18, 18: 19, 19: 20, 20: 21, 21: 22,
           22: 23, 23: 24, 24: 25, 25: 26, 26: 27, 27: 28, 28: 29, 29: 30, 30: 31, 31: 32, 32: 33,
           33: 34, 34: 35},
    'name': {0: 'John Deo', 1: 'Max Ruin', 2: 'Arnold', 3: 'Krish Star', 4: 'John Mike',
             5: 'Alex John', 6: 'My John Rob', 7: 'Asruid', 8: 'Tes Qry', 9: 'Big John',
             10: 'Ronald', 11: 'Recky', 12: 'Kty', 13: 'Bigy', 14: 'Tade Row', 15: 'Gimmy',
             16: 'Tumyu', 17: 'Honny', 18: 'Tinny', 19: 'Jackly', 20: 'Babby John', 21: 'Reggid',
             22: 'Herod', 23: 'Tiddy Now', 24: 'Giff Tow', 25: 'Crelea', 26: 'Big Nose',
             27: 'Rojj Base', 28: 'Tess Played', 29: 'Reppy Red', 30: 'Marry Toeey',
             31: 'Binn Rott', 32: 'Kenn Rein', 33: 'Gain Toe', 34: 'Rows Noump'},
    'class': {0: 'Four', 1: 'Three', 2: 'Three', 3: 'Four', 4: 'Four', 5: 'Four',
              6: 'Five', 7: 'Five', 8: 'Six', 9: 'Four', 10: 'Six', 11: 'Six', 12: 'Seven',
              13: 'Seven', 14: 'Four', 15: 'Four', 16: 'Six', 17: 'Five', 18: 'Nine', 19: 'Nine',
              20: 'Four', 21: 'Seven', 22: 'Eight', 23: 'Seven', 24: 'Seven', 25: 'Seven',
              26: 'Three', 27: 'Seven', 28: 'Seven', 29: 'Six', 30: 'Four', 31: 'Seven', 32: 'Six',
              33: 'Seven', 34: 'Six'},
    'mark': {0: 75, 1: 85, 2: 55, 3: 60, 4: 60, 5: 55, 6: 78,
             7: 85, 8: 78, 9: 55, 10: 89, 11: 94, 12: 88, 13: 88, 14: 88, 15: 88, 16: 54, 17: 75,
             18: 68, 19: 65, 20: 69, 21: 55, 22: 79, 23: 78, 24: 88, 25: 79, 26: 81, 27: 86, 28: 55,
             29: 79, 30: 88, 31: 90, 32: 96, 33: 69, 34: 88},
    'gender': {0: 'female', 1: 'male', 2: 'male', 3: 'female', 4: 'female', 5: 'male',
               6: 'male', 7: 'male', 8: 'male', 9: 'female', 10: 'female', 11: 'female', 12: 'female',
               13: 'female', 14: 'male', 15: 'male', 16: 'male', 17: 'male', 18: 'male', 19: 'female',
               20: 'female', 21: 'female', 22: 'male', 23: 'male', 24: 'male', 25: 'male', 26: 'female',
               27: 'female', 28: 'male', 29: 'female', 30: 'male', 31: 'female', 32: 'female',
               33: 'male', 34: 'female'}
}
df = pd.DataFrame(dt)
# Подсчитываем уникальные элементы для всех числовых столбцов
columns = ['mark']
for column in columns:
    # Подсчитываем уникальные элементы
    unique_elements = df[column].value_counts()
    print(unique_elements)
    # Создаем подграфики
    plt.bar(unique_elements.index, unique_elements.values, color= "#006400")

    plt.xlabel('Баллы')
    plt.ylabel('Кол-во учеников')
    plt.title('Распределение по баллам')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()