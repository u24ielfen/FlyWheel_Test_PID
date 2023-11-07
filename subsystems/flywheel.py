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
        # SmartDashboard Setup
        SmartDashboard.putNumber("kP", FlywheelConstants.kP)
        SmartDashboard.putNumber("kI", FlywheelConstants.kI)
        SmartDashboard.putNumber("kD", FlywheelConstants.kD)
        SmartDashboard.putBoolean("Reset Position", False)
        SmartDashboard.putBoolean("Velocity Mode", True)

        # Motor Setup
        self.motor = CANSparkMax(
            FlywheelConstants.flywheel_motor_id,
            CANSparkMaxLowLevel.MotorType.kBrushless,
        )
        self.motor.setIdleMode(CANSparkMax.IdleMode.kCoast)
        self.encoder = self.motor.getEncoder()

        # PID Setup
        self.setSetpoint(0)
        self.getController().setTolerance(
            FlywheelConstants.position_tolerance, FlywheelConstants.velocity_tolerance
        )

    def _useOutput(self, output: float, setpoint: float) -> None:
        self.motor.set(self.clamp(output, -1, 1))

    def _getMeasurement(self) -> float:
        if SmartDashboard.getBoolean("Velocity Mode", True):
            return self.encoder.getVelocity()
        else:
            return self.encoder.getPosition()

    def setSetpoint(self, setpoint: float) -> None:
        return super().setSetpoint(setpoint)

    def periodic(self) -> None:
        super().periodic()

        # General Telemetry
        SmartDashboard.putBoolean("PID Subsystem Enabled", self.isEnabled())
        SmartDashboard.putNumber("Motor Position", self.encoder.getPosition())
        SmartDashboard.putNumber("Motor Velocity", self.encoder.getVelocity())
        if SmartDashboard.getBoolean("Reset Position", True):
            self.encoder.setPosition(0.0)
            SmartDashboard.putBoolean("Reset Position", False)

        # PID Telemetry
        self.p = SmartDashboard.getNumber("kP", 0.0)
        self.i = SmartDashboard.getNumber("kI", 0.0)
        self.d = SmartDashboard.getNumber("kD", 0.0)
        self.kF = SmartDashboard.getNumber("kFF", 0.0)
        if self.p != FlywheelConstants.kP:
            super().getController().setP(self.p)
        if self.i != FlywheelConstants.kI:
            super().getController().setI(self.i)
        if self.d != FlywheelConstants.kD:
            super().getController().setD(self.d)

    def clamp(n, min, max):
        if n < min:
            return min
        elif n > max:
            return max
        else:
            return n
