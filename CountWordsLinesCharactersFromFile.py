def count_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        word_count= 0
        char_count = 0
        for line in lines:
            words = line.split()
            word_count += len(words)
            char_count += len(line)
    return (char_count, word_count, line_count)
 
file= "./test.txt"
char_count, word_count, line_count = count_file(file)
print(f"Number of words = {word_count}")
print(f"Number of lines = {line_count}")
print(f"Number of characters = {char_count}")
