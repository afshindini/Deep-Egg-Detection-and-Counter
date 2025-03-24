---
title: Deep Egg Detection And Counter
emoji: ⚡
colorFrom: green
colorTo: pink
sdk: streamlit
sdk_version: 1.43.2
app_file: app.py
pinned: false
license: mit
short_description: Detect and count white and brown eggs from images
---
# Deep-Egg-Detection-and-Counter
This repository allows you to detect and count eggs in an egg-shell with the help of deep learning models specifically YOLOv5.
A labeled dataset for training this model is collected manually.
A YOLOv5 model is trained on this dataset and the trained model is provided and used to detect and count eggs in an egg-shell.

## Dataset
A dataset from real application is collected and labeled manually in TOLO-format in order to be used for training and validation purposes.
This dataset is available [here](https://huggingface.co/datasets/afshin-dini/Egg-Detection).
The eggs are collected within different shell types and colours (the egg-shall might be transparent plastic, bright/dark carton, etc.) in order
to make the model robust to different background condition that might be encountered in real applications.
Right now, two classes exists in this dataset as:
- White eggs
- Brown eggs

The boundaries of the eggs are also specified in the dataset and the dataset is split into training and validation sets.
We try to make this dataset more diverse and rich by adding more classes and more images in the future.

### Dataset YOLO-format Structure
The [dataset](https://huggingface.co/datasets/afshin-dini/Egg-Detection) is prepared in th YOLO-format make it easier to use.
This dataset is split into training and validation sets. The structure of the dataset to be used in YOLO models are as following:
```
data/
├── images/
│   ├── train/
│   │   ├── sample1.jpg
│   │   ├── ...
│   │   ├── sample49.jpg
│   ├── val/
│   │   ├── sample50.jpg
│   │   ├── sample51.jpg
├── labels/
│   ├── train/
│   │   ├── sample1.txt
│   │   ├── ...
│   │   ├── sample49.txt
│   ├── val/
│   │   ├── sample50.txt
│   │   ├── sample51.txt
├── data.yaml
├── train.txt
├── val.txt
```
It is good to mention that although the number of images are not too much at the moment, there are many different eggs in each image which increases the
number of samples used in the training and validation stages. The `txt` files in the labels folders contain the bounding boxes around each egg in the images as well as
the class of egg which is white/brown.

The `train.txt` and `val.txt` files contain the path to the images in the training and validation sets.
The `data.yaml` file contains the class names, the path to the training and validation sets, and also the path to the parent `data` directory.

**NOTE:** For training, it is important to change the path to **absolute path** of the main directory where the data is located (In the above tree-structure it should be the absolute path to `data` directory.)

## How to Develop
Do the following only once after creating your project:
- Init the git repo with `git init`.
- Add files with `git add .`.
- Then `git commit -m 'initialize the project'`.
- Add remote url with `git remote add origin REPO_URL`.
- Then `git branch -M master`.
- `git push origin main`.
Then create a branch with `git checkout -b BRANCH_NAME` for further developments.
- Install poetry if you do not have it in your system from [here](https://python-poetry.org/docs/#installing-with-pipx).
- Create a virtual env preferably with virtualenv wrapper and `mkvirtualenv -p $(which python3.10) ENVNAME`.
- Then `git add poetry.lock`.
- Then `pre-commit install`.
- For applying changes use `pre-commit run --all-files`.

## Docker Container
Under development.
