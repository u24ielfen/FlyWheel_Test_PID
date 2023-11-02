import wpilib
from rev import CANSparkMax
import commands2
from wpilib import SmartDashboard
from robot_container import RobotContainer
from commands2 import CommandScheduler
from wpimath.controller import PIDController


class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()

    def robotPeriodic(self) -> None:
        #     controller = PIDController(0.9, 0.0, 0.0)
        #     controller.setSetpoint(200)

        CommandScheduler.getInstance().run()


if __name__ == "__main__":
    wpilib.run(MyRobot)
