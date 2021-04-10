from GDDecoder import GDLevels


levels = GDLevels().load()  # Загрузка

levels.levels["k_0"]["k2"] = "test text"  # Изменение названия 1 уровня во вкладке Create

levels.save()  # Сохранение
