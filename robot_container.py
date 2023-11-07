from commands2 import button
from commands.flywheel_cmd import FlywheelCMD
from subsystems.flywheel import Flywheel
from wpilib import XboxController
from constants import ButtonMappings


class RobotContainer:
    def __init__(self) -> None:
        self.flywheel = Flywheel()
        self.flywheel.setDefaultCommand(FlywheelCMD(self.flywheel))
        self.controller = XboxController(0)
        self.configure_button_bindings()

    def configure_button_bindings(self):
        button.JoystickButton(self.controller, ButtonMappings.A).onTrue(
            FlywheelCMD(self.flywheel)
        )
