from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QGraphicsView, QFrame
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(190, 0, 1721, 921))
        self.graphicsView.setFrameShape(QFrame.NoFrame)
        self.graphicsView.setMidLineWidth(0)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.graphicsView.setInteractive(True)
        self.graphicsView.setObjectName("graphicsView")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 191, 921))
        self.listWidget.setObjectName("listWidget")
        for text in ["INPUT", "OUTPUT", "AND", "OR", "NOT", "NAND", "NOR", "XOR"]:
            item = QtWidgets.QListWidgetItem(text)
            self.listWidget.addItem(item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 33))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuedit = QtWidgets.QMenu(self.menubar)
        self.menuedit.setObjectName("menuedit")
        self.menuwindows = QtWidgets.QMenu(self.menubar)
        self.menuwindows.setObjectName("menuwindows")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.setShortcut("Ctrl+N")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave.setShortcut("Ctrl+S")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.setShortcut("Esc")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionUndo.setShortcut("Ctrl+U")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionRedo.setShortcut("Ctrl+R")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCut.setShortcut("Ctrl+X")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionPaste.setShortcut("Ctrl+V")
        self.actiondelete = QtWidgets.QAction(MainWindow)
        self.actiondelete.setObjectName("actiondelete")
        self.actiondelete.setShortcut("Ctrl+Del")
        self.actiontheme = QtWidgets.QAction(MainWindow)
        self.actiontheme.setObjectName("actiontheme")
        self.actiontheme.triggered.connect(self.change_theme)
        self.menufile.addAction(self.actionNew)
        self.menufile.addAction(self.actionOpen)
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionExit)
        self.menuedit.addAction(self.actionUndo)
        self.menuedit.addAction(self.actionRedo)
        self.menuedit.addAction(self.actionCut)
        self.menuedit.addAction(self.actionPaste)
        self.menuedit.addAction(self.actiondelete)
        self.menuwindows.addAction(self.actiontheme)
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menuwindows.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.set_light_theme()  # Set default theme

    def change_theme(self):
        # Toggle between themes (dark and light)
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
        self.actiondelete.setText(_translate("MainWindow", "Delete"))
        self.actiontheme.setText(_translate("MainWindow", "Theme"))
