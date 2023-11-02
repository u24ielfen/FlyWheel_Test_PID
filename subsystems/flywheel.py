from wpimath.controller import PIDController
from commands2 import PIDSubsystem
from rev import CANSparkMax, CANSparkMaxLowLevel
from constants import FlywheelConstants
from wpilib import SmartDashboard


class Flywheel(PIDSubsystem):
    def __init__(self, initialPosition: float = 0) -> None:
        super().__init__(
            PIDController(
                FlywheelConstants.kP, FlywheelConstants.kI, FlywheelConstants.kD
            )
        )
        self.motor = CANSparkMax(
            FlywheelConstants.flywheel_motor_id,
            CANSparkMaxLowLevel.MotorType.kBrushless,
        )

        self.motor.setIdleMode(CANSparkMax.IdleMode.kCoast)
        self.encoder = self.motor.getEncoder()
        self.setSetpoint(0)
        self.getController().setTolerance()

    def _useOutput(self, output: float, setpoint: float) -> None:
        output = self.clamp(output, -1, 1)
        self.motor.set(output)

    def _getMeasurement(self) -> float:
        return self.encoder.getVelocity()

    def periodic(self) -> None:
        super().periodic()
        SmartDashboard.putBoolean("PID Subsystem Enabled", self.isEnabled())
        SmartDashboard.putNumber("PID Setpoint", self.getSetpoint())

    def clamp(n, min, max):
        if n < min:
            return min
        elif n > max:
            return max
        else:
            return n
