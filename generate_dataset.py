from os import listdir, makedirs
from shutil import rmtree
import librosa

# Script for preparing dataset
# Takes data from RAW_DATASET_LOCATION to generate data in FINAL_DATASET_LOCATION

RAW_DATASET_LOCATION = "raw_dataset"
FINAL_DATASET_LOCATION = "dataset"
TRAIN_DATASET_LOCATION = FINAL_DATASET_LOCATION + "/train"
DEV_DATASET_LOCATION = FINAL_DATASET_LOCATION + "/dev"
TEST_DATASET_LOCATION = FINAL_DATASET_LOCATION + "/test"


def get_raw_dataset_paths() -> [str]:
    try:
        file_lists = listdir(RAW_DATASET_LOCATION)
        print("raw dataset found")
        return file_lists
    except FileNotFoundError:
        print("raw dataset directory not found, aborting")
        exit(0)


def make_final_dataset_dir() -> None:
    try:
        rmtree(FINAL_DATASET_LOCATION)
        print("recreating final dataset directory")
    except (FileExistsError, FileNotFoundError):
        print("creating final dataset directory")
    finally:
        makedirs(TRAIN_DATASET_LOCATION)
        makedirs(DEV_DATASET_LOCATION)
        makedirs(TEST_DATASET_LOCATION)


def generate_hi_lo_pair(filename):
    hi_res_audio, sr = librosa.load(RAW_DATASET_LOCATION + "/" + filename)
    lo_res_audio = librosa.core.resample(hi_res_audio, sr, 8000)
    return hi_res_audio, lo_res_audio


if __name__ == "__main__":
    raw_dataset_filenames: [str] = get_raw_dataset_paths()
    make_final_dataset_dir()

