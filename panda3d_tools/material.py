# -*- coding: utf-8 -*-
import bpy
from bpy.props import *
from bpy.types import (PropertyGroup)

# Класс для вывода дополнительной информации, не влияет на экспорт
class Materials(bpy.types.Panel):
    bl_label = "Material"  # Имя панели
    bl_space_type = 'VIEW_3D'  # В каком окне
    bl_region_type = 'TOOLS'  # Место распаложения
    bl_category = 'Hatcher version 0.1'  # Название вкладки
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout 

        if hasattr(bpy.context.active_object.active_material, 'name'):
        
            # Общий фрейм для атрибутов с обводкой
            frameMat = layout.box()
            
            # Разделяем по вертикали
            frame_name = frameMat.split().row()
            frame_name.prop(bpy.context.active_object.active_material, "name", text='Slot name')
            frame_name.prop(bpy.context.active_object.active_material.hatcher, "chexbox_mat_wr")
            
            # Проверка переключателя
            if bpy.context.active_object.active_material.hatcher.chexbox_mat_wr:
                frameMat.active = True
            else:
                frameMat.active = False
                
            # Создаем еще фрем для параметров RGB Diffuse
            diffuse = frameMat.box().row()
            diffuse.label(text="Diffuse:")
            diffuse.label(text="R:  %3.3f" % bpy.context.object.active_material.diffuse_color[0])
            diffuse.label(text="G:  %3.3f" % bpy.context.object.active_material.diffuse_color[1])
            diffuse.label(text="B:  %3.3f" % bpy.context.object.active_material.diffuse_color[2])
            diffuse.label(text="A:  %3.3f" % bpy.context.object.active_material.hatcher.diffuse_color[3])
            diffuse.prop(bpy.context.active_object.active_material.hatcher, "diffuse_color", text="")
            
            # Создаем еще фрем для параметров RGB ambient
            ambient = frameMat.box().row()
            ambient.label(text="Ambient:")
            ambient.label(text="R:  %3.3f" % bpy.context.object.active_material.hatcher.ambient_color[0])
            ambient.label(text="G:  %3.3f" % bpy.context.object.active_material.hatcher.ambient_color[1])
            ambient.label(text="B:  %3.3f" % bpy.context.object.active_material.hatcher.ambient_color[2])
            ambient.label(text="A:  %3.3f" % bpy.context.object.active_material.hatcher.ambient_color[3])
            ambient.prop(bpy.context.active_object.active_material.hatcher, "ambient_color", text="")
            
            # Создаем еще фрем для параметров RGB emit
            emit = frameMat.box().row()
            emit.label(text="Emit:")
            emit.label(text="R:  %3.3f" % bpy.context.object.active_material.hatcher.emit_color[0])
            emit.label(text="G:  %3.3f" % bpy.context.object.active_material.hatcher.emit_color[1])
            emit.label(text="B:  %3.3f" % bpy.context.object.active_material.hatcher.emit_color[2])
            emit.label(text="A:  %3.3f" % bpy.context.object.active_material.hatcher.emit_color[3])
            emit.prop(bpy.context.active_object.active_material.hatcher, "emit_color", text="")

            # Создаем еще фрем для параметров RGB specular
            spec = frameMat.box().row()
            spec.label(text="Specular:")
            spec.label(text="R:  %3.3f" % bpy.context.object.active_material.hatcher.specular_color[0])
            spec.label(text="G:  %3.3f" % bpy.context.object.active_material.hatcher.specular_color[1])
            spec.label(text="B:  %3.3f" % bpy.context.object.active_material.hatcher.specular_color[2])
            spec.label(text="A:  %3.3f" % bpy.context.object.active_material.hatcher.specular_color[3])
            spec.prop(bpy.context.active_object.active_material.hatcher, "specular_color", text="")

            # Создаем еще фрем для параметров RGB shininess
            shininess = frameMat.box().row()
            shininess.label(text="Shininess:")
            shininess.prop(bpy.context.active_object.active_material.hatcher, "shininess", text="")

        else:
            layout.label(text="no material contains")
        