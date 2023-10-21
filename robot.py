import wpilib
from rev import CANSparkMax
import commands2
from wpilib import SmartDashboard


class MyRobot(commands2.TimedCommandRobot):
    def autonomousInit(self) -> None:
        SmartDashboard.init()
        return super().autonomousInit()

    def autonomousPeriodic(self) -> None:
        return super().autonomousPeriodic()

    def teleopInit(self) -> None:
        return super().teleopInit()

    def teleopPeriodic(self) -> None:
        return super().teleopPeriodic()


if __name__ == "__main__":
    wpilib.run(MyRobot)
