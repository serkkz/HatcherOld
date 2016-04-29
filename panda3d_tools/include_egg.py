# -*- coding: utf-8 -*-
import bpy
from bpy.props import IntProperty, CollectionProperty
from bpy.types import Panel, UIList

class Add_file(bpy.types.Operator):
    bl_idname = "mesh.add_file"
    bl_label = "Generator"

    def invoke(self, context, event):
        bpy.context.object.hatcher_list_egg_groop.add()
        return {'FINISHED'}

class Del_file(bpy.types.Operator):
    bl_idname = "mesh.remove_file"
    bl_label = "Generator"

    def invoke(self, context, event):
        bpy.context.object.hatcher_list_egg_groop.remove(bpy.context.object.hatcher.zones_index)
        return {'FINISHED'}

class Include(bpy.types.Panel):

    bl_label = "Included in group object"  # Имя панели
    bl_space_type = 'VIEW_3D'  # В каком окне
    bl_region_type = 'TOOLS'  # Место распаложения
    bl_category = 'Hatcher version 0.1'  # Название вкладки

    def draw(self, context):
        #Общий слой для элементов
        layout = self.layout
        
        if bpy.context.active_object.type == "MESH":
        
            obj = context.object
            layout.template_list("List_EGG_File", "", obj, "hatcher_list_egg_groop", obj.hatcher, "zones_index")
        
            # Кнопка экспорта модели
            layout.operator("mesh.add_file", text="Add file egg")
        
            # Кнопка экспорта модели
            layout.operator("mesh.remove_file", text="Remove file egg")
            
        else:
            layout.label(text="No select mesh")
