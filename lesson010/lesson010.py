# -*- coding: utf-8 -*-
"""lesson010.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T7UcFa-yAC-rnGEVREjS2ZbwF9rCeg9E

**Задача 44**

Создать новый столбец height_group в таблице с пингвинами, который будет отвечать за показатель длины клюва пингвина. high - высокий(от 42), middle - средний(от 35 до 42), low - низкий(до 35).

Изобразить гистограмму по flipper_length_mm с оттенком height_group.
"""

import pandas as pd
import seaborn as sns

# Подключение таблицы с пингвинами
penguins = sns.load_dataset("penguins")
penguins.head(10)

# Создать новый столбец height_group в таблице с пингвинами,
# который будет отвечать за показатель длины клюва пингвина.
# high - высокий(от 42), middle - средний(от 35 до 42), low - низкий(до 35).

def f(row):
 if row['bill_length_mm'] >= 42.0:
   val = 'high'
 elif row['bill_length_mm'] <= 35.0:
   val = 'low'
 else :
   val = 'middle'
 return val


penguins['height_group'] = penguins.apply (f, axis=1)
penguins[:10]

# Изобразить гистограмму по flipper_length_mm с оттенком height_group.
sns.histplot(data=penguins, x='bill_length_mm', hue='height_group')