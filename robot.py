import wpilib
import commands2
from robot_container import RobotContainer
from commands2 import CommandScheduler


class MyRobot(commands2.TimedCommandRobot):
    def robotInit(self) -> None:
        self.container = RobotContainer()

    def robotPeriodic(self) -> None:
        CommandScheduler.getInstance().run()


if __name__ == "__main__":
    wpilib.run(MyRobot)
