# Grosbeak

Audio quality manipulation experiment using deep learning.

## Goal

Be able to infer high quality, studio level audio recording out of normal recording from normal phone for any type source
(guitar, piano, vocal). (Ambitious right? I know)

## How to use?

This project requires you to have:
1. Dependencies listed in Pipfile, use [pipenv](https://pipenv.readthedocs.io/en/latest/) for convenience.
2. A bunch of audio dataset to train on, put it in raw_dataset directory.
3. (optional) Use pycharm if possible

To run this code do the following:
1. Generate the dataset using generate_dataset.py, run the `DEFINE VAR` then `GENERATE DATASET` cell if using pycharm, 
delete the last `CLEAN DATASET` part, then run the file otherwise.
2. Generate the model using the train_model.py
3. Put audio file in inference_input, then run infer.py to generate output from trained model.