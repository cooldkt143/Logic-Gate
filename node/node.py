from PyQt5.QtWidgets import QGraphicsItem, QGraphicsTextItem
from PyQt5.QtCore import Qt, QRectF

class Node(QGraphicsItem):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.text = QGraphicsTextItem(name, self)
        self.text.setPos(10, 10)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

    def boundingRect(self):
        return QRectF(0, 0, 100, 50)

    def paint(self, painter, option, widget):
        painter.setBrush(Qt.lightGray)
        painter.drawRect(self.boundingRect())

class AndNode(Node):
    def __init__(self):
        super().__init__("And")
        # Additional initialization for the AND gate

    def evaluate(self):
        # Implement the logic for AND gate: return 1 if both inputs are 1
        pass 

class OrNode(Node):
    def __init__(self):
        super().__init__("Or")
        self.inputs = [0, 0]  # Two inputs for the OR gate (default to 0)
        self.output = 0       # Output of the OR gate (default to 0)

    def set_inputs(self, input1, input2):
        """Set the values for the inputs of the OR gate."""
        self.inputs[0] = input1
        self.inputs[1] = input2

    def evaluate(self):
        """
        Perform the OR operation on the inputs.
        Returns the output of the OR gate.
        """
        self.output = self.inputs[0] or self.inputs[1]
        return self.output


class NotNode(Node):
    def __init__(self):
        super().__init__("Not")
        # Additional initialization for the NOT gate

    def evaluate(self):
        # Implement the logic for NOT gate: return 1 if inputs is 0
        pass

class NandNode(Node):
    def __init__(self):
        super().__init__("Nand")
        # Additional initialization for the NAND gate

    def evaluate(self):
        # Implement the logic for NAND gate: return 0 if both inputs are 1
        pass

class NorNode(Node):
    def __init__(self):
        super().__init__("Nor")
        # Additional initialization for the NOR gate

    def evaluate(self):
        # Implement the logic for NOR gate: return 1 if both inputs are 0
        pass

class XorNode(Node):
    def __init__(self):
        super().__init__("Xor")
        # Additional initialization for the XOR gate

    def evaluate(self):
        # Implement the logic for XOR gate: return 1 if both inputs are same
        pass

