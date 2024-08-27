def custom_write(file_name,strings):
    file=open(file_name,'w',encoding='utf-8')
    string_positions={}
    for i in range(len(strings)):
        string_positions.update({(i + 1, file.tell()): strings[i]})
        file.write(f'{strings[i]}\n')
    return string_positions
    file.close

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)