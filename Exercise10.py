import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# TODO: Use the glob.glob() function to obtain the list of filenames
filelist = glob.glob(pattern)
for filename in filelist:
    print(filelist)

# TODO: use os.path.getsize to find each file's size

for filesize in filelist:
    print(filename,'the file size is:', (os.path.getsize(hdir)), 'bytes')

# TODO: Add a test to only display files that are not zero length
filesize=(os.path.getsize(hdir))
for relevantfilesize in filelist:
    if filesize == 0:
        pass
    else:
        print(filelist, filename, 'the file size is:', filesize, 'bytes')


# TODO: Remove the leading directory name(s) from each filename before you print it -
# using os.path.basename()
for simplelist in filelist:
    simplelist = (os.path.basename(filename))
    print('the file local location is:', simplelist)


