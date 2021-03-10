class bodyParts:
    def _init_(self):
        self.hand = "hand"
        self.foot = "foot"

class creatures:
    def _init_(self, name):
        self.name = name

    class bodyPart(bodyParts):
        def display(self):
            return "hi"


print(creatures.bodyPart().ToString())