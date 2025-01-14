from PyQt5.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsView, QMainWindow, QVBoxLayout, QWidget, QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush
from PyQt5.QtGui import QTransform

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
        """Evaluate the logic of the node based on its connected inputs."""
        # Gather inputs from connected edges
        self.inputs = [edge.start_port.parentItem().outputs[0] for edge in self.input_ports[0].connected_edges]
        
        # Perform logic based on the node type
        if self.node_type == "AND Gate":
            self.outputs = [int(all(self.inputs))]
        elif self.node_type == "OR Gate":
            self.outputs = [int(any(self.inputs))]
        elif self.node_type == "NOT Gate":
            # NOT Gate assumes a single input
            self.outputs = [int(not self.inputs[0])] if len(self.inputs) == 1 else []
        elif self.node_type == "NAND Gate":
            self.outputs = [int(not all(self.inputs))]
        elif self.node_type == "NOR Gate":
            self.outputs = [int(not any(self.inputs))]
        elif self.node_type == "XOR Gate":
            # XOR: True if an odd number of inputs are True
            self.outputs = [int(sum(self.inputs) % 2 == 1)]
        elif self.node_type == "XNOR Gate":
            # XNOR: True if an even number of inputs are True
            self.outputs = [int(sum(self.inputs) % 2 == 0)]
        else:
            # Default behavior: pass inputs to outputs
            self.outputs = self.inputs

        # Update node visuals
        self.update()

class NodePort(QGraphicsItem):
    def __init__(self, parent_node, port_type):
        super().__init__(parent_node)
        self.port_type = port_type
        self.connected_ports = []
        self.connected_edges = []  # Initialize connected_edges

    def add_edge(self, edge):
        """Add an edge connected to this port."""
        self.connected_edges.append(edge)

    def remove_edge(self, edge):
        """Remove an edge connected to this port."""
        if edge in self.connected_edges:
            self.connected_edges.remove(edge)

    def notify_edges(self):
        """Notify all edges connected to this port to update their positions."""
        for edge in self.connected_edges:
            edge.update_positions()

    def boundingRect(self):
        """Return the bounding rectangle for the port."""
        return QRectF(-5, -5, 10, 10)

    def paint(self, painter, option, widget=None):
        """Paint the port."""
        painter.setBrush(QBrush(Qt.green if self.port_type == "input" else Qt.blue))
        painter.drawEllipse(self.boundingRect())

class Edge(QGraphicsItem):
    def __init__(self, start_port, end_port=None):
        super().__init__()
        self.start_port = start_port
        self.end_port = end_port
        self.setZValue(-1)  # Ensure edges are below nodes
        self.temp_end_pos = None  # Temporary position during drag

    def boundingRect(self):
        """Return the bounding rectangle for the edge."""
        if not self.end_port:
            return QRectF(self.start_port.scenePos(), self.temp_end_pos or self.start_port.scenePos()).normalized()
        return QRectF(self.start_port.scenePos(), self.end_port.scenePos()).normalized()

    def paint(self, painter, option, widget=None):
        """Paint the edge."""
        start_pos = self.start_port.scenePos()
        end_pos = self.end_port.scenePos() if self.end_port else self.temp_end_pos
        if end_pos:
            painter.setPen(QPen(Qt.black, 2))
            painter.drawLine(start_pos, end_pos)

    def update_positions(self):
        """Update the edge's position."""
        self.prepareGeometryChange()
        self.update()

    def set_temp_end_pos(self, pos):
        """Set the temporary end position for the edge during drag."""
        self.temp_end_pos = pos
        self.update()



class NodeEditor(QGraphicsScene):
    def __init__(self):
        super().__init__()
        self.nodes = []
        self.temp_edge = None  # Temporary edge for connections

    def __init__(self):
        super().__init__()
        self.nodes = []
        self.temp_edge = None

    def mousePressEvent(self, event):
        """Handle mouse press for edge creation."""
        item = self.itemAt(event.scenePos(), QTransform())
        if isinstance(item, NodePort):
            self.temp_edge = Edge(item)
            self.addItem(self.temp_edge)
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        """Update the temporary edge during mouse drag."""
        if self.temp_edge:
            self.temp_edge.set_temp_end_pos(event.scenePos())
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        """Finalize edge creation."""
        if self.temp_edge:
            end_item = self.itemAt(event.scenePos(), QTransform())
            if isinstance(end_item, NodePort) and end_item != self.temp_edge.start_port:
                # Connect the edge to the end port
                self.temp_edge.end_port = end_item
                self.temp_edge.update_positions()
                self.temp_edge.start_port.connected_ports.append(self.temp_edge)
                end_item.connected_ports.append(self.temp_edge)
            else:
                # Remove invalid edge
                self.removeItem(self.temp_edge)
            self.temp_edge = None
        super().mouseReleaseEvent(event)

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