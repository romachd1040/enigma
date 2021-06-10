import os
#path = input ("Enter Path to calculate Directory and file count:")
path="/home/ec2-user"
print(path)
fileCount = 0
dirCount = 0
for root, dirs, files in os.walk(path):
    print('Looking in:',root)
    for directories in dirs:
        dirCount+=1
    for Files in files:
        fileCount+=1
print('Number of files',fileCount)
print('Number of Directories',dirCount)
print('Total Count Including both Directories and Files:',(dirCount +
fileCount))

