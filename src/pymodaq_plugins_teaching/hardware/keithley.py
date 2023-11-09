# -*- coding: utf-8 -*-
"""
Created the 08/11/2023

@author: Sebastien Weber
"""
import warnings

from pymodaq_plugins_teaching.hardware.serial_addresses import SerialAddresses, BaseEnum
import random
from pylablib.core.devio import SCPI, interface


class EnumParameterClass(interface.EnumParameterClass):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def names(self):
        list(self._get_alias_map().keys())


class ResourceManager:

    def __init__(self):
        pass

    def list_resources(self):
        """List all possible addresses"""
        return SerialAddresses.names()


class Keithley2110:
    """ Python Driver object to communicate with a 2100 Series Keithley Digital Multimeter

    This is simulating a fake instrument but follows the PyLabLib driver structure
    """

    _p_function = interface.EnumParameterClass("function",
                                               {"volt_dc": "VOLT:DC", "curr_dc": "CURR:DC",
                                                "freq_volt": "FREQ:VOLT", "none": "NONE"})



    def __init__(self, address: str = None):

        self._is_open = False
        if address is not None:
            self.open_communication(address)

    @property
    def is_open(self):
        return self._is_open

    def open_communication(self, address: str):
        if self.is_open:
            raise IOError('Device already connected')
        else:
            if address not in SerialAddresses.names():
                raise IOError('Invalid Address')
            else:
                self._is_open = True

    def close(self):
        if self._is_open:
            self._is_open = False

    def get_function(self):
        return self._measurement.name

    def set_function(self, function: str):
        if function not in self._measurements.names():
            warnings.warn(f'The requested measurement, {function} cannot be set')
        else:
            self._measurement = self._measurements[function]

    def get_range(self) -> float:
        return self._range.value

    def get_reading(self, channel='primary'):
        return self.get_range() * random.random()

    def get_range(self):
        pass


if __name__ == '__main__':

    meter = Keithley2110(SerialAddresses.names()[0])

    meter.get_function()
    pass