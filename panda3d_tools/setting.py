# -*- coding: utf-8 -*-
import bpy
import os
from bpy.props import *
from bpy.types import (PropertyGroup)

# Класс интерфейса экспортера
class Setting(bpy.types.Panel):

    bl_label = "Setting export"  # Имя панели
    bl_space_type = 'VIEW_3D'  # В каком окне
    bl_region_type = 'TOOLS'  # Место распаложения
    bl_category = 'Hatcher version 0.3'  # Название вкладки

    def draw(self, context):
        #Общий слой для элементов
        layout = self.layout

        # Выбор директории где установленна панда
        layout.prop(context.scene.hatcher, 'dir_Panda3D', text='Installed Panda3D')
        
        if bpy.context.active_object != None:
            if bpy.context.active_object.type == "MESH":

                # Выбор директории для сохранения файла
                layout.prop(context.object.hatcher, 'path_export_egg', text='Path export model')
                
                # Поле для задания имени файла
                layout.prop(context.object, "name", text='Name file')
                
                # Вывод листа с выбором типа рендера
                layout.prop(context.object.hatcher, "chexbox_typerender", text="Render system")
                
                if context.object.hatcher.chexbox_typerender == 'Standard':
                
                    # Проверяем указан ли путь экспорта у объекта
                    if bpy.context.active_object.hatcher.path_export_egg != '':
                
                        # Вывод листа с осями верха для модели
                        layout.prop(bpy.context.active_object.hatcher, "coordinatesystem", text="Coordinate system")
                
                        # Кнопка экспорта модели
                        layout.operator("mesh.generate_egg", text="Export model (default egg)")

                        # Проверяем указан ли путь установленой панды
                        if bpy.context.scene.hatcher.dir_Panda3D != '':
                        
                            # Адрес утилиты конвертора в bam
                            ful_adress_util_egg_bam = os.path.join(bpy.context.scene.hatcher.dir_Panda3D, "bin", "egg2bam.exe")

                            util_list = self.layout.split()

                            # Проверка существования файла утилиты конвертации
                            if os.path.isfile(ful_adress_util_egg_bam):
                        
                                convert_bam = util_list.row()
                                convert_bam.prop(bpy.context.active_object.hatcher, "chexbox_convert_bam", text = "Convert to bam")
                                convert_bam.active = True
                            
                            else:
                                util_list.label(text='egg2bam.exe not found')
                            
                            # Адрес утилиты просмотра
                            ful_adress_util_view = os.path.join(bpy.context.scene.hatcher.dir_Panda3D, "bin", "pview.exe")                           

                            # Проверка существования файла утилиты просмотра
                            if os.path.isfile(ful_adress_util_view):
                        
                                view_model = util_list.row()
                                view_model.prop(bpy.context.active_object.hatcher, "chexbox_view_model", text = "View model")
                                view_model.active = True
                            
                            else:
                                util_list.label(text='pview.exe not found')

                        else:
                            layout.label(text='For access to utils specify the installation path panda3d')    
                               
                    else:
                        layout.label(text='Set path export !!!')
                        
                else:
                    layout.label(text='No supported, but I think about it') 
                    
            else:
                layout.label(text='Select the type of mesh object')  

        else:
            layout.label(text='active object is not selected')
