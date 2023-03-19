#power by https://github.com/little-file/
#version 1
import tarfile

def tar():
    print(".tar")
    tar_path = input("example /path/to/tarfile.tar:")
    with tarfile.open(tar_path, "r") as tar:
        tar.extractall()
def tar_gz():
    print(".tar.gz")
    tar_path = input("example /path/to/tarfile.tar:")
    with tarfile.open(tar_path, "r:gz") as tar:
        tar.extractall()

while True:
    print("""
    [1]tarfile.tar
    [2]tarfile.tar.gz
    [3]quite
    """)
    choice = int(input("Enter your choice: "))
    if choice == 1:
        tar()
    elif choice == 2:
        tar_gz()
    elif choice == 3:
        break 
    else:
        print("invalid choice. Please try again.")
