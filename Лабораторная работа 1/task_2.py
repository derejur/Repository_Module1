size_disk = 1.44  # Объем дискеты
pages = 100  # Кол-во страниц
line_in_page = 50  # Кол-во строк на странице
symbols_in_line = 25  # Кол-во символов на странице
weight_in_symbol = 4  # Вес одного символа

size_disk_in_bytes = size_disk * (1024 * 1024)  # Сделала перевод из мб в байты
book = (pages * line_in_page * symbols_in_line * weight_in_symbol)  # Вес всей книги
book_number = int(size_disk_in_bytes // book)  # Расчет кол-ва книг, кот. можно поместить на дискету
print("Количество книг, помещающихся на дискету:", book_number)
