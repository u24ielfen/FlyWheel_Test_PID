from wpimath.controller import PIDController
from commands2 import PIDSubsystem
from rev import CANSparkMax, CANSparkMaxLowLevel
from constants import FlywheelConstants


class Flywheel(PIDSubsystem):
    def __init__(self, controller: PIDController, initialPosition: float = 0) -> None:
        super().__init__(controller, initialPosition)
        self.motor = CANSparkMax(
            FlywheelConstants.flywheel_motor_id,
            CANSparkMaxLowLevel.MotorType.kBrushless,
        )
        self.motor.setIdleMode(CANSparkMax.IdleMode.kBrake)
        encoder = self.motor.getEncoder()
        self.setSetpoint(0)
        self.getController().setTolerance(
            FlywheelConstants.position_tolerance, FlywheelConstants.velocity_tolerance
        )

    def _useOutput(self, output: float, setpoint: float) -> None:
        output = self.clamp(output, -1, 1)
        self.motor.set(output)

    def periodic(self) -> None:
        return super().periodic()

    def clamp(n, min, max):
        if n < min:
            return min
        elif n > max:
            return max
        else:
            return n
