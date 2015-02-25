# Source Generated with Decompyle++
# File: MaschineMk2.pyc (Python 2.5)

from __future__ import with_statement
import Live
import time
from Maschine import Maschine
from MaschineMixerComponent import MaschineMixerComponent
from MIDI_Map import debug_out
from KnobSection import KnobSection
from PadColorButton import PadColorButton
from GatedColorButton import GatedColorButton
from _Framework.ControlSurface import ControlSurface, _scheduled_method
from _Framework.InputControlElement import *
from _Framework.SliderElement import SliderElement
from _Framework.ButtonElement import ButtonElement, ON_VALUE, OFF_VALUE
from _Framework.ButtonMatrixElement import ButtonMatrixElement

class MaschineMk2(Maschine):
    __module__ = __name__
    '''Control Script for Maschine Studio'''
    _gated_buttons = []
    
    def __init__(self, c_instance):
        super(MaschineMk2, self).__init__(c_instance)

    
    def create_pad_button(self, scene_index, track_index, color_source):
        return PadColorButton(True, 0, scene_index, track_index, color_source)

    
    def create_gated_button(self, identifier, hue):
        button = GatedColorButton(True, MIDI_CC_TYPE, identifier, hue)
        self._gated_buttons.append(button)
        return button

    
    def _init_maschine(self):
        self._jogwheel = KnobSection(self._modeselect, self._editsection)
        self._note_repeater.registerKnobHandler(self._jogwheel)
        self._mixer.set_touch_mode(2)
        self._device_component.set_touch_mode(2)

    
    def to_color_edit_mode(self, active):
        if self._editsection.is_color_edit() != active:
            if not active or 1:
                pass
            self._jogwheel.invoke_color_mode(0)
        

    
    def use_layered_buttons(self):
        return True

    
    def _final_init(self):
        debug_out('########## LIVE 9 MASCHINE Mk2 V 2.02 ############# ')

    
    def _click_measure(self):
        pass

    
    def apply_preferences(self):
        super(MaschineMk2, self).apply_preferences()
        pref_dict = self._pref_dict
        if 'color_mode' in pref_dict:
            value = pref_dict['color_mode']
            self._session.set_color_mode(value)
            if not value == True or 127:
                pass
            self._session._c_mode_button.send_value(0, True)
        else:
            self._session.set_color_mode(False)
            self._session._c_mode_button.send_value(0, True)

    
    def store_preferences(self):
        super(MaschineMk2, self).store_preferences()
        self._pref_dict['color_mode'] = self._session.is_color_mode()

    
    def preferences_name(self):
        return 'MaschineMk2'

    
    def cleanup(self):
        for button in self._gated_buttons:
            button.switch_off()
        


