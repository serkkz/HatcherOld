# -*- coding: utf-8 -*-
import bpy
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

    bl_label = "Includes egg file"  # Имя панели
    bl_space_type = 'VIEW_3D'  # В каком окне
    bl_region_type = 'TOOLS'  # Место распаложения
    bl_category = 'Hatcher version 0.1'  # Название вкладки

    def draw(self, context):
        
        #Общий слой для элементов
        layout = self.layout
        
        row = layout.row()

        if bpy.context.active_object.type == "MESH":
        
            obj = context.object
            row.template_list("List_EGG_File", "", obj, "hatcher_list_egg_groop", obj.hatcher, "zones_index", rows=1)
            
            col = row.column(align=True)
            
            # Кнопка добавления модели           
            col.operator("mesh.add_file", icon='ZOOMIN', text="")
            
            # Кнопка удаления модели 
            col.operator("mesh.remove_file", icon='ZOOMOUT', text="")
 
        else:
            
            layout.label(text="No select mesh")
