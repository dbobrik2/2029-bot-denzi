file = open('file.txt', 'a',) as file:
values = [10, 20, 30, 40, 50]

counter = 0
while counter < len(values):
file.write(str(values[counter]) + "\n")
counter += 1

file = open('file.txt', 'r') as file
print("Reading from file")
print(file.read())