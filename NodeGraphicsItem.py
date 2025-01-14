from PyQt5.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsView, QMainWindow, QVBoxLayout, QWidget, QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush

class NodeGraphicsItem(QGraphicsItem):
    def __init__(self, node_type):
        super().__init__()
        self.node_type = node_type
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.inputs = []
        self.outputs = []
        self.input_ports = []
        self.output_ports = []
        self.setAcceptHoverEvents(True)
        self.apply_theme()

    def apply_theme(self):
        """Apply the current theme to the node."""
        self.set_light_theme()

    def set_light_theme(self):
        """Set the light theme for the node."""
        self.brush = QBrush(Qt.lightGray)
        self.pen = QPen(Qt.black)

    def boundingRect(self):
        """Return the bounding rectangle for the node item."""
        return QRectF(0, 0, 120, 60)

    def paint(self, painter, option, widget=None):
        """Paint the node rectangle and display its type, inputs, and outputs."""
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawRect(self.boundingRect())

        # Display node type at the center
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.node_type)

        # Display inputs and outputs
        if self.inputs:
            painter.drawText(5, 15, f"Input: {', '.join(map(str, self.inputs))}")
        if self.outputs:
            painter.drawText(5, 45, f"Output: {', '.join(map(str, self.outputs))}")

    def add_input_port(self):
        """Add an input port."""
        port = NodePort(self, "input")
        self.input_ports.append(port)
        return port

    def add_output_port(self):
        """Add an output port."""
        port = NodePort(self, "output")
        self.output_ports.append(port)
        return port

    def set_input(self, inputs):
        """Set input values for the node."""
        self.inputs = inputs
        self.evaluate()

    def evaluate(self):
        """Evaluate the logic of the node based on its inputs."""
        if self.node_type == "AND Gate":
            self.outputs = [int(all(self.inputs))]
        elif self.node_type == "OR Gate":
            self.outputs = [int(any(self.inputs))]
        else:
            self.outputs = self.inputs  # Default: pass inputs as outputs
        self.update()


class NodePort(QGraphicsItem):
    def __init__(self, parent_node, port_type):
        super().__init__(parent_node)
        self.port_type = port_type
        self.connected_ports = []

    def boundingRect(self):
        """Return the bounding rectangle for the port."""
        return QRectF(-5, -5, 10, 10)

    def paint(self, painter, option, widget=None):
        """Paint the port."""
        painter.setBrush(QBrush(Qt.green if self.port_type == "input" else Qt.blue))
        painter.drawEllipse(self.boundingRect())


class NodeEditor(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.nodes = []

    def add_node(self, node_type):
        """Add a new node to the scene."""
        node_item = NodeGraphicsItem(node_type)
        self.addItem(node_item)
        self.nodes.append(node_item)

        # Add ports to the node
        node_item.add_input_port()
        node_item.add_output_port()
        return node_item

    def set_node_input(self, node_item):
        """Open a dialog to set input for a node."""
        dialog = InputDialog()
        if dialog.exec_():
            input_value = dialog.get_value()
            # Parse input (assume comma-separated values)
            inputs = list(map(int, input_value.split(",")))
            node_item.set_input(inputs)


class InputDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Set Node Input")
        self.setFixedSize(300, 150)
        layout = QVBoxLayout(self)

        # Instruction label
        self.label = QLabel("Enter input values (comma-separated):")
        layout.addWidget(self.label)

        # Input field
        self.input_field = QLineEdit(self)
        layout.addWidget(self.input_field)

        # Buttons
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.accept)
        layout.addWidget(self.ok_button)

    def get_value(self):
        """Get the input value from the dialog."""
        return self.input_field.text()


if __name__ == "__main__":
    app = QApplication([])

    # Set up main window
    window = QMainWindow()
    main_widget = QWidget()
    layout = QVBoxLayout(main_widget)

    # Create a NodeEditor and add it to a QGraphicsView
    node_editor = NodeEditor()
    view = QGraphicsView(node_editor)
    layout.addWidget(view)

    main_widget.setLayout(layout)
    window.setCentralWidget(main_widget)
    window.setWindowTitle("Node Graphics Item with Input")
    window.resize(800, 600)
    window.show()

    # Add example nodes
    and_gate = node_editor.add_node("AND Gate")
    or_gate = node_editor.add_node("OR Gate")

    # Set input for a node
    node_editor.set_node_input(and_gate)

    app.exec_()