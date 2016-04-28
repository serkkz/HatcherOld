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
        layout.label(text="Dummy")
        