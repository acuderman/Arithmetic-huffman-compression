import random

class StringGenerator:
    def __init__(self, size):
        self.size = size

    def generateRandomSequence(self):
        random_string = ''
        for i in range(0, self.size):
            random_num = random.randint(0,10)

            if (random_num<= 4):
                random_string += 'a'
            elif (random_num <= 7):
                random_string += 'b'
            elif (random_num <= 9):
                random_string += 'c'
            else:
                random_string += 'd'

        print(random_string)
        self.string = random_string

    def saveString(self, path):
        file = open(path, 'w')
        file.write(self.string)
