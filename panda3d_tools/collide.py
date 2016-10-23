# -*- coding: utf-8 -*-
import bpy
from bpy.props import *
from bpy.types import (PropertyGroup)

class Collide(bpy.types.Panel):
    bl_label = "Collide" # Имя панели
    bl_space_type = 'VIEW_3D' # В каком окне
    bl_region_type = 'TOOLS' # Место распаложения
    bl_category = 'Hatcher version 0.3' # Название вкладки
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout 

        if bpy.context.active_object.type == "MESH":
        
            layout.prop(bpy.context.active_object.hatcher, "collide_mask", text="Mask")
            layout.prop(bpy.context.active_object.hatcher, "from_collide_mask", text="From mask")
            layout.prop(bpy.context.active_object.hatcher, "into_collide_mask", text="Into mask")
        
            layout.prop(bpy.context.active_object.hatcher, "collide_type", text="Type")
            
            if bpy.context.active_object.hatcher.collide_type != 'None':
                
                layout.prop(bpy.context.active_object.hatcher, "collide_name", text="Name")
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_1", text="Flag 1")
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_2", text="Flag 2")
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_3", text="Flag 3")
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_4", text="Flag 4")
                layout.prop(bpy.context.active_object.hatcher, "collide_flag_5", text="Flag 5")

        else:
            layout.label(text="no select mesh")
