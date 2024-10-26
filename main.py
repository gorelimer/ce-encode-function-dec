from argparse import ArgumentParser

from src import LuaDecompiler


parser = ArgumentParser()
parser.add_argument("file_path", nargs='?')
args = parser.parse_args()

if args.file_path is not None:
    with open(args.file_path) as f:
        encoded_func = f.read()
else:
    encoded_func = input("Enter encoded function: ")

LuaDecompiler.decompile_encoded_func(encoded=encoded_func)
