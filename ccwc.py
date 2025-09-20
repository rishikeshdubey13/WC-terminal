import argparse
import sys #system-specific parameters and functions. It's the standard way to interact with the Python interpreter and the operating system environment.


def count_bytes(data: bytes) -> int:
    return len(data)

def count_lines(data: bytes) -> int:
    return data.count(b'\n')
    # lines = data.count(b"\n") #Note: wc counts newlines, even the last line
    # if data and not data.endswith(b"\n"):
    #    lines+=1
    # return lines

def count_words(data: bytes) -> int:
    #decode to str fo rword splting
    text = data.decode('utf-8', errors='replace') #Assuming utf-8
    words = text.split() # splits on whitespces
    return len(words)

def count_chars(data: bytes) -> int:
    text = data.decode('utf-8', errors='replace')
    return len(text)

def main():
    parser = argparse.ArgumentParser(description="ccwc: word, line, character and bytecount")
    parser.add_argument("-c", action = "store_true", help = "output the number of bytes")
    parser.add_argument("-w", action="store_true", help = "output the number of words")
    parser.add_argument("-l", action="store_true", help="output the number of lines")
    parser.add_argument("-m", action= "store_true", help="output the number of characters")
    parser.add_argument("file", nargs="?", help="file to process (optional; defaults to stdin)") #nargs-> number of arguments | ? -> makes the argument optional 

    args = parser.parse_args()

    if args.c and args.m:
        args.c  = False

    

    # print(f"Flags: c={args.c}, l= {args.l}, m={args.m}, w={args.w}")
    if args.file:
        try:
            with open(args.file, "rb") as f: #r-> read, b->binary, this means "open the file for reading in binary mode"
                data =f.read()
        except FileNotFoundError:
            print(f"ccwc: {args.file} No such file or directory")
            sys.exit(1)
    else:
        data = sys.stdin.buffer.read() #Use buffer for binary data
    
    if not (args.c or args.l or args.w or args.m):
        args.l = args.w = args.c = True
    
    results = []
    if args.l:
        results.append(str(count_lines(data)))
    if args.w:
        results.append(str(count_words(data)))
    if args.c:
        results.append(str(count_bytes(data)))
    if args.m:
        results.append(str(count_chars(data)))
    
    output = ' '.join(results)
    if args.file:
        output += f" {args.file}"
    print(output)

    # # test counts
    # print(f"Bytes: {count_bytes(data)}")
    # print(f"Lines: {count_lines(data)}")
    # print(f"Words: {count_words(data)}")
    # print(f"Chars: {count_chars(data)}")


if __name__ == "__main__":
    main()