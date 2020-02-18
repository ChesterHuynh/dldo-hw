import os
import numpy as np

from pathlib import Path
from scipy.spatial.distance import squareform


def parse_matrix(fpath):
    with open(fpath) as f:
        dists = f.read()

    arr = np.fromstring(dists, sep=' ')  # Convert into 1D array
    arr = arr[np.nonzero(arr)]
    mat = squareform(arr)  # Convert to symmetric matrix

    return mat


if __name__ == "__main__":
    basedir = Path(__file__).parent.absolute()
    fpath = os.path.join(basedir, "data/usa50.txt")
    weights = parse_matrix(fpath)
