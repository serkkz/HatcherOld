import bpy
from bpy.props import IntProperty, CollectionProperty
from bpy.types import Panel, UIList

class List_EGG_File(bpy.types.UIList):

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):

        layout.prop(item, "path_egg", text="File path egg")


