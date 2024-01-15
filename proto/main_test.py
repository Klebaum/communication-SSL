import socket
import ssl_simulation_robot_control_pb2 as pb2

def send_message(self, index, wheel_br, wheel_bl, wheel_fr, wheel_fl):
    self.index = index
    self.wheel_br = wheel_br
    self.wheel_bl = wheel_bl
    self.wheel_fr = wheel_fr
    self.wheel_fl = wheel_fl

    # Crie uma mensagem RobotCommand
    msg = pb2.RobotControl()
    msg.robot_commands.add().id = self.index
    msg.robot_commands.add().wheel_br = self.wheel_br
    msg.robot_commands.add().wheel_bl = self.wheel_bl
    msg.robot_commands.add().wheel_fr = self.wheel_fr
    msg.robot_commands.add().wheel_fl = self.wheel_fl

    try:
        # Serializar a mensagem para uma string de bytes
        data = msg.SerializeToString()
        # Crie um socket UDP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Envie a mensagem para o GrSim
        grsim_address = ('localhost', 10302)  # Substitua pelo endereço e porta corretos do GrSim
        sock.sendto(data, grsim_address)
    except Exception as e:
        print(e)
        print("Erro ao enviar mensagem para o GrSim")

# Crie uma mensagem RobotControl
robot_control = pb2.RobotControl()

# Crie uma mensagem RobotCommand
robot_command = robot_control.robot_commands.add()
robot_command.id = 0  # ID do robô para o qual você está enviando o comando

# Crie uma mensagem MoveGlobalVelocity
move_command = pb2.MoveGlobalVelocity()
move_command.x = 10.0
move_command.y = 20.0
move_command.angular = 3.0

# Atribua a mensagem MoveGlobalVelocity ao campo move_command da mensagem RobotCommand
#robot_command.move_command.global_velocity.CopyFrom(move_command)

# Serializar a mensagem para uma string de bytes
data = robot_control.SerializeToString()
# Crie um socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
    # Envie a mensagem para o GrSim
    grsim_address = ('localhost', 10302)  # Substitua pelo endereço e porta corretos do GrSim
    sock.sendto(data, grsim_address)

