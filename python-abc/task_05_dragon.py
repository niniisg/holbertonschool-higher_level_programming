#!/usr/bin/python3

class SwimMixin:

    def swim(self):
        return("The creature swims!")


class FlyMixin:
    def fly(self):
        return("The creature flies!")


class Dragon(SwimMixin, FlyMixin):

    def roar(self):
        return("The dragon roars!")
