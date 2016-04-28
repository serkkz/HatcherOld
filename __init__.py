# -*- coding: utf-8 -*-
bl_info = {"name": "Tools", 
           "description": "Tools", 
           "author": "serg-kkz", 
           "version": (0, 1), 
           "blender": (2, 7, 6),
           "location": "3D view > Hatcher", 
           "warning": "", 
           "wiki_url": "", 
           "tracker_url": "",
           "category": "Panda3D"}

import bpy
from bpy.props import *
from bpy.types import PropertyGroup

from .panda3d_tools.properties import Hatcher_mat, Hatcher_obj, Hatcher_scene, Hatcher_tex, Hatcher_list_egg_add

from .panda3d_tools.list_hather import List_EGG_File

# Импорт класса для расширения панели UV map
from .panda3d_tools.uv_add_menu import UV_unwrap_menu

# Импорт классов для отображения интерфейса
from .panda3d_tools.setting import Setting
from .panda3d_tools.collide import Collide
from .panda3d_tools.texture import Textures
from .panda3d_tools.material import Materials
from .panda3d_tools.vertex import Vertexs
from .panda3d_tools.polygon import Polygons
from .panda3d_tools.include_egg import Include, Add_file, Del_file
from .panda3d_tools.info import Info, Help_author_RU, Help_Page_Project_RU, Help_author_ENG, Help_Page_Project_ENG, Get_Addon, Egg_Syntax, Egg_Syntax_Full

# Импорт классов кнопок
from .panda3d_tools.export_standart import Export_egg
from .panda3d_tools.edit_map_uv import Edit_UV

def draw_item(self, context):
    layout = self.layout
    layout.menu(UV_unwrap_menu.bl_idname)

def register():

    bpy.utils.register_class(UV_unwrap_menu)
    
    # Добавление нового пункта меню в UV map
    bpy.types.IMAGE_HT_header.append(draw_item)
    
    bpy.utils.register_class(List_EGG_File)   

    bpy.utils.register_class(Setting)
    bpy.utils.register_class(Collide)
    bpy.utils.register_class(Textures)
    bpy.utils.register_class(Materials)
    bpy.utils.register_class(Vertexs)
    bpy.utils.register_class(Polygons)
    bpy.utils.register_class(Include)
    bpy.utils.register_class(Info)
    bpy.utils.register_class(Help_author_RU)
    bpy.utils.register_class(Help_Page_Project_RU)
    bpy.utils.register_class(Help_author_ENG)
    bpy.utils.register_class(Help_Page_Project_ENG)
    bpy.utils.register_class(Get_Addon)
    bpy.utils.register_class(Egg_Syntax)
    bpy.utils.register_class(Egg_Syntax_Full)
        
    bpy.utils.register_class(Export_egg)
    bpy.utils.register_class(Add_file)
    bpy.utils.register_class(Del_file)
    bpy.utils.register_class(Edit_UV)
    
    bpy.utils.register_class(Hatcher_scene)
    bpy.utils.register_class(Hatcher_mat)
    bpy.utils.register_class(Hatcher_obj)
    bpy.utils.register_class(Hatcher_tex)
    bpy.utils.register_class(Hatcher_list_egg_add)

    # Переменые для добавленных значений материалов
    bpy.types.Scene.hatcher = PointerProperty(type=Hatcher_scene)    
    
    # Переменые для добавленных значений материалов
    bpy.types.Material.hatcher = PointerProperty(type=Hatcher_mat)
    
    # Переменые для добавленных значений объектов
    bpy.types.Object.hatcher = PointerProperty(type=Hatcher_obj)

    # Переменые для добавленных значений текстур
    bpy.types.Texture.hatcher = PointerProperty(type=Hatcher_tex)
    
    bpy.types.Object.hatcher_list_egg_groop = CollectionProperty(type=Hatcher_list_egg_add)

def unregister():

    bpy.utils.unregister_class(UV_unwrap_menu)
    
    # Удаление пункта меню в UV map
    bpy.types.IMAGE_HT_header.remove(draw_item)  
    
    bpy.utils.unregister_class(List_EGG_File)
    
    bpy.utils.unregister_class(Setting)
    bpy.utils.unregister_class(Collide)
    bpy.utils.unregister_class(Textures)
    bpy.utils.unregister_class(Materials)
    bpy.utils.unregister_class(Vertexs)
    bpy.utils.unregister_class(Polygons)
    bpy.utils.unregister_class(Include)
    bpy.utils.unregister_class(Info)
    bpy.utils.unregister_class(Help_author_RU)
    bpy.utils.unregister_class(Help_Page_Project_RU)
    bpy.utils.unregister_class(Help_author_ENG)
    bpy.utils.unregister_class(Help_Page_Project_ENG)
    bpy.utils.unregister_class(Get_Addon)
    bpy.utils.unregister_class(Egg_Syntax)
    bpy.utils.unregister_class(Egg_Syntax_Full)
    
    bpy.utils.unregister_class(Export_egg)
    bpy.utils.unregister_class(Add_file)
    bpy.utils.unregister_class(Del_file)
    bpy.utils.unregister_class(Edit_UV)
    
    bpy.utils.unregister_class(Hatcher_scene)
    bpy.utils.unregister_class(Hatcher_mat)
    bpy.utils.unregister_class(Hatcher_obj)
    bpy.utils.unregister_class(Hatcher_tex)
    bpy.utils.unregister_class(Hatcher_list_egg_add)
    
    del bpy.types.Material.hatcher
    del bpy.types.Object.hatcher
    del bpy.types.Scene.hatcher
    del bpy.types.Texture.hatcher
    del bpy.types.Object.hatcher_list_egg_groop
