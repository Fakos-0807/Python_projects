# pip install pandas
import pandas as pd
import os

# Series - структура даних, що містить елементи та їх індекси.
# DataFrame - структура даних, що містить набори елементів та їх індекси.
# Кожен рядок та кожен стовпець DataFrame є об'єктом типу Series.

# Comma-Separated Values (CSV) ​​- значення, розділені комами.
# df = pd.read_csv(os.path.join(os.path.abspath(__file__) + '/..', 'class_set.csv'))
df = pd.read_csv(os.path.join(os.path.abspath(__file__ + '/..'), 'GoogleApps.csv'))

#print(df.info() )

print(df.info())
# Скільки коштує найдешевший платний додаток?
# print() Price min
# Type
#print(df[  df["Type"] == "Paid"  ]["Price"].min())

# Чому дорівнює медіана кількості установок додатків із категорії ART_AND_DESIGN?
 

###print(df[  df["Content Rating"] == "Teen" ]["Size"].min())
###print(df[  df["Type"] == "Paid" ]["Reviews"].max())
#print(df["Price"].value_counts())
print(df[(df["Price"] == df["Price"] >= 20)])
#print(df[df[df["Price"] >= 20] & df[df["Installs"] >= 10000]["Rating"].mean()])

print(df[(df['Price'] >= 20) & (df['Installs'] >= 10000)]['Rating'].mean())
#print(df["Price"].max())
# df.info()              #  Повертає коротку інформацію про кожен стовпчик і датафрейм загалом
# object -  текст, 
# float64 - дробове число, 
# int64 - ціле число.

# print(len(df.columns))
####print(df[df["Reviews"] == df["Reviews"].max()]["Category"])
# info = df.head(2)      #  Повертає перші n (за замовчуванням 5) рядків датафрейму
# info = df.tail(2)      #  Повертає останні n (за замовчуванням 5) рядків датафрейму
#info = df.describe()   #  Повертає узагальнені статистичні показники на основі даних, що зберігаються в датафреймі
#print(info)

# count     Кількість непустих значень
# mean      Середнє арифметичне
# std       Стандартне відхилення
# min       Мінімальне значення ознаки
# 25%       25-й відсоток (перший квартиль)
# 50%       50-й відсоток (медіана) median()
# 75%       75-й відсоток (третій квартиль)


# unique    вивести унікальні значення з стовбця в датасеті
# print(df['Type'].unique())
# print(df['Installs'].min())
# print(df['Installs'].mean())
# print(df['Installs'].max())
# min(), max(), mean() і median()