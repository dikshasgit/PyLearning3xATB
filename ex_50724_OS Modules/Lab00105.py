# Walk me in directory
import os

for root, dir, files in os.walk("C:/Users/snigd/PycharmProjects/PyLearning 3xATB/Ex_01072024"):
    print(f'current dir {root}')
    print(f'sub dir dir {dir}')
    print(f"files dir dir {files}")
    print(len(files))  # it will give the length of the files

    # import os

    fd = os.open("testdata.txt", os.O_RDWR)
    os.write(fd, b"hello i writing for api test")  # in the testdata the text we have written it will appear there
    os.close(fd)
