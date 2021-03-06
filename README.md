# DeepTable

### A Permutation Invariant Neural Network for Table Orientation Classification

This repository contains a table corpus with their orientations annotations for tables from PMC, and additionally contains the code and the models for classifying tables into one of the orientation layouts of horizontal, vertical, and matrix.
<br>
## Train a model
To train a model, you need to use the DeepTableTrain.py and provide the number of epochs, the learning rate value and the location of the trained embeddings (download it from <a href = "http://bio.nlplab.org/"> here</a>), the table data (in tables.picklef file) and the directory of the trained model:
```
DeepTableTrain.py [-h] -e N_EPOCH -l LR -v EMBEDDING_LOC -i INPUT_TABLES -o MODEL_DIR
```


## Table Orientation tagging

The following command tags tables into one of the three classes of 0: horizontal, 1: vertical and 2: matrix. Before using this command you need to train a model.

```
DeepTableEval.py [-h] -m MODEL -i INPUT_TABLES -o OUTPUT_TAGS
```


## Citation
Please cite the following work
```
@article{habibi2020deeptable,
  title={DeepTable: A Permutation Invariant Neural Network for Table Orientation Classification},
  author={Habibi, Maryam and Starlinger, Johannes and Leser, Ulf},
  booktitle={Data Mining and Knowledge Discovery},
  year={2020}
}
```

