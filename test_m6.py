def read_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content



def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for _ in file)
    return line_count



def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text)



def read_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = [file.readline().strip() for _ in range(n)]
    return lines




def delete_line(filename, n):
    lines = []
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(filename, 'w') as file:
        for idx, line in enumerate(lines):
            if idx != n-1:
                file.write(line)




def sum_numbers(filename):
    total = 0
    with open(filename, 'r') as file:
        for line in file:
            total += int(line.strip())
    return total



def find_longest_word(filename):
    longest = ''
    with open(filename, 'r') as file:
        for line in file:
            for word in line.split():
                if len(word) > len(longest):
                    longest = word
    return longest




def safe_file_read(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"
