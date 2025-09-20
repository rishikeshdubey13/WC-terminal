import argparse
import sys #system-specific parameters and functions. It's the standard way to interact with the Python interpreter and the operating system environment.

def main():
    parser = argparse.ArgumentParser(description="ccwc: word, line, character and bytecount")
    parser.add_argument("-c", action = "store_true", help = "output the number of bytes")
    parser.add_argument("-w", action="store_true", help = "output the number of words")
    parser.add_argument("-l", action="store_true", help="output the number of lines")
    parser.add_argument("-m", action= "store_true", help="output the number of characters")
    parser.add_argument("file", nargs="?", help="file to process (optional; defaults to stdin)") #nargs-> number of arguments | ? -> makes the argument optional 

    args = parser.parse_args()

    print(f"Flags: c={args.c}, l= {args.l}, m={args.m}, w={args.w}")
    if args.file:
        try:
            with open(args.file, "rb") as f: #r-> read, b->binary, this means "open the file for reading in binary mode"
                data =f.read
        except FileNotFoundError:
            print(f"ccwc: {args.file} No such file or directory")
            sys.exit(1)
    else:
        data = sys.stdin.buffer.read()
        


if __name__ == "__main__":
    main()