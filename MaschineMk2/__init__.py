# Source Generated with Decompyle++
# File: __init__.pyc (Python 2.5)

from MaschineMk2 import MaschineMk2

def create_instance(c_instance):
    return MaschineMk2(c_instance)

from _Framework.Capabilities import *

def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(vendor_id = 9000, product_ids = [
            2], model_name = 'Maschine Mk2'),
        PORTS_KEY: [
            inport(props = [
                HIDDEN,
                NOTES_CC,
                SCRIPT]),
            inport(props = []),
            outport(props = [
                HIDDEN,
                NOTES_CC,
                SYNC,
                SCRIPT]),
            outport(props = [])] }

