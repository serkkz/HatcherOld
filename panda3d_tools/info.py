# -*- coding: utf-8 -*-
import bpy
from bpy.props import *
from bpy.types import (PropertyGroup)


class Help_Page_Project_RU(bpy.types.Operator):
    bl_idname = "mesh.help_page_project_ru"
    bl_label = "Generator"
    
    def invoke(self, context, event):
   
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url="http://panda3d.org.ru/forum/3-324-1#5147")
        
        return {"FINISHED"}

class Help_author_RU(bpy.types.Operator):
    bl_idname = "mesh.help_author_ru"
    bl_label = "Generator"
    
    def invoke(self, context, event):
   
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url="http://panda3d.org.ru/index/8-0-serg~kkz")
        
        return {"FINISHED"}
    

class Help_Page_Project_ENG(bpy.types.Operator):
    bl_idname = "mesh.help_page_project_eng"
    bl_label = "Generator"
    
    def invoke(self, context, event):
   
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url="http://www.panda3d.org/forums/viewtopic.php?f=2&t=18788")
        
        return {"FINISHED"}

class Help_author_ENG(bpy.types.Operator):
    bl_idname = "mesh.help_author_eng"
    bl_label = "Generator"
    
    def invoke(self, context, event):
   
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url="https://www.panda3d.org/forums/memberlist.php?mode=viewprofile&u=11192&sid=6deff07532c9eb2bcb8ac7bd5ca3c30e")
        
        return {"FINISHED"}

class Get_Addon(bpy.types.Operator):
    bl_idname = "mesh.get_addon"
    bl_label = "Generator"
    
    def invoke(self, context, event):
   
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url="https://github.com/serkkz/Hatcher")
        
        return {"FINISHED"}
        
class Egg_Syntax(bpy.types.Operator):
    bl_idname = "mesh.egg_syntax"
    bl_label = "Generator"
    
    def invoke(self, context, event):
   
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url="https://www.panda3d.org/manual/index.php/Egg_Syntax")
        
        return {"FINISHED"}
        
class Egg_Syntax_Full(bpy.types.Operator):
    bl_idname = "mesh.egg_syntax_full"
    bl_label = "Generator"
    
    def invoke(self, context, event):
   
        bpy.ops.wm.url_open("INVOKE_DEFAULT", url="https://github.com/panda3d/panda3d/blob/master/panda/src/doc/eggSyntax.txt")
        
        return {"FINISHED"}

class Info(bpy.types.Panel):
    bl_label = "Info"  # Имя панели
    bl_space_type = 'VIEW_3D'  # В каком окне
    bl_region_type = 'TOOLS'  # Место распаложения
    bl_category = 'Hatcher version 0.1'  # Название вкладки
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout 
        
        box1 = layout.box()
        
        row1 = box1.row()
        row1.label(text="Project page: ")
        row1.operator("mesh.help_page_project_ru", icon="URL", text="panda3d.org.ru")  
        

        row2 = box1.row()
        row2.label(text="Author profile: ")
        row2.operator("mesh.help_author_ru", icon="URL", text="panda3d.org.ru")
        
        box2 = layout.box()
        
        row3 = box2.row()
        row3.label(text="Project page: ")
        row3.operator("mesh.help_page_project_eng", icon="URL", text="panda3d.org")  
        
        row4 = box2.row()
        row4.label(text="Author profile: ")
        row4.operator("mesh.help_author_eng", icon="URL", text="panda3d.org")
        
        box3 = layout.box()
        
        row5 = box3.row()
        row5.label(text="Get add-on: ")
        row5.operator("mesh.get_addon", icon="URL", text="github.com")

        box4 = layout.box()
        
        row6 = box4.row()
        row6.label(text="Egg_Syntax")
        row6.operator("mesh.egg_syntax", icon="URL", text="panda3d.org")

        row7 = box4.row()
        row7.label(text="Egg_Syntax(Full)")
        row7.operator("mesh.egg_syntax_full", icon="URL", text="github.com")
