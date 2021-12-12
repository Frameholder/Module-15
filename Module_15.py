Myfile=input('Enter file name ')
Myfile+=".txt"
with open(Myfile) as f:
    fileText = f.read()
   # print(fileText)
def changeText(fileText):
    for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
        fileText = fileText.replace(i, '')

    return fileText.split()
print(changeText(fileText))
