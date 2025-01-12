import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from ui.main_win import Ui_MainWindow
from node_editor import NodeEditor


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Integrate the NodeEditor with the QGraphicsView
        self.node_editor = NodeEditor()
        self.ui.graphicsView.setScene(self.node_editor.scene)

        # Connect menu actions to their respective functions
        self.ui.actionNew.triggered.connect(self.new_file)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionUndo.triggered.connect(self.node_editor.undo)
        self.ui.actionRedo.triggered.connect(self.node_editor.redo)

        # Populate the listWidget with node types
        self.ui.listWidget.itemClicked.connect(self.add_node)

    def new_file(self):
        """Clears the node editor to start a new file."""
        self.node_editor.clear_scene()

    def open_file(self):
        """Opens an existing node editor file."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Node Editor File", "", "JSON Files (*.json)")
        if file_path:
            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                    self.node_editor.load_scene(data)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file: {e}")

    def save_file(self):
        """Saves the current state of the node editor."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Node Editor File", "", "JSON Files (*.json)")
        if file_path:
            try:
                data = self.node_editor.save_scene()
                with open(file_path, "w") as file:
                    json.dump(data, file, indent=4)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file: {e}")

    def add_node(self, item):
        """Adds a new node based on the selected type from the listWidget."""
        node_type = item.text()
        self.node_editor.add_node(node_type)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
