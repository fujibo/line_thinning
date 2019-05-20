import argparse
import os
import tqdm

from thin import Thinner, save_image


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_dir')
    parser.add_argument('--output_dir')
    parser.add_argument('--split', type=int, default=0)
    parser.add_argument('--n_proc', type=int, default=1)
    args = parser.parse_args()

    paths = sorted(os.listdir(args.input_dir))
    paths = paths[args.split::args.n_proc]
    thin = Thinner()
    for path in tqdm.tqdm(paths):
        output = thin(os.path.join(args.input_dir, path))
        save_image(output, os.path.join(args.output_dir, path))


if __name__ == '__main__':
    main()
