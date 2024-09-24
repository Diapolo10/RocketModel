import sys
import os
from PySide6 import QtCore, QtGui, QtWidgets

# Add the parent directory to the system path for user class import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Rocket_Config import Motor


class MotorConfigUi(QtWidgets.QWidget):
    def __init__(self, motor: Motor, parent = None):
        super().__init__(parent)
        self.motor = motor
       
        self.configLabel = QtWidgets.QLabel()
        self.configLabel.setGeometry(QtCore.QRect(0, 15, 201, 21))
        font = QtGui.QFont()
        font.setBold(True)
        self.configLabel.setFont(font)
        self.configLabel.setText("Motor Configuration:")
        
        self.fuelMassLabel = QtWidgets.QLabel()
        self.fuelMassLabel.setGeometry(QtCore.QRect(0, 50, 100, 16))
        self.fuelMassLabel.setText("Fuel Mass (kg):")
        
        self.fuelMassEdit = QtWidgets.QLineEdit()
        self.fuelMassEdit.setGeometry(QtCore.QRect(150, 50, 100, 20))
        self.fuelMassEdit.setText(str(self.motor.mass_fuel))
        self.fuelMassEdit.editingFinished.connect(self.setFuelMass)
                
        self.avgThrustLabel = QtWidgets.QLabel()
        self.avgThrustLabel.setGeometry(QtCore.QRect(0, 75, 100, 16))
        self.avgThrustLabel.setText("Average Thrust (N):")
        
        self.avgThrustEdit = QtWidgets.QLineEdit()
        self.avgThrustEdit.setGeometry(QtCore.QRect(150, 75, 100, 20))
        self.avgThrustEdit.setText(str(self.motor.thrust_avg))
        self.avgThrustEdit.editingFinished.connect(self.setAvgThrust)
                
        self.totalImpulseLabel = QtWidgets.QLabel()
        self.totalImpulseLabel.setGeometry(QtCore.QRect(0, 100, 100, 16))
        self.totalImpulseLabel.setText("Total Impuse (N*s):")
        
        self.totalImpulseEdit = QtWidgets.QLineEdit()
        self.totalImpulseEdit.setGeometry(QtCore.QRect(150, 100, 100, 20))
        self.totalImpulseEdit.setText(str(self.motor.total_impulse))
        self.totalImpulseEdit.editingFinished.connect(self.setTotalImpulse)
        
        self.burnTimeLabel = QtWidgets.QLabel()
        self.burnTimeLabel.setGeometry(QtCore.QRect(0, 100, 100, 16))
        self.burnTimeLabel.setText("Burn time: (s):")
        
        self.burnTimeEdit = QtWidgets.QLineEdit()
        self.burnTimeEdit.setGeometry(QtCore.QRect(150, 100, 100, 20))
        self.burnTimeEdit.setText(str(self.motor.burn_time))
        self.burnTimeEdit.editingFinished.connect(self.setBurnTime)
        
        self.ISPLabel = QtWidgets.QLabel()
        self.ISPLabel.setGeometry(QtCore.QRect(0, 100, 100, 16))
        self.ISPLabel.setText("ISP (s):")
        
        self.ISPvalueLabel = QtWidgets.QLabel()
        self.ISPvalueLabel.setGeometry(QtCore.QRect(150, 100, 100, 20))
        self.ISPvalueLabel.setText(str(self.motor.ISP))

        formLayout = QtWidgets.QFormLayout(self)
        formLayout.addRow(self.configLabel)
        formLayout.addRow(self.fuelMassLabel, self.fuelMassEdit)
        formLayout.addRow(self.avgThrustLabel, self.avgThrustEdit)
        formLayout.addRow(self.burnTimeLabel, self.burnTimeEdit)
        formLayout.addRow(self.totalImpulseLabel, self.totalImpulseEdit)
        formLayout.addRow(self.ISPLabel, self.ISPvalueLabel)
        
    def setFuelMass(self):
        self.motor.mass_fuel = float(self.fuelMassEdit.text())
        print(self.motor.mass_fuel)
        
    def setAvgThrust(self):
        self.motor.thrust_avg = float(self.avgThrustEdit.text())
        print(self.motor.thrust_avg)
        
    def setBurnTime(self):
        self.motor.burn_time = float(self.burnTimeEditEdit.text())
        print(self.motor.burn_time)
            
    def setTotalImpulse(self):
        self.motor.total_impulse = float(self.totalImpulseEdit.text())
        print(self.motor.total_impulse)
        
        
    


if __name__ == "__main__":
    
    # n Rocket Motor Perameters
    FuelMass = 7512.0/1000.0 # kg
    ThrustAvg = 3168.0 # F
    TotalImpulse = 14041.0 # Ns
    burn_time = 4.4 #s
    Nmotor = Motor(FuelMass, ThrustAvg, TotalImpulse, burn_time)
   
   
    #print(Nmotor.motor_output(1), type(Nmotor.motor_output(1)) )
    
    # testing .ui
    app = QtWidgets.QApplication()
    ui = MotorConfigUi(Nmotor)
    ui.show()
    
    sys.exit(app.exec())
    