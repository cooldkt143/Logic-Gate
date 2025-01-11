import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene, QGraphicsView, QListWidgetItem
from ui.main_win import Ui_MainWindow

class LogicNodesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Setup scene for the node editor
        self.scene = QGraphicsScene()
        self.ui.graphicsView.setScene(self.scene)

        # Connect menu actions
        self.ui.actionNew.triggered.connect(self.new_file)
        self.ui.actionOpen.triggered.connect(self.open_file)
        self.ui.actionSave.triggered.connect(self.save_file)
        self.ui.actionExit.triggered.connect(self.close)

        # Add nodes to the sidebar
        self.setup_nodes()

    def setup_nodes(self):
        """Add nodes to the sidebar."""
        nodes = ['Input', 'Output', 'And', 'Or', 'Not', 'Nand', 'Nor', 'Xor', 'Xnor']
        for node in nodes:
            item = QListWidgetItem(node)
            self.ui.nodeList.addItem(item)

    def new_file(self):
        """Create a new node editor tab."""
        # Logic for adding a new tab with an empty canvas

    def open_file(self):
        """Open an existing node file."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Node File", "", "Node Files (*.json)")
        if file_path:
            # Logic for loading node file
            pass

    def save_file(self):
        """Save the current node editor state."""
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Node File", "", "Node Files (*.json)")
        if file_path:
            # Logic for saving node file
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LogicNodesApp()
    window.show()
    sys.exit(app.exec_())
