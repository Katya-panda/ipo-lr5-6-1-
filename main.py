# открываем файл text.txt в режиме чтения
with open("text.txt", "r", encoding = "utf-8") as input_file:
    # читаем строки из файла
    lines = input_file.readlines()
#  открываем файл output.txt в режиме записи
with open("output.txt", "w", encoding = "utf-8") as output_file:
    # проходим по каждой строке из input_file
    for line in lines:
        # удаляем пробелы и символы новой строки 
        stripped_line = line.strip()
        # записываем эту строку в обратном порядке в output.txt
output_file.write("stripped_line[::-1]'\n'")
# выводим сообщение о завершении записи
print("Строки записаны в output.txt в обратном порядке.")