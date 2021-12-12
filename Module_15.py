Myfile=input('Enter file name ')
Myfile+=".txt"
with open(Myfile) as f:
    fileText = f.read()
   #print(fileText)
def changeText(fileText):
    for i in '!"\'#$%&()*+-,--/:.;<=>?@[\\]^_{|}~':
        fileText = fileText.replace(i, '')
    return fileText.split()

NewScript=changeText(fileText)

print(NewScript)#Выводим разделенные слова из текста в виде списка

def mostCommon(NewScript, lenght=0):
    most_common = []
    qty_most_common = 0
    for item in NewScript:
        if len(item) > lenght:
            qty = NewScript.count(item)
        if qty > qty_most_common and qty > 3:
            qty_most_common = qty
            most_common = [item]
        elif qty == qty_most_common:
            most_common.append(item)
    return list(set(most_common))
Result=mostCommon(NewScript)
print('Самое частое слово больше трех символов - это ', "".join(map(str,Result)))
print('Самое длинное слово  - это ', max(NewScript, key=len))





