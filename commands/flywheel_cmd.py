from commands2 import CommandBase
from subsystems.flywheel import Flywheel


class FlywheelCMD(CommandBase):
    def __init__(self, flywheel: Flywheel) -> None:
        super().__init__()
        self.flywheel = flywheel
        self.addRequirements(flywheel)
        self.done = False

    def execute(self) -> None:
        self.flywheel.setSetpoint(2000)
        self.done = True

    def isFinished(self) -> bool:
        return self.done
