# -*- coding: utf-8 -*-
import bpy
from bpy.props import *
from bpy.types import (PropertyGroup)

class Collide(bpy.types.Panel):
    bl_label = "Collide" # Имя панели
    bl_space_type = 'VIEW_3D' # В каком окне
    bl_region_type = 'TOOLS' # Место распаложения
    bl_category = 'Hatcher version 0.1' # Название вкладки
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout 

        if bpy.context.active_object.type == "MESH":
            # Вывод листа с осями верха для модели
            layout.prop(bpy.context.active_object.hatcher, "collide_type", text="Collide type")
            
            if bpy.context.active_object.hatcher.collide_type != 'None':
                
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_1", text="Flags 1")
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_2", text="Flags 2")
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_3", text="Flags 3")
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_4", text="Flags 4")
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_5", text="Flags 5")
                
        else:
            layout.label(text="no select mesh")
