# GDDecoder

### *Версия 1.1.1*

- Добавлено раскидирование блоков в редакторе, помещение их в список со словарём настроек. Для групп добавлен перевод в список. !!! Функция 1 раз сломала сохранение, советую делать бекап до выяснения причины поломки !!!

Библиотека для простого расшифрования, редактирования и сохранения файлов сохранений игры Geometry Dash.

## Пример
Для начала нужно подключить библиотеку и создать объект класса GDLevels. Как аргумент в него передаётся путь к файлу сохранения, пример ```Filepath="CCLocalLevels.dat"```. Если его не передать, будет использоваться стандартный путь к файлам сохранений Geometry Dash ```C:\Users\{user}\AppData\Local\GeometryDash\CCLocalLevels.dat```
```python
from GDDecoder import GDLevels


levels = GDLevels()
```

Чтобы начать процесс раскодирования, нуждно использовать метод **load()**. Так же можно сразу произвести раскодирование при создании объекта.
```python
levels = GDLevels().load()
```
**load()** вернёт объект

Чтобы сохранить изменённый файл и закодировать, нужно использовать метод **save()**
```python
levels.save()
```
Файл, выбранный при открытии, перезапишется. Чтобы создать новый файл или перезаписать другой, нужно изменить путь сохранения через level.savepath = "новый путь".
```python
levels.savepath = "other/CCLocalLevels.dat"

levels.save()
```
### Программа, меняющая название 1 уровня в игре

```python
from GDDecoder import GDLevels


levels = GDLevels().load()  # Загрузка

levels.levels["k_0"]["k2"] = "test text"  # Изменение названия

levels.save()  # Сохранение
```

Чтобы понять, как обпратитьтся к нужному значению, можно использовать раскодированный файл сохранения, или посмотреть структуру словаря в debag'ере<br>

![image](https://user-images.githubusercontent.com/58140098/114270215-5f6f3580-9a35-11eb-8b8a-b6803d03cdbe.png)

Ключи **"k_0"**, **"k_1"** и тд хранаят словарь с данными о уроне<br>

![image](https://user-images.githubusercontent.com/58140098/114270272-a4936780-9a35-11eb-8a7d-693297e9b82e.png)

В ключе **"k2"** хранится название уровня.

Значения ключей нужно подбирать экспеременальным путём или найти где-то в интернете. В будущем я добавлю файлик со значением всех ключей + сделаю замену ключей в словаре, чтобы сразу было понятно, что есть что.

### Доступ в редактор

```python
from GDDecoder import GDLevels


levelsdata = GDLevels().load()# Загрузка

editor = s.loadeditor(int(input("Номер уровня: ")))  # Загрузка редатора из уровня

print(editor.blocks[0]["57"])  # Вывидит все группы первого блока в редаторе

levelsdata.saveeditor(1, editor)  # Сохранит в 1 уровень редактор

```

В массиве ***blocks*** будут все блоки в уровне. Каждый эллемент массива хранит слварь с данными о блоке. Без перевода все ключи имеют значения как в игре. ***editor.blocks["1"]*** вернёт id блока, **editor.blocks["2"]*** позицию по X.


## Переменные

### ***level.plist***
Хранит расшифрованный файл сохранения в виде xml кода. В нём не будет табуляций и переносов строк. Чтобы их добавить можно использовать функцию strtoplist из файла convertors.py
```python
from converters import strtoplist


plist = strtoplist(levels.plist)

with open("gamedata.plist", "w") as f:
    f.write(plist)
```
Подобный код можно будет открыть в plist редакторе и визуально ознокомиться с ним.
![image](https://user-images.githubusercontent.com/58140098/114268168-f635f500-9a29-11eb-9794-669b8985c703.png)

### ***level.filedict***
Хранит словарь, особым образом созданный из xml кода сохранений. Не сохраняется и не загружается при создании [**загрузачной точки**](https://github.com/NodusLorden/GDDecoder/blob/main/README.md#%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BE%D1%87%D0%BD%D0%B0%D1%8F-%D1%82%D0%BE%D1%87%D0%BA%D0%B0). Переходная ячейка хранения данных.

### ***levels.levels***
Хранит словарь из всех уровней и является копией ```levels.filedict["LLM_01"]```.

### ***levels.rude***
Хранит (на всякий случай) разные значения не оказывающее влияние на файл сохранений. Используется в сборке файла сохранения

### ***levels.savepath***
Харнит путь, куда будет сохраняться файл после вызова метода ```level.save```. Если его не менять, путь будет такой же как и у открытого файла.

## Загрузочная точка
На расшифровку и конвертацию файла тратится много времени. Чтобы долго не ждать, при многократном использовании программы, можно создать точку, где будет сохранена вся нужная информация в незакодированном виде. Загрузка такого файла в разы быстрее исходного.<br>
Для создания, нужно сипользовать ```level.createloadpoint()```, как аргумент можно передать путь к файлу загрузочной точки, по умолчанию "point.json". Можно сделать точку сразу при создании объекта ```levels = GDLevels().createloadpoint()```. В файл сохранится список
```python
[self.FILEPATH, self.savepath, self.plist, self.levels, self.rude, self.convertkey]
``` 
Для загрузки можно использовать ```levels.fastload()``` или ```levels = GDLevels().fastload()```.




## Сейчас в разработке

- Расшифровка цветов в редаторе
- Переводчик ключей словаря с циферного значения в человеческий. Добавление их как мод или класс, для удобства обновления
- Переводчик оставшихся сложных значений (группы уже добавлены). Добавление их как мод или класс, для удобства обновления
- Перенос класса LevelEditor в GDLevel, оптимизация, упрощение кода и уменьшение прослоек
