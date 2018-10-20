# -*- coding: utf-8; -*-

# Copyright (C) 2015 - 2018 Lionel Ott
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import enum

import gremlin.error


class DeviceIdentifier:

    """Represents device identity.

    Transparently handles case with duplicate and non-duplicate devices, taking
    care of using the minimally required features to distinguish different
    devices.
    """

    # Storage for duplicate device state information
    _duplicate_device = {}

    # Value shift amount for hash computation
    ShiftHardwareId = 0
    ShiftWindowsId = 32

    def __init__(self, hardware_id, windows_id):
        """Creates a new instance.

        :param hardware_id hardware id of the device
        :param windows_id windows id of the device
        """
        self._hardware_id = hardware_id
        self._windows_id = windows_id

    def __eq__(self, other):
        """Returns whether this instance is identical to the other one.

        :return True if this and other are identical, False otherwise
        """
        return hash(self) == hash(other)

    def __hash__(self):
        """Returns the hash value of this instance.

        :return hash value of this instance
        """
        hash_val = 0
        hash_val += self._hardware_id << DeviceIdentifier.ShiftHardwareId
        windows_id = 0
        if DeviceIdentifier._duplicate_device.get(self._hardware_id, False):
            hash_val += self._windows_id
        hash_val += windows_id << DeviceIdentifier.ShiftWindowsId

        return hash_val

    @classmethod
    def reset(cls):
        """Resets the device identifier class storage."""
        DeviceIdentifier._duplicate_device = {}


class InputType(enum.Enum):

    """Enumeration of possible input types."""

    Keyboard = 1
    JoystickAxis = 2
    JoystickButton = 3
    JoystickHat = 4
    Mouse = 5
    VirtualButton = 6

    @staticmethod
    def to_string(value):
        try:
            return _InputType_to_string_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")

    @staticmethod
    def to_enum(value):
        try:
            return _InputType_to_enum_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")

_InputType_to_string_lookup = {
    InputType.JoystickAxis: "axis",
    InputType.JoystickButton: "button",
    InputType.JoystickHat: "hat",
    InputType.Keyboard: "key",
}

_InputType_to_enum_lookup = {
    "axis": InputType.JoystickAxis,
    "button": InputType.JoystickButton,
    "hat": InputType.JoystickHat,
    "key": InputType.Keyboard
}


# Mapping from InputType values to their textual representation
input_type_to_name = {
    InputType.Keyboard: "Keyboard",
    InputType.JoystickAxis: "Axis",
    InputType.JoystickButton: "Button",
    InputType.JoystickHat: "Hat"
}


class AxisButtonDirection(enum.Enum):

    """Possible activation directions for axis button instances."""

    Anywhere = 1
    Below = 2
    Above = 3

    @staticmethod
    def to_string(value):
        try:
            return _AxisButtonDirection_to_string_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")

    @staticmethod
    def to_enum(value):
        try:
            return _AxisButtonDirection_to_enum_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")


_AxisButtonDirection_to_string_lookup = {
    AxisButtonDirection.Anywhere: "anywhere",
    AxisButtonDirection.Above: "above",
    AxisButtonDirection.Below: "below"
}


_AxisButtonDirection_to_enum_lookup = {
    "anywhere": AxisButtonDirection.Anywhere,
    "above": AxisButtonDirection.Above,
    "below": AxisButtonDirection.Below
}


class MouseButton(enum.Enum):

    """Enumeration of all possible mouse buttons."""

    Left = 1
    Right = 2
    Middle = 3
    Forward = 4
    Back = 5
    WheelUp = 10
    WheelDown = 11

    @staticmethod
    def to_string(value):
        try:
            return _MouseButton_to_string_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")

    @staticmethod
    def to_enum(value):
        try:
            return _MouseButton_to_enum_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")


_MouseButton_to_string_lookup = {
    MouseButton.Left: "Left",
    MouseButton.Right: "Right",
    MouseButton.Middle: "Middle",
    MouseButton.Forward: "Forward",
    MouseButton.Back: "Back",
    MouseButton.WheelUp: "Wheel Up",
    MouseButton.WheelDown: "Wheel Down",
}


_MouseButton_to_enum_lookup = {
    "Left": MouseButton.Left,
    "Right": MouseButton.Right,
    "Middle": MouseButton.Middle,
    "Forward": MouseButton.Forward,
    "Back": MouseButton.Back,
    "Wheel Up": MouseButton.WheelUp,
    "Wheel Down": MouseButton.WheelDown,
}


class VariableType(enum.Enum):

    """Enumeration of all supported variable types."""

    Int = 1
    Float = 2
    String = 3
    Bool = 4
    PhysicalInput = 5
    VirtualInput = 6
    Mode = 7

    @staticmethod
    def to_string(value):
        try:
            return _VariableType_to_string_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")

    @staticmethod
    def to_enum(value):
        try:
            return _VariableType_to_enum_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")



_VariableType_to_string_lookup = {
    VariableType.Int: "Int",
    VariableType.Float: "Float",
    VariableType.String: "String",
    VariableType.Bool: "Bool",
    VariableType.PhysicalInput: "PhysicalInput",
    VariableType.VirtualInput: "VirtualInput",
    VariableType.Mode: "Mode"
}

_VariableType_to_enum_lookup = {
    "Int": VariableType.Int,
    "Float": VariableType.Float,
    "String": VariableType.String,
    "Bool": VariableType.Bool,
    "PhysicalInput": VariableType.PhysicalInput,
    "VirtualInput": VariableType.VirtualInput,
    "Mode": VariableType.Mode
}


def index_to_direction(direction):
    """Returns a direction index to a direction name.

    :param direction index of the direction to convert
    :return text representation of the direction index
    """
    lookup = {
        1: "Up",
        2: "Up & Right",
        3: "Right",
        4: "Down & Right",
        5: "Down",
        6: "Down & Left",
        7: "Left",
        8: "Up & Left"
    }
    return lookup[int(direction)]


# Mapping from hat direction tuples to their textual representation
direction_tuple_lookup = {
    (0, 0): "Center",
    (0, 1): "North",
    (1, 1): "North East",
    (1, 0): "East",
    (1, -1): "South East",
    (0, -1): "South",
    (-1, -1): "South West",
    (-1, 0): "West",
    (-1, 1): "North West",
    "Center": (0, 0),
    "North": (0, 1),
    "North East": (1, 1),
    "East": (1, 0),
    "South East": (1, -1),
    "South": (0, -1),
    "South West": (-1, -1),
    "West": (-1, 0),
    "North West": (-1, 1)
}


# Names of vJoy axis according to their index
vjoy_axis_names = [
    "X",
    "Y",
    "Z",
    "X Rotation",
    "Y Rotation",
    "Z Rotation",
    "Slider",
    "Dial"
]


class SingletonDecorator:

    """Decorator turning a class into a singleton."""

    def __init__(self, klass):
        self.klass = klass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance is None:
            self.instance = self.klass(*args, **kwargs)
        return self.instance


class DeviceType(enum.Enum):

    """Enumeration of the different possible input types."""

    Keyboard = 1
    Joystick = 2
    VJoy = 3

    @staticmethod
    def to_string(value):
        try:
            return _DeviceType_to_string_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")

    @staticmethod
    def to_enum(value):
        try:
            return _DeviceType_to_enum_lookup[value]
        except KeyError:
            raise gremlin.error.GremlinError("Invalid type in lookup")


_DeviceType_to_string_lookup = {
    DeviceType.Keyboard: "keyboard",
    DeviceType.Joystick: "joystick",
    DeviceType.VJoy: "vjoy"
}


_DeviceType_to_enum_lookup = {
    "keyboard": DeviceType.Keyboard,
    "joystick": DeviceType.Joystick,
    "vjoy": DeviceType.VJoy
}