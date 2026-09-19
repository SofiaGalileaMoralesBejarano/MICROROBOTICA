from controller import Robot


robot = Robot()


timestep = int(robot.getBasicTimeStep())


motor_izquierdo = robot.getDevice('left wheel motor')


motor_izquierdo.setPosition(float('inf'))


motor_izquierdo.setVelocity(5.0)


while robot.step(timestep) != -1:
   
    pass