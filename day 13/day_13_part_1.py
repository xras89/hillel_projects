file_name = 'data.txt'

with open(file_name, 'w') as f:
    while True:
        line = input('Input your text: ')
        if not line:
            break

        f.write(f'{line}\n')

print(f'Data is saved to the file {file_name}')