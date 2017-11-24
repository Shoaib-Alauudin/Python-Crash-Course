alphabets = 'abcdefghijklmnopqrstuvwxyz'

def check_count(char,text):
    count = 0
    for alphabet in text.lower():
        if alphabet == char:
            count += 1
    return count

fileName = input("Please enter file name do you want to open ? ")
with open(fileName) as f:
    text = f.read()

print(check_count('h',text))

for alphabet in alphabets:
    percentage = 100 * check_count(alphabet, text)/len(text)
    print("{a} - {b}%".format(a=alphabet,b=round(percentage,3)))
