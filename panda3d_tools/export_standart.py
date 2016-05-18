# -*- coding: utf-8 -*-
import bpy
import bmesh
import io
import os
import subprocess

from ..panda3d_tools.util_dir_file import dir_create_save, cor_path

# Коректировка пути для панды
def corrpath(path, type=None):
    raw = '{!r}'.format(path)
    rezr = raw.replace("\\", "/").replace("//", "/").replace("'", '')
    if type:
        rez = rezr.replace("\\", "/")
    else:
        u = rezr[0]
        p = rezr[:].split('/')
        x = p[1:]
        x.insert(0, p[0].lower().replace(":", ""))
        rez = '/'+'/'.join(x)
    return rez

#Получение относительной директории и относительной директории с именем файла
def getRelative(pathstart, dircopytex, texadress):
    # Принимат полный адрес файла, для извлечения имени
    # Путь экспорта модели
    # Путь копирования текстуры полный
    # Возращает кортеж, относительный путь и вычисленый полный путь с именем.

    # Раскладываем адрес изображения на директорию и имя
    (dirName, fileName) = os.path.split(texadress)
    # Вычесление относительного пути
    relpath = os.path.relpath(dircopytex, pathstart)
    # К директории добавляем имя файла, и получаем полный относительный адрес
    fulrelpath = os.path.join(relpath, fileName)
    # Возращаем скоррективыный относительный путь
    return (relpath, fulrelpath)

# Класс для экспорта egg
class Export_egg(bpy.types.Operator):
    bl_idname = "mesh.generate_egg"
    bl_label = "Generator"

    def invoke(self, context, event):
    
        # Создаем виртуальный файл в памяти
        egg = io.StringIO()
        
        # Путь экспорта меша
        path_export = bpy.data.objects[context.object.name].hatcher.path_export_egg
        
        # Кеш для имен материалов, которые были извлечены из полигона
        nameMat_cache = []
        
        # Кеш для текстур
        texture_cache = []
        
        # Кеш для материалов
        material_cache = []

        # Кеш для пула вертексов, сюда будем помещать чтоб записать в файл в нужном порядке.
        vertex_cache = []
        
        # Кеш для пула полигонов, сюда будем помещать чтоб записать в файл в нужном порядке.
        polygons_cache = []
        
        # Запись строки о системе координат
        egg.write('<CoordinateSystem> { ' + bpy.data.objects[context.object.name].hatcher.coordinatesystem + ' }\n\n')
            
        # Запись о версии hatcher
        egg.write('<Comment> { "Exporter Hatcher version 0.3" }\n\n')

        # Кеш для группы вершин которые состовляют один полигон.
        vert = []

        # Проверка есть ли активные текстурные координаты у объекта
        if bpy.context.object.data.uv_layers.active:
            # Если есть то создаем переменную с данными
            uv_layer = bpy.context.object.data.uv_layers.active.data
        else:
            uv_layer = None

        # Открываем пул вершин
        vertex_cache.append(' <VertexPool> {} {{\n'.format(bpy.context.object.name))

        id_vertex = 0

        # Перебираем полигоны активного объкта
        for poly in bpy.context.object.data.polygons:
        
            for i in poly.vertices[:]:
            
                # Получаем данные из вершин
                vert_data = bpy.context.object.data.vertices[i]

                # Открываем вершину 
                vertex_cache.append('  <Vertex> {} {{ {} \n'.format(id_vertex, '{0:.6f}'.format(vert_data.co[0]).rstrip('0').rstrip('.') +' '+ '{0:.6f}'.format(vert_data.co[1]).rstrip('0').rstrip('.') +' '+  '{0:.6f}'.format(vert_data.co[2]).rstrip('0').rstrip('.')))

                # Проверка используется ли сглаживание 
                if poly.use_smooth:
                
                    vertex_cache.append('   <Normal> {{ {} {} {} }}\n'.format('{0:.6f}'.format(vert_data.normal[0]).rstrip('0').rstrip('.'), '{0:.6f}'.format(vert_data.normal[1]).rstrip('0').rstrip('.'), '{0:.6f}'.format(vert_data.normal[2]).rstrip('0').rstrip('.')))

                # Проверка статуса переменой с текстурными координатами. 
                if uv_layer:
                
                    # Активный слой записываем без имени UV
                    
                    print ('   <UV> {{ {} {} }}'.format('{0:.6f}'.format(uv_layer[id_vertex].uv[0]).rstrip('0').rstrip('.'), '{0:.1f}'.format(uv_layer[id_vertex].uv[1]).rstrip('0').rstrip('.'))) 
                    
                    vertex_cache.append('   <UV> {{ {} {} }}\n'.format('{0:.6f}'.format(uv_layer[id_vertex].uv[0]).rstrip('0').rstrip('.'), '{0:.6f}'.format(uv_layer[id_vertex].uv[1]).rstrip('0').rstrip('.')))         

                    # Проходим по не активным слоям
                    for uv in bpy.context.object.data.uv_layers:

                        # Если имя не равно активному слою, то записываем.
                        if uv.name != bpy.context.object.data.uv_layers.active.name:

                            vertex_cache.append('   <UV> {} {{ {} {} }}\n'.format(uv.name,'{0:.6f}'.format(uv.data[id_vertex].uv[0]).rstrip('0').rstrip('.'), '{0:.6f}'.format(uv.data[id_vertex].uv[1]).rstrip('0').rstrip('.')))

                # Закрываем  вершину
                vertex_cache.append('  }\n')
                
                id_vertex += 1
            
            # Всего вершин из которых состоит полигон
            total_vert = poly.loop_total
                
            # Перебираем вершины для извлечения информации
            for i in range(total_vert):
                
                # Запись в кеш с корректировкой номера
                vert.append(str(poly.loop_start + i))

            # Открываем группу полигонов
            polygons_cache.append(' <Polygon> {id} {{ \n'.format(id = poly.index))

            # Проверяем есть ли слоты с материалом
            if context.object.material_slots.items() != []:
            
                # Проверяем флажек записи материала
                if bpy.context.active_object.active_material.hatcher.chexbox_mat_wr:

                    # Получаем имя материала 
                    name_mat = bpy.context.active_object.material_slots[poly.material_index]
                    
                    if name_mat.name != '':

                        polygons_cache.append('  <MRef> {{ {} }}\n'.format(name_mat.name)) 
            
                        # Добавляем имя материала в кеш для дальнейшего использования в экспорте
                        nameMat_cache.append(name_mat.name) 

                        for tex_data in bpy.context.active_object.material_slots[poly.material_index].material.texture_slots:
                        
                            if tex_data:
                            
                                # Проверка типа текстуры
                                if hasattr(tex_data.texture, 'image'):
                                
                                    # Проверка есть ли у текстуры атрибут путь файла изображения
                                    if hasattr(tex_data.texture.image, 'filepath'):
                            
                                        polygons_cache.append('  <TRef> {{ {} }}\n'.format(tex_data.name))
                                       
            # Запись строки о направлении нормали
            polygons_cache.append('  <Normal> {{ {} {} {} }}\n'.format('{0:.6f}'.format(poly.normal[0]).rstrip('0').rstrip('.'), '{0:.6f}'.format(poly.normal[1]).rstrip('0').rstrip('.'), '{0:.6f}'.format(poly.normal[2]).rstrip('0').rstrip('.')))
            
            # Запись строки с номерами вершин из которых состоит полигон
            polygons_cache.append('  <VertexRef> {{ {} <Ref> {{ {} }} }}\n'.format(','.join(vert).replace(",", " "), bpy.context.object.name))
            
            # Закрываем группу полигонов
            polygons_cache.append('  }\n')
            
            # Очистка кеша для следующей группы вершин 
            vert[:] = []

        # Закрываем  пул вершин
        vertex_cache.append(' }\n\n')
        
        # Удаляем дубликаты, так как сюда заносились данные в цикле 
        list_mat_name = list(set(nameMat_cache))

        # Проверка есть ли имена материалов в списке
        if list_mat_name:
            
            # Проходим по списку
            for mat_name in list_mat_name:

                # Открываем материал
                material_cache.append('<Material> {} {{\n'.format(mat_name))
                
                material_cache.append(' <Scalar> diffr {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.diffuse_color[0]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> diffg {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.diffuse_color[1]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> diffb {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.diffuse_color[2]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> diffa {{ {} }}\n\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.diffuse_color[3]).rstrip('0').rstrip('.')))

                material_cache.append(' <Scalar> ambr {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.ambient_color[0]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> ambg {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.ambient_color[1]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> ambb {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.ambient_color[2]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> amba {{ {} }}\n\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.ambient_color[3]).rstrip('0').rstrip('.')))
                
                material_cache.append(' <Scalar> emitr {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.emit_color[0]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> emitg {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.emit_color[1]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> emitb {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.emit_color[2]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> emita {{ {} }}\n\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.emit_color[3]).rstrip('0').rstrip('.')))

                material_cache.append(' <Scalar> specr {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.specular_color[0]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> specg {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.specular_color[1]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> specb {{ {} }}\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.specular_color[2]).rstrip('0').rstrip('.')))
                material_cache.append(' <Scalar> speca {{ {} }}\n\n'.format('{0:.6f}'.format(bpy.context.object.material_slots[mat_name].material.hatcher.specular_color[3]).rstrip('0').rstrip('.')))
                
                material_cache.append(' <Scalar> shininess {{ {} }}\n'.format(bpy.context.object.material_slots[mat_name].material.hatcher.shininess))
                

                list_tex = bpy.context.object.material_slots[mat_name].material.texture_slots.items()
                
                for texture in list_tex:
                
                    slot_tex = texture[1]
                    
                    # Проверяем флажок записи текстуры
                    if slot_tex.texture.hatcher.chexbox_tex_wr:

                        # Проверка типа текстуры
                        if hasattr(slot_tex.texture, 'image'):                    
                    
                            # Проверка есть ли у текстуры атрибут путь файла изображения
                            if hasattr(slot_tex.texture.image, 'filepath'):

                                #Открываем текстуры
                                texture_cache.append('<Texture> {} {{\n'.format(slot_tex.name))
                                
                                texture_cache.append(' "{}"\n'.format(dir_create_save(slot_tex.texture.hatcher.set_dir_rel, path_export, slot_tex.texture.image.filepath)))
                                
                                # Проверяем есть ли адрес альфа файла
                                if slot_tex.texture.hatcher.alfa_file:
                                   
                                    # Проверяем существует ли файл
                                    if os.path.isfile(slot_tex.texture.hatcher.alfa_file):
                                    
                                        # Проверяем тип пути
                                        if slot_tex.texture.hatcher.tex_dir_alpha_type == 'Absolute':
                                    
                                            texture_cache.append(' <Scalar> alpha-file {{ "{}" }}\n'.format(cor_path(slot_tex.texture.hatcher.alfa_file)))
                                            
                                        else:  
                                            texture_cache.append(' <Scalar> alpha-file {{ "{}" }}\n'.format(dir_create_save(slot_tex.texture.hatcher.alfa_file_save, path_export, slot_tex.texture.hatcher.alfa_file)))
                                            
                                    texture_cache.append(' <Scalar> alpha-file-channel {{ {} }}\n'.format(slot_tex.texture.hatcher.alpha_file_channel))           

                                texture_cache.append(' <Scalar> format {{ {} }}\n'.format(slot_tex.texture.hatcher.format_tex))
                                
                                texture_cache.append(' <Scalar> alpha {{ {} }}\n'.format(slot_tex.texture.hatcher.alpha_stat))
                                
                                texture_cache.append(' <Scalar> compression {{ {} }}\n'.format(slot_tex.texture.hatcher.value_compr))
                                
                                texture_cache.append(' <Scalar> envtype {{ {} }}\n'.format(slot_tex.texture.hatcher.value_envtype))
                                
                                texture_cache.append(' <Scalar> anisotropic-degree {{ {} }}\n'.format(slot_tex.texture.hatcher.value_anisotropic))
                                
                                texture_cache.append(' <Scalar> wrapu {{ {} }}\n'.format(slot_tex.texture.hatcher.value_wrapu))
                                
                                texture_cache.append(' <Scalar> wrapv {{ {} }}\n'.format(slot_tex.texture.hatcher.value_wrapv))
                                
                                texture_cache.append(' <Scalar> minfilter {{ {} }}\n'.format(slot_tex.texture.hatcher.value_minfilter))
                                
                                texture_cache.append(' <Scalar> magfilter {{ {} }}\n'.format(slot_tex.texture.hatcher.value_magfilter))

                                texture_cache.append('}\n\n')

                # Закрываем материал
                material_cache.append('}\n\n')

        # Записываем все текстуры в виртуальный файл
        for data_tex in texture_cache:
        
            egg.write(data_tex) 
                
                
        # Записываем все материалы в виртуальный файл
        for data_mat in material_cache:
        
            egg.write(data_mat)

        # Открываем группу объекта 
        egg.write('<Group>  {} {{\n'.format(bpy.context.object.name))
        
        egg.write(' <Scalar> collide-mask {{ {} }}\n'.format(bpy.context.active_object.hatcher.collide_mask))
        egg.write(' <Scalar> from-collide-mask {{ {} }}\n'.format(bpy.context.active_object.hatcher.from_collide_mask))
        egg.write(' <Scalar> into-collide-mask {{ {} }}\n'.format(bpy.context.active_object.hatcher.into_collide_mask))

        list_flags = []

        context.object.hatcher.collide_type
        
        if context.object.hatcher.collide_type != "None":
        
            if context.object.hatcher.collide_flag_1 != "None":
            
                list_flags.append(context.object.hatcher.collide_flag_1)
                
            if context.object.hatcher.collide_flag_2 != "None":
            
                list_flags.append(context.object.hatcher.collide_flag_2)
                
            if context.object.hatcher.collide_flag_3 != "None":
            
                list_flags.append(context.object.hatcher.collide_flag_3)
                
            if context.object.hatcher.collide_flag_4 != "None":
            
                list_flags.append(context.object.hatcher.collide_flag_4)
                
            if context.object.hatcher.collide_flag_5 != "None":
            
                list_flags.append(context.object.hatcher.collide_flag_5)
            
            # Проверка есть ли записанные флаги в списке
            if list_flags:
                
                # Записываем с флагами
                egg.write(' <Collide> {} {{ {} {} }}\n'.format(bpy.context.active_object.hatcher.collide_name, context.object.hatcher.collide_type, ','.join(list_flags).replace(",", " ")))

            else:
            
                # Записываем без флагами
                egg.write(' <Collide> {} {{ {} }}\n'.format(bpy.context.active_object.hatcher.collide_name, context.object.hatcher.collide_type))

        # Записываем все вершины в виртуальный файл
        for data_vert in vertex_cache:
        
            egg.write(data_vert)
             
        # Записываем все материалы в виртуальный файл
        for data_poly in polygons_cache:
        
            egg.write(data_poly)
        
        # Добавляем файлы
        
        # Проверяем есть ли списке egg файлы
        if context.object.hatcher_list_egg_groop.items() != []: 
        
            # Проходим по списку с egg файлами
            for data_egg_file in context.object.hatcher_list_egg_groop:
                
                # Проверяем указан ли адрес файла
                if data_egg_file.path_egg:

                    egg.write('<File> {{ "{}" }}\n'.format(cor_path(data_egg_file.path_egg)))
                 
        # Закрываем группу объекта
        egg.write('}')

        # Собираем адрес сохранения egg
        path_save = os.path.join(path_export, context.object.name)
    
        # Сохраняем файл
        with open(path_save + '.egg', 'w') as fd:
        
            fd.write(egg.getvalue())
            
            # Закрываем файл
            fd.close()
        
        # Закрываем виртуальный файл
        egg.close()
        
        if bpy.context.active_object.hatcher.chexbox_convert_bam:
        
            # Адрес утилиты конвертора в bam
            ful_adress_util_egg_bam = os.path.join(bpy.context.scene.hatcher.dir_Panda3D, "bin", "egg2bam.exe")
        
            egg_bam = subprocess.Popen(ful_adress_util_egg_bam+' -o '+str(path_save + '.bam')+' '+str(path_save + '.egg'), shell=True, stdout=subprocess.PIPE)
            out_egg_bam = egg_bam.stdout.readlines()
            
            if out_egg_bam:
                print (out_egg_bam)
            
            if bpy.context.active_object.hatcher.chexbox_view_model:
        
                # Адрес утилиты просмотра
                ful_adress_util_view = os.path.join(bpy.context.scene.hatcher.dir_Panda3D, "bin", "pview.exe") 
        
                view = subprocess.Popen(ful_adress_util_view+' '+str(path_save + '.bam'), shell=True, stdout=subprocess.PIPE)
                out_view = view.stdout.readlines()
                
                if out_view:
                    print (out_view)
                  
        else:
                    
            if bpy.context.active_object.hatcher.chexbox_view_model:
        
                # Адрес утилиты просмотра
                ful_adress_util_view = os.path.join(bpy.context.scene.hatcher.dir_Panda3D, "bin", "pview.exe") 
        
                view = subprocess.Popen(ful_adress_util_view+' '+str(path_save + '.egg'), shell=True, stdout=subprocess.PIPE)
                out_view = view.stdout.readlines()
                
                if out_view:
                    print (out_view)

        return {'FINISHED'}
