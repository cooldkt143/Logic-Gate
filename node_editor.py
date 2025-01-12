from PyQt5.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush


class NodeEditor:
    def __init__(self):
        self.scene = QGraphicsScene()
        self.nodes = []
        self.undo_stack = []
        self.redo_stack = []

    def add_node(self, node_type):
        """Adds a graphical representation of a node to the scene."""
        node_item = NodeGraphicsItem(node_type)
        self.scene.addItem(node_item)
        self.nodes.append(node_item)
        
        # Store the action for undo
        self.undo_stack.append(('add', node_item))

        # Clear redo stack, as a new action invalidates redo history
        self.redo_stack.clear()

    def remove_node(self, node_item):
        """Removes a node from the scene."""
        self.scene.removeItem(node_item)
        self.nodes.remove(node_item)

        # Store the action for undo
        self.undo_stack.append(('remove', node_item))

        # Clear redo stack, as a new action invalidates redo history
        self.redo_stack.clear()

    def undo(self):
        """Undo the last action."""
        if not self.undo_stack:
            return
        
        action, item = self.undo_stack.pop()
        
        if action == 'add':
            self.remove_node(item)
        elif action == 'remove':
            self.scene.addItem(item)
            self.nodes.append(item)
        
        # Push the reversed action to redo stack
        self.redo_stack.append((action, item))

    def redo(self):
        """Redo the last undone action."""
        if not self.redo_stack:
            return
        
        action, item = self.redo_stack.pop()
        
        if action == 'add':
            self.scene.addItem(item)
            self.nodes.append(item)
        elif action == 'remove':
            self.remove_node(item)

        # Push the action back to undo stack
        self.undo_stack.append((action, item))

    def save_scene(self):
        """Saves the current scene to a dictionary."""
        data = {
            "nodes": [
                {
                    "type": node.node_type,
                    "x": node.x(),
                    "y": node.y()
                }
                for node in self.nodes
            ]
        }
        return data

    def load_scene(self, data):
        """Loads a scene from a dictionary."""
        self.clear_scene()
        for node_data in data.get("nodes", []):
            node_item = NodeGraphicsItem(node_data["type"])
            node_item.setPos(node_data["x"], node_data["y"])
            self.scene.addItem(node_item)
            self.nodes.append(node_item)

    def clear_scene(self):
        """Clears the entire scene."""
        self.scene.clear()
        self.nodes = []
        self.undo_stack.clear()
        self.redo_stack.clear()


class NodeGraphicsItem(QGraphicsItem):
    def __init__(self, node_type):
        super().__init__()
        self.node_type = node_type
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

    def boundingRect(self):
        return QRectF(0, 0, 100, 50)

    def paint(self, painter, option, widget=None):
        painter.setPen(QPen(Qt.black))
        painter.setBrush(QBrush(Qt.lightGray))
        painter.drawRect(self.boundingRect())
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.node_type)
