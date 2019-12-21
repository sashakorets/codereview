'''
вивести всі слова в нижньому регістрі
'''

data='AS aSssssdsad asdasdas ads asd asdas 1 2'
data_list = data.split(' ')
for word_lower in data_list:
    if word_lower==word_lower.lower():
        print(word_lower)
    else:
        continue
