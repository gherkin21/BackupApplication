import argparse

def get_args():
    # Read arguments from command line
    parser = argparse.ArgumentParser()
    parser.add_argument('--credentials', '-c', help='ścieżka do pliku z credentialsami')
    parser.add_argument('--file', '-f', required=True, help='ścieżka do pliku do wysłania')
    parser.add_argument('--project', '-p', required=True)
    parser.add_argument('--bucket', '-b', required=True, help='nazwa bucketu')
    parser.add_argument('--prefix', '-P', default=None)
    args = parser.parse_args()
    return args
