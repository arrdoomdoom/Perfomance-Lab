Проверка корректности вводимых значений не осуществляется. Предполагаю, что в этом нет необходимости, но если будет нужно, могу добавить.
Единственное, что было непонятно, аргументы вводятся одной строкой через пробел, либо же разными строками. Сработают оба варианта.

Для третьего задания есть две версии решения. Основная версия полностью сохраняет исходную структуру файла, но сломается, если структуру изменить, скажем, передав json в одну строку. Но до тех пор, пока каждая строка файла содержит только одну пару ключ:значение, всё будет работать.
Альтернативная версия немного портит структуру файла, сохраняя только структуру данных внутри. Она не сломается, как бы ни менялся формат файла.
Если будет нужно, могу как-то объединить придумать.
