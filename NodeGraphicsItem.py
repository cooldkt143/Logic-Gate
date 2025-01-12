from PyQt5.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtGui import QPen, QBrush, QColor

class NodeGraphicsItem(QGraphicsItem):
    def __init__(self, node_type):
        super().__init__()
        self.node_type = node_type
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.inputs = []
        self.outputs = []
        self.input_ports = []  # Holds input ports for connections
        self.output_ports = []  # Holds output ports for connections
        self.setAcceptHoverEvents(True)  # Allow interaction when hovering over nodes
        self.apply_theme()

    def apply_theme(self):
        """Apply the current theme to the node."""
        # Hardcoded to 'light' theme for testing; replace with dynamic theme logic
        self.set_light_theme()

    def set_dark_theme(self):
        """Set the dark theme for the node."""
        self.setBrush(QBrush(Qt.darkGray))
        self.setPen(QPen(Qt.white))

    def set_light_theme(self):
        """Set the light theme for the node."""
        self.setBrush(QBrush(Qt.lightGray))
        self.setPen(QPen(Qt.black))

    def boundingRect(self):
        """Return the bounding rectangle for the node item."""
        return QRectF(0, 0, 100, 50)

    def paint(self, painter, option, widget=None):
        """Paint the node (draw the rectangle and text) and its ports."""
        painter.setPen(self.pen())
        painter.setBrush(self.brush())
        painter.drawRect(self.boundingRect())  # Draw the node rectangle
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.node_type)  # Draw the node type

        # Draw input ports (left side)
        for i, port in enumerate(self.input_ports):
            port.setPos(0, i * 20)
            port.paint(painter, option, widget)

        # Draw output ports (right side)
        for i, port in enumerate(self.output_ports):
            port.setPos(100, i * 20)
            port.paint(painter, option, widget)

    def add_input_port(self):
        """Add an input port to the node."""
        port = NodePort(self, "input")
        self.input_ports.append(port)
        return port

    def add_output_port(self):
        """Add an output port to the node."""
        port = NodePort(self, "output")
        self.output_ports.append(port)
        return port

    def mousePressEvent(self, event):
        """Handle mouse press events for selecting the node."""
        super().mousePressEvent(event)
        if event.button() == Qt.LeftButton:
            self.setSelected(True)

    def mouseReleaseEvent(self, event):
        """Handle mouse release events."""
        super().mouseReleaseEvent(event)
        self.update_connections()

    def update_connections(self):
        """Update the connections when the node is moved or modified."""
        for port in self.input_ports:
            port.update_position()
        for port in self.output_ports:
            port.update_position()


class NodePort(QGraphicsItem):
    def __init__(self, parent_node, port_type):
        super().__init__(parent_node)
        self.port_type = port_type  # "input" or "output"
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        self.connected_ports = []  # Keep track of connected ports

    def boundingRect(self):
        """Return the bounding rectangle for the port."""
        return QRectF(0, 0, 10, 10)

    def paint(self, painter, option, widget=None):
        """Paint the port (a small circle for input/output ports)."""
        if self.port_type == "input":
            painter.setBrush(QBrush(Qt.green))
        else:
            painter.setBrush(QBrush(Qt.blue))

        painter.drawEllipse(self.boundingRect())  # Draw the port circle

    def update_position(self):
        """Update the position of the port."""
        node_pos = self.parentItem().pos()
        if self.port_type == "input":
            self.setPos(node_pos.x(), node_pos.y())
        else:
            self.setPos(node_pos.x() + 100, node_pos.y())

    def connect(self, port):
        """Connect this port to another port."""
        if port not in self.connected_ports:
            self.connected_ports.append(port)
            port.connect(self)

    def disconnect(self, port):
        """Disconnect this port from another port."""
        if port in self.connected_ports:
            self.connected_ports.remove(port)
            port.disconnect(self)


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


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication, QGraphicsView, QMainWindow, QVBoxLayout, QWidget

    app = QApplication([])
    window = QMainWindow()
    main_widget = QWidget()
    layout = QVBoxLayout(main_widget)

    # Create a NodeEditor and add it to a QGraphicsView
    node_editor = NodeEditor()
    view = QGraphicsView(node_editor)
    layout.addWidget(view)
    main_widget.setLayout(layout)

    # Set up main window
    window.setCentralWidget(main_widget)
    window.setWindowTitle("Node Graphics Item")
    window.show()

    # Add some nodes
    node_editor.add_node("AND Gate")
    node_editor.add_node("OR Gate")

    app.exec_()
