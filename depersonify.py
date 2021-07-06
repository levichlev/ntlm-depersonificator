result = ""
parts = []
newlines = []


with open('.\\hashes.txt', 'r') as file:
    lines = [line.rstrip('\n') for line in file]
    file.close

for line in lines:
    array = line.split(":")
    array[4] = array[4][:10] + 5 * '*'
    parts.append(array[5][10:35])
    parts.append(array[5][100:150])
    parts.append(array[5][300:350])
    parts[0] = parts[0][:10] + 5 * '*'
    parts[1] = parts[1][:10] + 5 * '*'
    parts[2] = parts[2][:10] + 5 * '*'
    parts.append(10 * '*')
    array[5] = array[5][:9] + parts[0] + parts[1] + parts[2] + array[5][351:484] + parts[3] + array[5][520:]
    newlines.append(":".join(array))
    array = []
    print(line)

print('#' * 20)
print(newlines)

with open('result.txt', 'w') as f:
    for line in newlines:
        f.write(line + '\n')
