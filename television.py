class Television:
    '''
    A class representing controls for a TV and setting constants
    '''
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        '''
        Method to set default values of a TV
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        '''
        Method to turn on TV
        :return: power status of TV
        '''
        self.__status = not self.__status

    def mute(self):
        '''
        Method to mute TV
        :return: mute status of TV
        '''
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        '''
        Method to turn up the channel number
        :return: new channel number
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        '''
        Method to turn down the channel
        :return: new channel number
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        '''
        Method to turn up the volume
        :return: new volume number
        '''
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        '''
        Method to turn down the volume
        :return: new volume level
        '''
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        '''
        Method to print status of power, channel, and volume status
        :return: Power, Channel, Volume
        '''
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'

