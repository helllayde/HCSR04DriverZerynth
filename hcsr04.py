# Copyright (c) 2020 helllayde
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

class hcsr04:
    """
        Class representing a HCSR04 device.
        If correctly initialized and plugged, the device is able to estimate the distance
        between its position and the first occluder object using a supersonic burst

        Attributes
        ----------
        trigger : int
            Tringger Pin number
        echo : int
            Echo pin number 
        
    """

    @c_native("HCSR04_readDistanceRaw", ["csrc/hcsr04.c"], [])
    def _getDistanceRaw(trig, echo):
        """
            (static wrapper function, should not be used. Use hcsr04.getDistanceRaw() instead)
            Get the distance as length in microseconds of the ICU pulse.
            This function is a wrapper from the C souce

            Parameters
            ----------
            trig : int
                Trigger Pin number
            echo : int
                Echo pin number 
        """
        pass
    
    def getDistanceRaw(self):
        """
            Get the distance from the device as length in microseconds of the ICU pulse
        """
        return hcsr04._getDistanceRaw(self.trigger, self.echo)
    
    def getDistanceCM(self):
        """
            Get the distance normalized in centimeters from the device
        """
        return self.getDistanceRaw() / 58
    
    def getDistanceINCH(self):
        """
            Get the distance normalized in inches from the device
        """
        return self.getDistanceRaw() / 148
    
    def __init__(self, trigger, echo):
        """
            Initialize a new HCSR04 device using the given pin numbers.
            When interrogated, the device will be triggered with a 10 microsecond-length
            pulse on the trigger pin and the device will respond with a pulse on the
            echo pin representing the length of the distance between the device and the
            first occluder

            Parameters
            ----------
            trigger : int
                Trigger Pin number
            echo : int
                Echo Pin number
        """
        self.trigger = trigger
        self.echo = echo
        
        pinMode(self.trigger, OUTPUT)
        pinMode(self.echo, INPUT)