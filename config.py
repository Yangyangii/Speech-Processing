import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--fpath', type=str, default='', help='audio file used in processing')
args = parser.parse_args()
