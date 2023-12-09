
with open('test.txt', 'w') as file:
     file.write('Hello world')


def writeText(text):
    with open("text.txt", "w") as file:
        file.write(text)
        
def checkText():
    with open("mysteryText.txt", "r") as file:
        for line in file:
            writeText(line)
checkText()
                
