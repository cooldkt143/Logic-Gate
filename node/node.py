class Node:
    """Base class for all nodes."""
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def evaluate(self):
        """Evaluates the node's logic."""
        raise NotImplementedError("This method must be implemented in subclasses.")


class InputNode(Node):
    """Node representing an input value."""
    def __init__(self, value=0):
        super().__init__("Input")
        self.value = value

    def evaluate(self):
        """Returns the value of the input."""
        return self.value


class OutputNode(Node):
    """Node representing the output of a logic operation."""
    def __init__(self):
        super().__init__("Output")

    def evaluate(self, input_value):
        """Passes through the input value as the output."""
        return input_value


class AndNode(Node):
    """Node representing the AND logic gate."""
    def __init__(self):
        super().__init__("And")

    def evaluate(self, input1, input2):
        """Returns True if both inputs are True."""
        return bool(input1 and input2)


class OrNode(Node):
    """Node representing the OR logic gate."""
    def __init__(self):
        super().__init__("Or")

    def evaluate(self, input1, input2):
        """Returns True if at least one input is True."""
        return bool(input1 or input2)


class NotNode(Node):
    """Node representing the NOT logic gate."""
    def __init__(self):
        super().__init__("Not")

    def evaluate(self, input1):
        """Returns the negation of the input."""
        return not bool(input1)


class NandNode(Node):
    """Node representing the NAND logic gate."""
    def __init__(self):
        super().__init__("Nand")

    def evaluate(self, input1, input2):
        """Returns True if at least one input is False."""
        return not (input1 and input2)


class NorNode(Node):
    """Node representing the NOR logic gate."""
    def __init__(self):
        super().__init__("Nor")

    def evaluate(self, input1, input2):
        """Returns True if both inputs are False."""
        return not (input1 or input2)


class XorNode(Node):
    """Node representing the XOR logic gate."""
    def __init__(self):
        super().__init__("Xor")

    def evaluate(self, input1, input2):
        """Returns True if exactly one input is True."""
        return bool(input1) ^ bool(input2)


class XnorNode(Node):
    """Node representing the XNOR logic gate."""
    def __init__(self):
        super().__init__("Xnor")

    def evaluate(self, input1, input2):
        """Returns True if both inputs are the same."""
        return not (bool(input1) ^ bool(input2))


# Example usage:
if __name__ == "__main__":
    # Input nodes
    input1 = InputNode(value=1)
    input2 = InputNode(value=0)

    # Logic gates
    and_gate = AndNode()
    or_gate = OrNode()
    not_gate = NotNode()
    nand_gate = NandNode()
    nor_gate = NorNode()
    xor_gate = XorNode()
    xnor_gate = XnorNode()

    # Test each gate
    print("AND:", and_gate.evaluate(input1.evaluate(), input2.evaluate()))  # Output: 0
    print("OR:", or_gate.evaluate(input1.evaluate(), input2.evaluate()))   # Output: 1
    print("NOT:", not_gate.evaluate(input1.evaluate()))                    # Output: 0
    print("NAND:", nand_gate.evaluate(input1.evaluate(), input2.evaluate()))  # Output: 1
    print("NOR:", nor_gate.evaluate(input1.evaluate(), input2.evaluate()))   # Output: 0
    print("XOR:", xor_gate.evaluate(input1.evaluate(), input2.evaluate()))   # Output: 1
    print("XNOR:", xnor_gate.evaluate(input1.evaluate(), input2.evaluate())) # Output: 0

    # Output node
    output = OutputNode()
    print("Output:", output.evaluate(xor_gate.evaluate(input1.evaluate(), input2.evaluate())))  # Output: 1
