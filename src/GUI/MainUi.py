import sys
import os
import numpy as np
from PySide6 import QtWidgets
from PySide6.QtGui import QAction, QKeySequence, QPixmap, QFont
from PySide6.QtCore import Slot, Qt

from config.Rocket_Config import RocketConfig, Motor
from config.Simulation_Config import simulation, Time, SimulationData

from gui.RocketConfigUi import RocketConfigUi
from gui.MotorConfigUi import MotorConfigUi
from gui.SimulationConfigUi import SimulationUi
from gui.FigureWidget import FigureWidget



class MainUi(QtWidgets.QMainWindow):
    def __init__(self, rocket: RocketConfig, motor: Motor, time: Time, parent = None):
        super().__init__(parent)
        self.rocket = rocket
        self.motor = motor
        self.time = time
        self.data = SimulationData()
        
        centralWidget = QtWidgets.QWidget()
        headerWidget = QtWidgets.QWidget()
        interfaceWidget = QtWidgets.QWidget()
        configWidget = QtWidgets.QWidget()
        configWidget.setFixedWidth(225)
        simulationWidget = QtWidgets.QWidget()
        
        # Redfine director for pyinstaller 
        BASE_DIR = os.path.dirname(__file__)
        imagePath = os.path.join(BASE_DIR, "images", "HornetLogo.png")
        logoPath = QPixmap(imagePath).scaled(configWidget.width(), configWidget.width(), aspectMode = Qt.KeepAspectRatio , mode = Qt.SmoothTransformation)
        logoLabel = QtWidgets.QLabel()
        logoLabel.setPixmap(logoPath)
        
        titleLabel = QtWidgets.QLabel()
        titleLabel.setText("Rocket Model")
        titleFont = QFont()
        titleFont.bold()
        titleFont.setPointSize(20)
        titleLabel.setFont(titleFont)
        
        headerLayout = QtWidgets.QHBoxLayout()
        headerLayout.addWidget(logoLabel)
        headerLayout.addWidget(titleLabel, alignment = Qt.AlignmentFlag.AlignLeading.AlignLeft)
        headerLayout.addStretch()
        headerWidget.setLayout(headerLayout)

        
        rocketConfigWidget = RocketConfigUi(self.rocket, self)
        motorConfigWidget = MotorConfigUi(self.motor, self)
        
        self.textbox = QtWidgets.QTextEdit()
        
        
        configLayout = QtWidgets.QVBoxLayout()
        configLayout.addWidget(rocketConfigWidget)
        configLayout.addWidget(motorConfigWidget)
        configLayout.addWidget(self.textbox)
        #configLayout.addStretch()
        configWidget.setLayout(configLayout)
        
        
        simulationConfigWidget = SimulationUi(self.time, self)
        self.figureWidget = FigureWidget(self)
        
        simulationLayout = QtWidgets.QVBoxLayout()
        simulationLayout.addWidget(simulationConfigWidget)
        simulationLayout.addWidget(self.figureWidget)
        simulationLayout.addStretch()
        simulationWidget.setLayout(simulationLayout)
        
        interfaceLayout = QtWidgets.QHBoxLayout()
        interfaceLayout.addWidget(configWidget, alignment = Qt.AlignmentFlag.AlignLeft)
        interfaceLayout.addWidget(simulationWidget, alignment=Qt.AlignmentFlag.AlignTop)
        interfaceWidget.setLayout(interfaceLayout)
               
        
        centralLayout = QtWidgets.QVBoxLayout()
        centralLayout.addWidget(headerWidget)
        centralLayout.addWidget(interfaceWidget)
        centralWidget.setLayout(centralLayout)
        self.setCentralWidget(centralWidget)
        
        self.addAction
        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        
        
    @Slot()
    def runSimulation(self):
        inital_conditions = np.array([0, 0, self.rocket.rocket_mass_0])
        statevector, time_array = simulation(inital_conditions, self.time, self.rocket, self.motor)
        self.data.update_data(statevector, time_array, self)
        self.figureWidget.updateCanvas()
        
    @Slot()
    def appendText(self, text):
        self.textbox.append(text)


if __name__ == "__main__":
    
    # testing rocket data
    rocket_mass_0 = 32098/1000 # kilograms
    drag_coefficient = 0.36 #cf
    diameter = 0.155 # meters
    rocket = RocketConfig(rocket_mass_0, drag_coefficient, diameter)
    
    # n Rocket Motor Perameters
    FuelMass = 7512.0/1000.0 # kg
    ThrustAvg = 3168.0 # F
    TotalImpulse = 14041.0 # Ns
    burn_time = 4.4 #s
    Nmotor = Motor(FuelMass, ThrustAvg, TotalImpulse, burn_time)
    
    time = Time(0, 63, 0.001)
    
    
    # testing .ui
    app = QtWidgets.QApplication(sys.argv)
    ui = MainUi(rocket, Nmotor, time)
    ui.show()
    
    sys.exit(app.exec())
    