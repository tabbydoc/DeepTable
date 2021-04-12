import os
import json
import pickle

path_struct = "G:\\proj\\python\\DeepTable\\Deep\\scitsr\\structure"

files_list = open("input_files", "r")
data = []
tables = []
answers = []
for line in files_list:
    file, index = line.replace('\n', '').split(";")
    table = [["dungeon master" for _ in range(9)] for _ in range(9)]
    answer = [0, 0, 0]
    with open(os.path.join(path_struct, file + ".json")) as f:
        json_file = json.load(f)
        for cells in json_file['cells']:
            text = ""
            for content in cells['content']:
                text += content
            if cells['start_row'] < 9 and cells['start_col'] < 9:
                for x in range(cells['end_row'] - cells['start_row'] + 1):
                    for y in range(cells['end_col'] - cells['start_col'] + 1):
                        table[x + cells['start_row']][y + cells['start_col']] = text
        for x in range(8, -1, -1):
            for y in range(8, -1, -1):
                if table[x][y] == 'dungeon master':
                    table[x].pop(y)
            if len(table[x]) == 0:
                table.pop(x)

    answer[int(index)] = 1
    answers.append(answer)
    tables.append(table)
# data = [tables, answers]
# print(data)
with open("DeepTable//tables.pickle", 'rb') as f:
    data_new_f = pickle.load(f)
    for data_n in data_new_f[0]:
        tables.append(data_n)
    for data_n in data_new_f[1]:
        answers.append(data_n)
    data = [tables, answers]

print(data)
with open('DeepTable\\new_dataset.pickle', 'wb') as f:
    pickle.dump(data, f)
files_list.close()

