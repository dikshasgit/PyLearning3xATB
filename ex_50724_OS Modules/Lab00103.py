# OS Module, many many modules are in python
# OS TO INteract with the operating system,
# multiple operation, in which directory we are, overall file name, size of the file, name of the file
# to get working directory, change dir, file exist, Environment


# all functions from posix or nt, e. g. unlink, stat, etc.
# os. path is either posixpath or ntpath
# os. name is either 'posix' or 'nt'
# os. curdir is a string representing the current directory (always '.')
# os. pardir is a string representing the parent directory (always '..')
# os. sep is the (or a most common) pathname separator ('/' or '\')
# os. extsep is the extension separator (always '.')
# os. altsep is the alternate pathname separator (None or '/')
# os. pathsep is the component separator used in $PATH etc
# os. linesep is the line separator in text files ('r' or 'n' or 'rn')
# os. defpath is the default search path for executables
# os. devnull is the file path of the null device ('/ dev/ null', etc.)
# Programs that import and use 'os' stand a better chance of being portable between different platforms. Of course,they must then only
# use functions that are defined by all platforms (e. g., unlink and opendir), and leave all pathname manipulation to os. path (e. g., split and join).
for window nt, posix - mac / linux
#
print(os.getcwd())  # currentworkkingdirectory
#
# os.chdir("C:/Users/snigd/PycharmProjects/PyLearning 3xATB/")# change the directory
# print(os.getcwd()) #currentworkkingdirectory
#
print(os.listdir("C:/Users/snigd/PycharmProjects/PyLearning 3xATB/"))  # list dir
#
# os.mkdir("Snigdha")# created one directory

# Read a file, if file exist or not we have to check the files ,

size = os.path.getsize('testdata.txt')
