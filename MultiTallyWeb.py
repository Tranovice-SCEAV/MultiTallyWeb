
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App
import PyATEMMax
import time

switcher = PyATEMMax.ATEMMax()

switcher.connect('192.168.1.200')
switcher.waitForConnection()


class TallyWeb(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(TallyWeb, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
    #Update detection
        tally_1 = str(switcher.tally.bySource.flags[1])

        if tally_1 == "[PGM]":
            self.src1.css_background_color = "rgb(245,0,0)"
        elif tally_1 == "[PVW]":
            self.src1.css_background_color = "rgb(80,164,0)"
        elif tally_1 == "[]":
            self.src1.css_background_color = "rgb(170,170,170)"
        elif tally_1 == "[PGM][PVW]":
            self.src1.css_background_color = "rgb(245,0,0)"
        
        tally_2 = str(switcher.tally.bySource.flags[2])

        if tally_2 == "[PGM]":
            self.src2.css_background_color = "rgb(245,0,0)"
        elif tally_2 == "[PVW]":
            self.src2.css_background_color = "rgb(80,164,0)"
        elif tally_2 == "[]":
            self.src2.css_background_color = "rgb(170,170,170)"
        elif tally_2 == "[PGM][PVW]":
            self.src2.css_background_color = "rgb(245,0,0)"
        
        tally_3 = str(switcher.tally.bySource.flags[3])

        if tally_3 == "[PGM]":
            self.src3.css_background_color = "rgb(245,0,0)"
        elif tally_3 == "[PVW]":
            self.src3.css_background_color = "rgb(80,164,0)"
        elif tally_3 == "[]":
            self.src3.css_background_color = "rgb(170,170,170)"
        elif tally_3 == "[PGM][PVW]":
            self.src3.css_background_color = "rgb(245,0,0)"

        tally_4 = str(switcher.tally.bySource.flags[4])

        if tally_4 == "[PGM]":
            self.src4.css_background_color = "rgb(245,0,0)"
        elif tally_4 == "[PVW]":
            self.src4.css_background_color = "rgb(80,164,0)"
        elif tally_4 == "[]":
            self.src4.css_background_color = "rgb(170,170,170)"
        elif tally_4 == "[PGM][PVW]":
            self.src4.css_background_color = "rgb(245,0,0)"
        pass
    
    
    def main(self):
        return TallyWeb.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        self.container0 = Container()
        self.container0.attr_class = "Container"
        self.container0.attr_editor_newclass = False
        self.container0.css_background_color = "rgb(254,79,73)"
        self.container0.css_height = "330.0px"
        self.container0.css_left = "30.0px"
        self.container0.css_position = "absolute"
        self.container0.css_top = "30.0px"
        self.container0.css_width = "780.0px"
        self.container0.variable_name = "container0"
        self.src1 = Button()
        self.src1.attr_class = "Button"
        self.src1.attr_editor_newclass = False
        self.src1.css_font_size = "70px"
        self.src1.css_height = "125px"
        self.src1.css_left = "60.0px"
        self.src1.css_position = "absolute"
        self.src1.css_top = "15.0px"
        self.src1.css_width = "255px"
        self.src1.text = "1"
        self.src1.variable_name = "src1"
        self.container0.append(self.src1,'src1')
        self.src3 = Button()
        self.src3.attr_class = "Button"
        self.src3.attr_editor_newclass = False
        self.src3.css_font_size = "70px"
        self.src3.css_height = "125px"
        self.src3.css_left = "60.0px"
        self.src3.css_position = "absolute"
        self.src3.css_top = "180.0px"
        self.src3.css_width = "255.0px"
        self.src3.text = "3"
        self.src3.variable_name = "src3"
        self.container0.append(self.src3,'src3')
        self.src2 = Button()
        self.src2.attr_class = "Button"
        self.src2.attr_editor_newclass = False
        self.src2.css_font_size = "70px"
        self.src2.css_height = "125px"
        self.src2.css_left = "465.0px"
        self.src2.css_position = "absolute"
        self.src2.css_top = "15.0px"
        self.src2.css_width = "255px"
        self.src2.text = "2"
        self.src2.variable_name = "src2"
        self.container0.append(self.src2,'src2')
        self.src4 = Button()
        self.src4.attr_class = "Button"
        self.src4.attr_editor_newclass = False
        self.src4.css_font_size = "70px"
        self.src4.css_height = "125px"
        self.src4.css_left = "465.0px"
        self.src4.css_position = "absolute"
        self.src4.css_top = "180.0px"
        self.src4.css_width = "255px"
        self.src4.text = "4"
        self.src4.variable_name = "src4"
        self.container0.append(self.src4,'src4')
        

        self.container0 = self.container0
        return self.container0
    


#Configuration
start(TallyWeb, address='0.0.0.0', port=8081, multiple_instance=True, enable_file_cache=True, update_interval=0.08, start_browser=True)