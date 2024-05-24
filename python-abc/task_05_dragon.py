#!/usr/bin/python3

class SwimMixin:
    def swim(self):
        return("The creatures swims!")


class FlyMixin:
    def fly(self):
        return("The creatures flies!")


class Dragon(SwimMixin, FlyMixin):
    pass

    def roar(self):
        return("The dragon roars!")
