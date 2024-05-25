#!/usr/bin/python3

class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, item):
        super().extend(item)
        leng = len(item)
        print(f"Extend the list with [{leng}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, index=None):

        if index is not None:
            erase = super().pop(index)
            print(f"Popped [{erase}] from the list.")
            return erase
        else:
            erase = super().pop()
            print(f"Popped [{erase}] from the list.")
            return erase
