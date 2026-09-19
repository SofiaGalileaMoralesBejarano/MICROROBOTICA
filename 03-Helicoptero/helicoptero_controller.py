from controller import Robot

# Inicializar el robot (Helicóptero)
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# En Webots, los helicópteros y drones usan motores rotacionales de alta velocidad 
# para las hélices (normalmente llamados 'propeller_motor' o 'rotor')
motor_helice_principal = robot.getDevice('main_rotor_motor')
motor_helice_cola = robot.getDevice('tail_rotor_motor')

# Configurar motores en modo velocidad infinita
if motor_helice_principal and motor_helice_cola:
    motor_helice_principal.setPosition(float('inf'))
    motor_helice_cola.setPosition(float('inf'))
    
    # Asignar una velocidad alta para generar sustentación (elevarse)
    motor_helice_principal.setVelocity(50.0) 
    motor_helice_cola.setVelocity(20.0)

print("Controlador del helicóptero iniciado. Elevando motores...")

# Bucle principal de simulación
while robot.step(timestep) != -1:
    # Aquí puedes añadir controles por teclado más adelante si lo requieres
    pass