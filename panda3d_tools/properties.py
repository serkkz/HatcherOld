# -*- coding: utf-8 -*-
import bpy
from bpy.props import *
from bpy.types import (PropertyGroup)
from bpy.types import UIList

def diffuse_color_update(self, context):
    bpy.context.object.active_material.diffuse_color = (bpy.context.object.active_material.hatcher.diffuse_color[0], bpy.context.object.active_material.hatcher.diffuse_color[1], bpy.context.object.active_material.hatcher.diffuse_color[2])
    
def ambient_update(self, context):
    listval = [bpy.context.object.active_material.hatcher.ambient_color[0], bpy.context.object.active_material.hatcher.ambient_color[1], bpy.context.object.active_material.hatcher.ambient_color[2]]
    listval.sort()
    bpy.context.object.active_material.ambient = listval[2]
    
def emit_update(self, context):
    listval = [bpy.context.object.active_material.hatcher.emit_color[0], bpy.context.object.active_material.hatcher.emit_color[1], bpy.context.object.active_material.hatcher.emit_color[2]]
    listval.sort()
    bpy.context.object.active_material.emit = listval[2]*2 

def specular_color_update(self, context):
    bpy.context.object.active_material.specular_color = (bpy.context.object.active_material.hatcher.specular_color[0], bpy.context.object.active_material.hatcher.specular_color[1], bpy.context.object.active_material.hatcher.specular_color[2])

def shininess_update(self, context):
    bpy.context.object.active_material.specular_hardness = bpy.context.object.active_material.hatcher.shininess*3.9921875

# Xранит пользовательские даные для текстур
class Hatcher_tex(PropertyGroup):

    chexbox_tex_wr = BoolProperty(name="", description="Record string of texture", default=True)
    
    tex_dir_type = EnumProperty(items=(('Absolute', "Absolute", ""), ('Relative', "Relative", "")), default='Absolute')
    
    set_dir_rel = StringProperty(default='textures', subtype='DIR_PATH', description="")
    
    alfa_file = StringProperty(subtype='FILE_PATH')
    
    alfa_file_save = StringProperty(default='textures', subtype='FILE_PATH')
    
    tex_dir_alpha_type = EnumProperty(items=(('Absolute', "Absolute", ""), ('Relative', "Relative", "")), default='Absolute')
    
    alpha_file_channel = EnumProperty(items=(('0', "0", ""), ('1', "1", ""), ('2', "2", ""), ('3', "3", ""), ('4', "4", "")), default='0')
    
    format_tex = EnumProperty(items=(
        ('RGBA', "RGBA", ""), ('RGBM', "RGBM", ""), ('RGBA12', "RGBA12", ""), ('RGBA8', "RGBA8", ""),
        ('RGBA4', "RGBA4", ""), ('RGB', "RGB", ""), ('RGB12', "RGB12", ""), ('RGB8', "RGB8", ""), ('RGB5', "RGB5", ""),
        ('RGB332', "RGB332", ""), ('LUMINANCE_ALPHA', "LUMINANCE_ALPHA", ""), ('RED', "RED", ""),
        ('GREEN', "GREEN", ""),
        ('BLUE', "BLUE", ""), ('ALPHA', "ALPHA", ""), ('LUMINANCE', "LUMINANCE", ""),), default='RGB')
        
    alpha_stat = EnumProperty(items=(
        ('OFF', "OFF", ""), ('ON', "ON", ""), ('BLEND', "BLEND", ""), ('BLEND_NO_OCCLUDE', "BLEND_NO_OCCLUDE", ""),
        ('MS', "MS", ""), ('MS_MASK', "MS_MASK", ""), ('BINARY', "BINARY", ""), ('DUAL', "DUAL", "")), default='OFF')
        
    value_compr = EnumProperty(items=(
        ('OFF', "OFF", ""), ('ON', "ON", ""), ('FXT1', "FXT1", ""), ('DXT1', "DXT1", ""),
        ('DXT2', "DXT2", ""), ('DXT3', "DXT3", ""), ('DXT4', "DXT4", ""), ('DXT5', "DXT5", "")), default='OFF')
        
    value_envtype = EnumProperty(items=(
        ('MODULATE', "MODULATE", ""), ('DECAL', "DECAL", ""), ('BLEND', "BLEND", ""), ('REPLACE', "REPLACE", ""),
        ('ADD', "ADD", ""), ('BLEND_COLOR_SCALE', "BLEND_COLOR_SCALE", ""), ('MODULATE_GLOW', "MODULATE_GLOW", ""),
        ('MODULATE_GLOSS', "MODULATE_GLOSS", ""), ('NORMAL', "NORMAL", ""), ('NORMAL_HEIGHT', "NORMAL_HEIGHT", ""),
        ('GLOW', "GLOW", ""), ('GLOSS', "GLOSS", ""), ('HEIGHT', "HEIGHT", ""),('SELECTOR', "SELECTOR", "")), default='MODULATE')

    value_minfilter = EnumProperty(items=(
        ('NEAREST', "NEAREST", ""), ('LINEAR', "LINEAR", ""), ('NEAREST_MIPMAP_NEAREST', "NEAREST_MIPMAP_NEAREST", ""),
        ('LINEAR_MIPMAP_NEAREST', "LINEAR_MIPMAP_NEAREST", ""), ('NEAREST_MIPMAP_LINEAR', "NEAREST_MIPMAP_LINEAR", ""),
        ('LINEAR_MIPMAP_LINEAR', "LINEAR_MIPMAP_LINEAR", "")), default='LINEAR_MIPMAP_LINEAR')
    value_magfilter = EnumProperty(items=(
        ('NEAREST', "NEAREST", ""), ('LINEAR', "LINEAR", ""), ('NEAREST_MIPMAP_NEAREST', "NEAREST_MIPMAP_NEAREST", ""),
        ('LINEAR_MIPMAP_NEAREST', "LINEAR_MIPMAP_NEAREST", ""), ('NEAREST_MIPMAP_LINEAR', "NEAREST_MIPMAP_LINEAR", ""),
        ('LINEAR_MIPMAP_LINEAR', "LINEAR_MIPMAP_LINEAR", "")), default='LINEAR_MIPMAP_LINEAR')

    value_anisotropic = EnumProperty(
        items=(('0', "0", ""), ('1', "1", ""), ('2', "2", ""), ('4', "4", ""), ('8', "8", ""), ('16', "16", "")),
        default='0')

    value_wrapu = EnumProperty(items=(
        ('REPEAT', "REPEAT", ""), ('CLAMP', "CLAMP", ""), ('MIRROR', "MIRROR", ""), ('MIRROR_ONCE', "MIRROR_ONCE", ""),
        ('BORDER_COLOR', "BORDER_COLOR", "")), default='REPEAT')
        
    value_wrapv = EnumProperty(items=(
        ('REPEAT', "REPEAT", ""), ('CLAMP', "CLAMP", ""), ('MIRROR', "MIRROR", ""), ('MIRROR_ONCE', "MIRROR_ONCE", ""),
        ('BORDER_COLOR', "BORDER_COLOR", "")), default='REPEAT')

        
# Xранит пользовательские даные для материалов
class Hatcher_mat(PropertyGroup):

    chexbox_mat_wr = BoolProperty(name="", description="Record string of material", default=True)
    
    diffuse_color = FloatVectorProperty(name = "", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, default = (0.8,0.8,0.8,1.0), update=lambda self, context: diffuse_color_update(self, context))
    
    ambient_color = FloatVectorProperty(name = "", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, default = (0.8,0.8,0.8,1.0), update=lambda self, context: ambient_update(self, context))
    
    emit_color = FloatVectorProperty(name = "", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, default = (0.0,0.0,0.0,1.0), update=lambda self, context: emit_update(self, context))
    
    specular_color = FloatVectorProperty(name = "", subtype = "COLOR", size = 4, min = 0.0, max = 1.0, default = (0.5,0.5,0.5,1.0), update=lambda self, context: specular_color_update(self, context))
    
    shininess = IntProperty(name = "",  min = 0, max = 128, default = 12, update=lambda self, context: shininess_update(self, context))
    
# Xранит пользовательские даные для объектов
class Hatcher_obj(PropertyGroup):

    # Переменная для хранеия адреса для сохранения egg
    path_export_egg = StringProperty(subtype='DIR_PATH')

    chexbox_convert_bam = BoolProperty(name="", description="Convert to bam", default=False)
    
    chexbox_view_model = BoolProperty(name="", description="View model", default=False)
    
    chexbox_typerender = EnumProperty(items=(('Standard', "Standard", ""), ('Pipeline', "Pipeline", "")), default='Standard') 
    
    coordinatesystem = EnumProperty(items=(('Z-Up', "Z-Up", ""), ('Y-Up', "Y-Up", "")), default='Z-Up')
    
    collide_type = EnumProperty(items=(('Plane', "Plane", ""), ('Polygon', "Polygon", ""), ('Polyset', "Polyset", ""), ('Sphere', "Sphere", ""), ('Box', "Box", ""), ('InvSphere', "InvSphere", ""), ('Tube', "Tube", ""), ('None', "None", "")), default='None')

    collide_flag_1 = EnumProperty( items=(('event', "event", ""), ('intangible', "intangible", ""), ('descend', "descend", ""), ('keep', "keep", ""), ('level', "level", ""), ('None', "None", "")), default='None')                    
    collide_flag_2 = EnumProperty(items=(('event', "event", ""), ('intangible', "intangible", ""), ('descend', "descend", ""), ('keep', "keep", ""), ('level', "level", ""), ('None', "None", "")), default='None')
    collide_flag_3 = EnumProperty(items=(('event', "event", ""), ('intangible', "intangible", ""), ('descend', "descend", ""), ('keep', "keep", ""), ('level', "level", ""), ('None', "None", "")), default='None')
    collide_flag_4 = EnumProperty(items=(('event', "event", ""), ('intangible', "intangible", ""), ('descend', "descend", ""), ('keep', "keep", ""), ('level', "level", ""), ('None', "None", "")), default='None')
    collide_flag_5 = EnumProperty(items=(('event', "event", ""), ('intangible', "intangible", ""), ('descend', "descend", ""), ('keep', "keep", ""), ('level', "level", ""), ('None', "None", "")), default='None')
    
    zones_index = IntProperty()
    
# Xранит пользовательские даные для сцены
class Hatcher_scene(PropertyGroup):
    # Переменная для хранения адреса установленный панды
    dir_Panda3D = StringProperty(subtype='DIR_PATH')
    
    
class Hatcher_list_egg_add(PropertyGroup):

    path_egg = StringProperty(subtype='FILE_PATH')
