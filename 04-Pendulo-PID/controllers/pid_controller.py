from controller import Robot

# 1. Inicializar el robot y el tiempo de paso
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# 2. Obtener los dispositivos del péndulo
# El motor controla la posición del carro; el sensor mide el ángulo del péndulo
motor_carro = robot.getDevice('cart_motor')
sensor_angulo = robot.getDevice('pendulum_sensor')

# Activar el sensor de ángulo especificando el tiempo de muestreo
if sensor_angulo:
    sensor_angulo.enable(timestep)

# Configurar el motor en modo de velocidad/fuerza
if motor_carro:
    motor_carro.setPosition(float('inf'))
    motor_carro.setVelocity(0.0)

# =========================================================================
# 🔴 SECCIÓN DE SINTONIZACIÓN MANUAL DEL PID
# Cambia estos 3 valores manualmente para estabilizar el péndulo
# =========================================================================
Kp = 40.0   # Constante Proporcional (reacciona al error actual)
Ki = 0.5    # Constante Integral (corrige errores acumulados en el tiempo)
Kd = 10.0   # Constante Derivativa (amortigua el movimiento y evita oscilaciones)

# Variables internas del algoritmo PID
error_anterior = 0.0
integral = 0.0

print("Controlador PID Manual Iniciado. Intentando balancear el péndulo...")

# 3. Bucle principal de control
while robot.step(timestep) != -1:
    if not sensor_angulo:
        continue
        
    # El objetivo es que el ángulo sea 0.0 radianes (perfectamente vertical)
    posicion_actual = sensor_angulo.getValue()
    error = 0.0 - posicion_actual
    
    # Cálculo de los 3 términos del PID
    proporcional = error
    integral += error * (timestep / 1000.0)
    derivativa = (error - error_anterior) / (timestep / 1000.0)
    
    # Ecuación del PID para calcular la velocidad de corrección del motor
    salida_velocidad = (Kp * proporcional) + (Ki * integral) + (Kd * derivativa)
    
    # Guardar el error actual para el siguiente ciclo
    error_anterior = error
    
    # Aplicar la velocidad calculada limitándola a un máximo seguro (ej. 10.0)
    if motor_carro:
        velocidad_final = max(min(salida_velocidad, 10.0), -10.0)
        motor_carro.setVelocity(velocidad_final)