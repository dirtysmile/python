# python 인자 테스트.

import sys

file_path = sys.argv[1]

if len(sys.argv) != 2:
    print("ttt")
    sys.exit()
print(sys.argv[0])
print("File path : " + file_path)

