# check whether SuperRobot is a subclass of AstromechDroid,
# MedicalDroid, BattleDroid, and PilotDroid

# the order is IMPORTANT

# class SuperRobot:
#     pass
#
#
# class AstromechDroid(SuperRobot):
#     pass
#
#
# class MedicalDroid(SuperRobot):
#     pass
#
#
# class BattleDroid(SuperRobot):
#     pass
#
#
# class PilotDroid(SuperRobot):
#     pass


print(issubclass(SuperRobot, AstromechDroid))
print(issubclass(SuperRobot, MedicalDroid))
print(issubclass(SuperRobot, BattleDroid))
print(issubclass(SuperRobot, PilotDroid))
