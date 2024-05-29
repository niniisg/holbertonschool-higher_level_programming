#!/usr/bin/python3

import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is student:", self.is_student)

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Error occured while serializing:", {e})
        return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "rb")as f:
                return pickle.load(f)
        except Exception as e:
            print(f"error occured during deserializing:", {e})
        return None
