# Source Generated with Decompyle++
# File: MaschineMode.pyc (Python 2.5)

import Live
from _Framework.SubjectSlot import subject_slot
from _Framework.CompoundComponent import CompoundComponent
from _Framework.ControlSurfaceComponent import ControlSurfaceComponent
from _Framework.ControlSurface import ControlSurface, _scheduled_method
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement
from MIDI_Map import *
from PadScale import *
from MaschineSessionComponent import MaschineSessionComponent

def find_drum_device(track):
    devices = track.devices
    for device in devices:
        if device.can_have_drum_pads:
            return device
            continue
    


class MaschineMode(CompoundComponent):
    __module__ = __name__
    
    def __init__(self, button_index = None, *a, **k):
        super(MaschineMode, self).__init__(*a, **a)
        self._active = False
        self._alternate_mode = None
        self.button_index = button_index

    
    def get_color(self, value, column_index, row_index):
        pass

    
    def notify(self, blink_state):
        pass

    
    def notify_mono(self, blink_state):
        pass

    
    def navigate(self, dir, modifier, alt_modifier = False):
        pass

    
    def unbind(self):
        pass

    
    def is_lock_mode(self):
        return True

    
    def enter(self):
        raise NotImplementedError, self.__class__

    
    def exit(self):
        raise NotImplementedError, self.__class__

    
    def enter_edit_mode(self, type):
        pass

    
    def exit_edit_mode(self, type):
        pass

    
    def get_mode_id(self):
        return OTHER_MODE

    
    def enter_clear_state(self):
        pass

    
    def exit_clear_state(self):
        pass

    
    def disconnect(self):
        super(MaschineMode, self).disconnect()

    
    def fitting_mode(self, track):
        return self

    
    def set_alternate_mode(self, mode):
        self._alternate_mode = mode

    
    def isShiftDown(self):
        return self.canonical_parent.isShiftDown()

    
    def handle_push(self, value):
        pass

    
    def refresh(self):
        pass

    
    def _device_changed(self):
        pass

    
    def update(self):
        pass



class StudioClipMode(MaschineMode):
    __module__ = __name__
    
    def __init__(self, button_index, *a, **k):
        super(StudioClipMode, self).__init__(button_index, *a, **a)

    
    def get_color(self, value, column_index, row_index):
        session = self.canonical_parent._session
        scene = session.scene(row_index)
        clip_slot = scene.clip_slot(column_index)._clip_slot
        color = session.get_color(clip_slot)
        if not value == 0 or 1:
            pass
        cindex = 0
        return color[cindex]

    
    def notify(self, blink_state):
        self.canonical_parent._session.notify(blink_state)

    
    def notify_mono(self, blink_state):
        self.canonical_parent._session.notify_mono(blink_state)

    
    def enter_edit_mode(self, type):
        self.canonical_parent._session.set_enabled(False)

    
    def exit_edit_mode(self, type):
        self.canonical_parent._session.set_enabled(True)

    
    def get_mode_id(self):
        return CLIP_MODE

    
    def navigate(self, dir, modifier, alt_modifier = False):
        if modifier:
            if dir == 1:
                self.canonical_parent._session.bank_up()
            else:
                self.canonical_parent._session.bank_down()
        elif dir == 1:
            self.canonical_parent._session.bank_right()
        else:
            self.canonical_parent._session.bank_left()

    
    def enter(self):
        self._active = True
        for (column, row) in self.canonical_parent._bmatrix.iterbuttons():
            if button:
                button.set_to_notemode(False)
                scene = self.canonical_parent._session.scene(row)
                clip_slot = scene.clip_slot(column)
                clip_slot.set_launch_button(button)
                continue
        

    
    def refresh(self):
        if self._active:
            for (column, row) in self.canonical_parent._bmatrix.iterbuttons():
                if button:
                    button.reset()
                    button.refresh()
                    continue
            
        

    
    def exit(self):
        self._active = False
        self.canonical_parent._deassign_matrix()
        self.canonical_parent._session.set_clip_launch_buttons(None)


