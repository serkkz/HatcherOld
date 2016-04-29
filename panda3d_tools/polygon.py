# -*- coding: utf-8 -*-
import bpy
from bpy.props import *
from bpy.types import (PropertyGroup)

class Polygons(bpy.types.Panel):
    bl_label = "Polygon"  # Имя панели
    bl_space_type = 'VIEW_3D'  # В каком окне
    bl_region_type = 'TOOLS'  # Место распаложения
    bl_category = 'Hatcher version 0.1'  # Название вкладки
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        
        layout = self.layout
        
        if context.active_object.mode == 'EDIT':
        
            obj = context.edit_object 
            
            me = obj.data  
            
            bm = bmesh.from_edit_mesh(me) 
            
            # Кеш для выбраных полигонов
            cache_face_select = []
  
            for f in bm.faces:  
            
                if f.select:  
                
                    cache_face_select.append(f.normal)

            if cache_face_select != []:
            
                layout.label(text=str(cache_face_select))
                
            else:
            
                layout.label(text="No select face(s)")
                
            cache_face_select[:] = []

            bmesh.update_edit_mesh(me, True)
            
        else:
        
            layout.label(text="Set mode EDIT")
        
