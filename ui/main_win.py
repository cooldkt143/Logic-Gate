from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGraphicsView, QFrame
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Graphics View
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(190, 0, 1721, 921))
        self.graphicsView.setFrameShape(QFrame.NoFrame)
        self.graphicsView.setMidLineWidth(0)
        self.graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setObjectName("graphicsView")

        # List Widget
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 191, 921))
        self.listWidget.setObjectName("listWidget")
        for text in ["INPUT", "OUTPUT", "AND", "OR", "NOT", "NAND", "NOR", "XOR"]:
            item = QtWidgets.QListWidgetItem(text)
            self.listWidget.addItem(item)

        # Line Edit
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 90, 191, 61))
        self.lineEdit.setObjectName("lineEdit")

        # Combo Box
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(240, 110, 131, 24))
        self.comboBox.addItems(["0", "1"])
        self.comboBox.setObjectName("comboBox")

        # Push Button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 110, 21, 21))
        self.pushButton.setText("->")
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)

        # Menubar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 33))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setTitle("File")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setTitle("Edit")
        self.menuwindows = QtWidgets.QMenu(self.menubar)
        self.menuwindows.setTitle("Window")
        MainWindow.setMenuBar(self.menubar)

        # Status Bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        # Actions
        self.actionNew = QtWidgets.QAction(MainWindow, text="New", shortcut="Ctrl+N")
        self.actionOpen = QtWidgets.QAction(MainWindow, text="Open", shortcut="Ctrl+O")
        self.actionSave = QtWidgets.QAction(MainWindow, text="Save", shortcut="Ctrl+S")
        self.actionExit = QtWidgets.QAction(MainWindow, text="Exit", shortcut="Esc")
        self.actionUndo = QtWidgets.QAction(MainWindow, text="Undo", shortcut="Ctrl+U")
        self.actionRedo = QtWidgets.QAction(MainWindow, text="Redo", shortcut="Ctrl+R")
        self.actionCut = QtWidgets.QAction(MainWindow, text="Cut", shortcut="Ctrl+X")
        self.actionPaste = QtWidgets.QAction(MainWindow, text="Paste", shortcut="Ctrl+V")
        self.actionDelete = QtWidgets.QAction(MainWindow, text="Delete", shortcut="Ctrl+Del")
        self.actionTheme = QtWidgets.QAction(MainWindow, text="Theme")

        self.menufile.addActions([self.actionNew, self.actionOpen, self.actionSave, self.actionExit])
        self.menuedit.addActions([self.actionUndo, self.actionRedo, self.actionCut, self.actionPaste, self.actionDelete])
        self.menuwindows.addAction(self.actionTheme)

        self.menubar.addMenu(self.menufile)
        self.menubar.addMenu(self.menuedit)
        self.menubar.addMenu(self.menuwindows)

        # Signals
        self.actionTheme.triggered.connect(self.change_theme)

        # Set default theme
        self.set_light_theme()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "File"))
        self.menuedit.setTitle(_translate("MainWindow", "Edit"))
        self.menuwindows.setTitle(_translate("MainWindow", "Window"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionTheme.setText(_translate("MainWindow", "Theme"))


    def change_theme(self):
        if QtWidgets.QApplication.palette().color(QtGui.QPalette.Window) == QtCore.Qt.white:
            self.set_dark_theme()
        else:
            self.set_light_theme()

    def set_dark_theme(self):
        """Set dark theme."""
        dark_palette = QtGui.QPalette()
        dark_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(53, 53, 53))
        dark_palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(255, 255, 255))
        dark_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(25, 25, 25))
        dark_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(53, 53, 53))
        dark_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(255, 255, 255))
        dark_palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(255, 255, 255))
        dark_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(255, 255, 255))
        dark_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(53, 53, 53))
        dark_palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(255, 255, 255))
        dark_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(142, 45, 197).lighter())
        dark_palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(0, 0, 0))

        QtWidgets.QApplication.setPalette(dark_palette)

        # Apply explicit styles for QMenuBar
        self.apply_styles(
            """
            QMenuBar {
                background-color: #353535;
                color: black;  /* Ensure black text */
            }
            QMenuBar::item {
                background: transparent;
                color: black;  /* Explicitly set individual menu items to black */
            }
            QMenuBar::item:selected {
                background: #505050;
                color: black;
            }
            QMenu {
                background-color: #353535;
                color: white;  /* Menu dropdown items stay white */
            }
            QMenu::item:selected {
                background-color: #505050;
                color: white;
            }
            QGraphicsView {
                background-color: #2B2B2B;
            }
            QListWidget {
                background-color: #2B2B2B;
                color: white;
            }
            """
        )

        # Set QMenuBar text color programmatically as a fallback
        self.menubar.setStyleSheet("color: white; background-color: #353535;")

        for menu in [self.menufile, self.menuedit, self.menuwindows]:
            menu.setStyleSheet("color: white; background-color: #353535;")

    def set_light_theme(self):
        """Set light theme."""
        light_palette = QtGui.QPalette()
        light_palette.setColor(QtGui.QPalette.Window, QtGui.QColor(255, 255, 255))
        light_palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor(0, 0, 0))
        light_palette.setColor(QtGui.QPalette.Base, QtGui.QColor(255, 255, 255))
        light_palette.setColor(QtGui.QPalette.AlternateBase, QtGui.QColor(233, 233, 233))
        light_palette.setColor(QtGui.QPalette.ToolTipBase, QtGui.QColor(255, 255, 255))
        light_palette.setColor(QtGui.QPalette.ToolTipText, QtGui.QColor(0, 0, 0))
        light_palette.setColor(QtGui.QPalette.Text, QtGui.QColor(0, 0, 0))
        light_palette.setColor(QtGui.QPalette.Button, QtGui.QColor(233, 233, 233))
        light_palette.setColor(QtGui.QPalette.ButtonText, QtGui.QColor(0, 0, 0))
        light_palette.setColor(QtGui.QPalette.BrightText, QtGui.QColor(255, 0, 0))
        light_palette.setColor(QtGui.QPalette.Highlight, QtGui.QColor(76, 163, 224))
        light_palette.setColor(QtGui.QPalette.HighlightedText, QtGui.QColor(255, 255, 255))

        QtWidgets.QApplication.setPalette(light_palette)

        # Apply custom styles
        self.apply_styles(
            "QMenuBar { background-color: #FFFFFF; color: black; }"
            "QMenu { background-color: #FFFFFF; color: black; }"
            "QGraphicsView { background-color: #F0F0F0; }"
            "QListWidget { background-color: #FFFFFF; color: black; }"
        )

                # Set QMenuBar text color programmatically as a fallback
        self.menubar.setStyleSheet("color: black; background-color: #FFFFFF;")

        for menu in [self.menufile, self.menuedit, self.menuwindows]:
            menu.setStyleSheet("color: black; background-color: #FFFFFF;")

    def apply_styles(self, style_sheet):
        """Apply a stylesheet to the main window."""
        self.centralwidget.setStyleSheet(style_sheet)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
