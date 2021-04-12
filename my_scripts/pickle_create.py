import pickle
import json

data = [[
    [["Зоны",                   "Плотность хералия", "Уровень связи", "Отдых"],
     ["Распределительный узел",       "0.56",           "5",            "1"],
     ["Метеостанция",                 "0.78",           "3.4",          "0"],
     ["Озёрный узел",                 "0.87",           "4",            "1"]],
[["Зоны",                   "Плотность хералия", "Уровень связи", "Отдых"],
     ["Распределительный узел",       "0.56",           "5",            "1"],
     ["Метеостанция",                 "0.78",           "3.4",          "0"],
     ["Озёрный узел",                 "0.87",           "4",            "1"]],
[["Зоны",                   "Плотность хералия", "Уровень связи", "Отдых"],
     ["Распределительный узел",       "0.56",           "5",            "1"],
     ["Метеостанция",                 "0.78",           "3.4",          "0"],
     ["Озёрный узел",                 "0.87",           "4",            "1"]],
[["Зоны",                   "Плотность хералия", "Уровень связи", "Отдых"],
     ["Распределительный узел",       "0.56",           "5",            "1"],
     ["Метеостанция",                 "0.78",           "3.4",          "0"],
     ["Озёрный узел",                 "0.87",           "4",            "1"]]
], [[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1]]]

print(data)

with open('DeepTable\\my_table.pickle', 'wb') as f:
    pickle.dump(data, f)
with open('DeepTable\\my_table.json', 'w') as f:
    json.dump(data, f)

with open('DeepTable\\my_table.pickle', 'rb') as f:
    data_new = pickle.load(f)
print(data_new)