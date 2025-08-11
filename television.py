

class Television:
    """A simple television remote emulator that has power, volume, and mute"""

    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL:int  = 3

    def __init__(self):
        """used to initialize the different tv settings"""
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """allows for on and off of the TV"""
        self.__status = not self.__status


    def mute(self):
        """allows for the ability to mute the TV"""
        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self):
        """allows to change the channel up by one"""
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """allows to change the channel down by one"""
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """allows to change the volume up by one"""
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """allows to change the volume down by one"""
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Returns a string that displays the TV Status"""
        if self.__muted:
            self.__muted = 0
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__muted}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
