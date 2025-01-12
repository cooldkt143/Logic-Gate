from PyQt5.QtWidgets import QGraphicsItem, QGraphicsScene, QGraphicsView
from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QPen, QBrush


class NodeEditor:
    def __init__(self):
        self.scene = QGraphicsScene()
        self.nodes = []
        self.clipboard = []  # Clipboard to store cut/copied nodes
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

    def cut_nodes(self):
        """Cuts the selected nodes and stores them in the clipboard."""
        selected_nodes = [node for node in self.nodes if node.isSelected()]
        
        # Store cut nodes in clipboard
        self.clipboard = selected_nodes[:]
        
        # Remove selected nodes from the scene
        for node in selected_nodes:
            self.remove_node(node)
        
        # Store the action for undo
        self.undo_stack.append(('cut', self.clipboard[:]))  # Storing the nodes that were cut

        # Clear redo stack, as a new action invalidates redo history
        self.redo_stack.clear()

    def paste_nodes(self):
        """Pastes the nodes from the clipboard into the scene."""
        if not self.clipboard:
            return
        
        # Paste each node from clipboard
        for node in self.clipboard:
            node_item = NodeGraphicsItem(node.node_type)
            node_item.setPos(node.x(), node.y())  # Preserve the original position
            self.scene.addItem(node_item)
            self.nodes.append(node_item)
        
        # Store the action for undo
        self.undo_stack.append(('paste', self.clipboard[:]))  # Storing pasted nodes
        
        # Clear redo stack, as a new action invalidates redo history
        self.redo_stack.clear()

    def delete_nodes(self):
        """Deletes the selected nodes."""
        selected_nodes = [node for node in self.nodes if node.isSelected()]
        
        # Remove selected nodes from the scene
        for node in selected_nodes:
            self.remove_node(node)
        
        # Store the deleted nodes for undo
        self.undo_stack.append(('delete', selected_nodes[:]))
        
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
        elif action == 'cut':
            for node in item:
                self.scene.addItem(node)
                self.nodes.append(node)
        elif action == 'delete':
            for node in item:
                self.scene.addItem(node)
                self.nodes.append(node)
        
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
        elif action == 'cut':
            for node in item:
                self.remove_node(node)
        elif action == 'delete':
            for node in item:
                self.remove_node(node)

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
