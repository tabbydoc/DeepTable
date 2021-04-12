import csv
import fnmatch
import pickle
import os
import random
import numpy as np

data = []
tables = []
answers = []

c = -1
for root, _, files in os.walk("G:\\Local\\part1001-2000\\1346823845675_1346868712460_2991.arc.gz6165451449140421555"):
    for file in files:
        # print(file)
        if fnmatch.fnmatch(file, '*.csv'):
            # c += 1
            # if c > 9:
            #     break
            try:
                with open(os.path.join(root, file)) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    table = []
                    answer = [1, 0, 0]
                    for i, row in enumerate(csv_reader):
                        row_list = []
                        for j, cell in enumerate(row):
                            if j < 9:
                                row_list.append(str(cell))
                            else:
                                break
                        if i < 9:
                            table.append(row_list)
                        else:
                            break
                    if random.random() > 0.5:
                        table = np.array(table)
                        answer = [0, 1, 0]
                        table = np.transpose(table)
                        table = table.tolist()
                    answers.append(answer)
                    tables.append(table)
            except Exception:
                # print('skip')
                c = 0
print("OK")
with open("DeepTable//tables.pickle", 'rb') as f:
    data_new_f = pickle.load(f)
    for data_n in data_new_f[0]:
        tables.append(data_n)
    for data_n in data_new_f[1]:
        answers.append(data_n)
print("OK")
with open("DeepTable//new_dataset.pickle", 'rb') as f:
    data_new_f = pickle.load(f)
    for data_n in data_new_f[0]:
        tables.append(data_n)
    for data_n in data_new_f[1]:
        answers.append(data_n)
print("OK")
data = [tables, answers]
print(data[0])

with open('DeepTable\\cvs_dataset.pickle', 'wb') as f:
    pickle.dump(data, f)

