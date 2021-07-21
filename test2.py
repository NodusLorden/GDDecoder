from GDDecoder import GDLevels
from decoders import *
from converters import *


'''
Заменяет блоки с выбранным id и групой 955 на другие, с сохранением всех настроек
Replaces blocks with the selected id and group 955 with others, while maintaining all settings
'''

print("Загрузка и расшифровка файлов игры...")
s = GDLevels().load()
print("Загрузка завершена")

ed = s.loadeditor(int(input("Номер уровня: ")))
print("Редактор загружен")

id1 = input("id заменяемного блока: ")
id2 = input("id блока на замену: ")

print("Замена...")
for i in range(len(ed.blocks)):
    if ed.blocks[i]["1"] == id1 and "57" in ed.blocks[i].keys() and "955" in ed.blocks[i]["57"]:
        ed.blocks[i]["1"] = id2

print("Сборка редактора...")
s.saveeditor(1, ed)

print("Сборка и сохранение данных игры...")
s.save()

print("end")

input()
