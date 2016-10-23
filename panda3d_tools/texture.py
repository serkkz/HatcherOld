# -*- coding: utf-8 -*-
import bpy
from bpy.props import *
from bpy.types import (PropertyGroup)
import os
import imghdr

class Textures(bpy.types.Panel):
    bl_label = "Texture"  # Имя панели
    bl_space_type = 'VIEW_3D'  # В каком окне
    bl_region_type = 'TOOLS'  # Место распаложения
    bl_category = 'Hatcher version 0.3'  # Название вкладки
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout 
         
        # Проверка есть ли активный материал
        if hasattr(bpy.context.active_object, 'active_material'):
            
            # Проверка есть ли активная текстура у материала
            if hasattr(bpy.context.active_object.active_material, 'active_texture'):
        
                # Активный слот текстуры
                if bpy.context.active_object.active_material.active_texture:
                
                    # Проверка типа текстуры
                    if hasattr(bpy.context.active_object.active_material.active_texture, 'image'):
                    
                        # Проверка есть ли у текстуры атрибут путь файла изображения
                        if hasattr(bpy.context.active_object.active_material.active_texture.image, 'filepath'):
                        
                            frametex = layout.box()

                            if bpy.context.active_object.active_material.active_texture.hatcher.chexbox_tex_wr:
                                frametex.active = True
                            else:
                                frametex.active = False

                            fram_name = frametex.row()
                        
                            fram_name.prop(bpy.context.active_object.active_material.active_texture, "name", text='Slot name')
                            
                            fram_name.prop(bpy.context.active_object.active_material.active_texture.hatcher, "chexbox_tex_wr")
                        
                            fram_path = frametex.row()
                        
                            if bpy.context.active_object.active_material.active_texture.hatcher.tex_dir_type == 'Absolute':
                                fram_path.label(text="Filename:    %s" % bpy.context.active_object.active_material.active_texture.image.filepath)
                            else:
                                fram_path.prop(bpy.context.active_object.active_material.active_texture.hatcher, "set_dir_rel", text="")
                         
                            fram_path.prop(bpy.context.active_object.active_material.active_texture.hatcher, "tex_dir_type", text="")
                        
                        
                            frame_alpha = frametex.box()

                            frame_alpha.prop(bpy.context.active_object.active_material.active_texture.hatcher, "alfa_file", text="alpha-file")
                            

                            if bpy.context.active_object.active_material.active_texture.hatcher.alfa_file != '':

                                if os.path.isfile(bpy.context.active_object.active_material.active_texture.hatcher.alfa_file):
                                
                                    frame_alpha_file = frame_alpha.row()
                                    
                                    if bpy.context.active_object.active_material.active_texture.hatcher.tex_dir_alpha_type == 'Absolute':
                                    
                                        frame_alpha_file.label(text="File: " + bpy.context.active_object.active_material.active_texture.hatcher.alfa_file)                                    
                                        frame_alpha_file.prop(bpy.context.active_object.active_material.active_texture.hatcher, "tex_dir_alpha_type", text="")
  
                                    else:
   
                                        frame_alpha_file.prop(bpy.context.active_object.active_material.active_texture.hatcher, "alfa_file_save", text="Alpha file save")
                                        frame_alpha_file.prop(bpy.context.active_object.active_material.active_texture.hatcher, "tex_dir_alpha_type", text="")

                                    frame_alpha.prop(bpy.context.active_object.active_material.active_texture.hatcher, "alpha_file_channel", text="alpha-file-channel")
                                
                                else:
                                
                                    frame_alpha.label(text="File not found")

                            else:
                                frame_alpha.label(text="Select file")
                                
                            
                            frame_format = frametex.box()
                            frame_format.prop(bpy.context.active_object.active_material.active_texture.hatcher, "format_tex", text="format")
                        
                            frame_alpha_stat = frametex.box()
                            frame_alpha_stat.prop(bpy.context.active_object.active_material.active_texture.hatcher, "alpha_stat", text="alpha")
                        
                            frame_value_compr = frametex.box()
                            frame_value_compr.prop(bpy.context.active_object.active_material.active_texture.hatcher, "value_compr", text="compression")
                        
                            frame_value_envtype = frametex.box()
                            frame_value_envtype.prop(bpy.context.active_object.active_material.active_texture.hatcher, "value_envtype", text="envtype")
                        
                            frame_anisotropic = frametex.box()
                            frame_anisotropic.prop(bpy.context.active_object.active_material.active_texture.hatcher, "value_anisotropic", text="anisotropic filtering")

                            frame_value_wrapuv = frametex.box()
                            frame_value_wrapuv.prop(bpy.context.active_object.active_material.active_texture.hatcher, "value_wrapu", text="wrapu")
                            frame_value_wrapuv.prop(bpy.context.active_object.active_material.active_texture.hatcher, "value_wrapv", text="wrapv")

                            frame_value_minfilter_magfilter = frametex.box()
                            frame_value_minfilter_magfilter.prop(bpy.context.active_object.active_material.active_texture.hatcher, "value_minfilter", text="minfilter")
                            frame_value_minfilter_magfilter.prop(bpy.context.active_object.active_material.active_texture.hatcher, "value_magfilter", text="magfilter")                      

                        else:
                            layout.label(text="Texture no file map")
                    
                    else:
                        layout.label(text="Texture no type image")

                else:
                    layout.label(text="Empty slot texture")
            
            else:
                layout.label(text="No material")
            
        else:
            layout.label(text="No material")
