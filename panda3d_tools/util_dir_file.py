import os
import shutil
    
# Коректировка пути для панды
def cor_path(path, type=None):
    raw = '{!r}'.format(path)
    rezr = raw.replace("\\", "/").replace("//", "/").replace("'", '')
    if type:
        rez = rezr.replace("\\", "/")
    else:
        u = rezr[0]
        p = rezr[:].split('/')
        x = p[1:]
        x.insert(0, p[0].lower().replace(":", ""))
        rez = '/' + '/'.join(x)
    return rez

# Получение относительной директории и относительной директории с именем файла
def getRelative(path_export, dir_copy_tex, tex_adress):

    # Принимат полный адрес файла, для извлечения имени
    # Путь экспорта модели
    # Путь копирования текстуры полный
    
    # Раскладываем адрес изображения на директорию и имя
    (dirName, fileName) = os.path.split(tex_adress)
    
    # Вычесление относительного пути
    relpath = os.path.relpath(dir_copy_tex, path_export)
    
    # К директории добавляем имя файла, и получаем полный относительный адрес
    fulrelpath = os.path.join(relpath, fileName)

    # Возращаем скоррективыный относительный путь
    return (relpath, fulrelpath)

def dir_create_save(dir_copy_tex, path_export, tex_adress):

    # Сохраняем имя рабочей директории, чтоб вернуться
    fd = os.getcwd()
                                    
    # Проверяем существует ли директория
    if os.path.exists(path_export):
        # Переходим в директорию куда мы экспортирум еgg
        os.chdir(path_export)
    else:
        # Если нет, то создаем
        os.makedirs(path_export)
        # Переходим в директорию куда мы экспортирум еgg
        os.chdir(path_export)
                                 
    # Получаем относительный путь и относительный путь с именем файла
    # Относительно директории куда экспортитируем egg
    (relpath, fulrelpath) = getRelative(path_export, dir_copy_tex, tex_adress)

    # Проверяем существует ли директория
    if os.path.exists(relpath):
                            
        # Копируем текстуру
        shutil.copy(tex_adress, relpath)
                                
    else:
                            
        # Если нет, то создаем
        os.makedirs(relpath)

        # Копируем текстуру
        shutil.copy(tex_adress, relpath)
                                
    # Возращаемся назад в рабочую директорию
    os.chdir(fd)
                                
    # Коректируем путь для панды
    path = cor_path(fulrelpath, type=1)

    return path