"""
Singleton Pattern
Easy
Implement the Singleton design pattern.

The Singleton is a creational design pattern which ensures that at most one instance of a class may exist.

Singleton getInstance() will return the singleton instance.
String getValue() will return the value of the singleton.
void setValue(String value) will update the value of the singleton.
You can assume the singleton will only be used in a single-threaded environment.
"""

class Singleton:
    _instance = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.value = None
            
        return cls._instance

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value


s = Singleton()
print(s.getValue()) # None

s.setValue("value")
print(s.getValue()) # Value

s2 = Singleton()
print(s2.getValue()) # Value