import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QTabWidget, QFileDialog, QAction, QMenuBar, QListWidget, QWidget
from node import NodeEditor  # Import your NodeEditor class

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logic Nodes Application")
        self.resize(1200, 800)

        # Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Components
        self.create_topbar_menu()
        self.create_side_panel()
        self.create_tabbed_node_editor()

        # Add to layout
        self.layout.addWidget(self.side_panel, 1)
        self.layout.addWidget(self.tab_widget, 4)

    def create_topbar_menu(self):
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # File menu
        file_menu = menu_bar.addMenu("File")
        new_action = QAction("New", self)
        open_action = QAction("Open", self)
        save_action = QAction("Save", self)
        exit_action = QAction("Exit", self)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)

        new_action.triggered.connect(self.create_new_tab)
        open_action.triggered.connect(self.open_file)
        save_action.triggered.connect(self.save_file)
        exit_action.triggered.connect(self.close)

    def create_side_panel(self):
        self.side_panel = QListWidget()
        self.side_panel.setFixedWidth(200)
        self.side_panel.addItem("Input")
        self.side_panel.addItem("Output")
        self.side_panel.addItem("And")
        self.side_panel.addItem("Or")
        self.side_panel.addItem("Not")

    def create_tabbed_node_editor(self):
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        self.create_new_tab()

    def create_new_tab(self):
        new_editor = NodeEditor()  # NodeEditor must be defined in node_editor.py
        self.tab_widget.addTab(new_editor, "New Graph")

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "JSON Files (*.json)")
        if file_path:
            new_editor = NodeEditor()
            new_editor.load_from_file(file_path)
            self.tab_widget.addTab(new_editor, file_path.split("/")[-1])

    def save_file(self):
        current_editor = self.tab_widget.currentWidget()
        if current_editor:
            file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "JSON Files (*.json)")
            if file_path:
                current_editor.save_to_file(file_path)

    def close_tab(self, index):
        self.tab_widget.removeTab(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
