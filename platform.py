'''
   Copyright 2023 (c) WizIO ( Georgi Angelov )
'''

from platformio.public import PlatformBase

class WizioarmPlatform(PlatformBase):
    def is_embedded(self):
        return True

