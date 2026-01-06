import math
import socket

# Mensuration calculations function
def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""
    
    # Define dimensions
    r = 7.5      # radius
    l, b, h = 12, 8, 5  # length, breadth, height
    a = 6        # side length
    
    # 2D Shapes Calculations
    area_circle = math.pi * r ** 2
    peri_circle = 2 * math.pi * r
    area_rect = l * b
    peri_rect = 2 * (l + b)
    area_square = a ** 2
    peri_square = 4 * a
    area_triangle = 0.5 * b * h
    
    # 3D Shapes Calculations
    sa_cube = 6 * a ** 2
    vol_cube = a ** 3
    sa_cuboid = 2 * (l*b + b*h + h*l)
    vol_cuboid = l * b * h
    sa_cylinder = 2 * math.pi * r * (r + h)
    vol_cylinder = math.pi * r ** 2 * h
    
    # Calculate total sum of all measurements
    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )
    
    return total

# Server code
def run_server():
    port = 60000
    s = socket.socket()
    host = socket.gethostname()
    s.bind((host, port))
    s.listen(5)
    print('Server listening on port', port)
    
    while True:
        conn, addr = s.accept()
        print('Got connection from', addr)
        
        # Receive data from client
        data = conn.recv(1024)
        print('Server received:', repr(data.decode()))
        
        # Get mensuration calculation result
        result = mensuration_calculations()
        message = f"Mensuration calculation total: {result:.2f}"
        
        # Send result to client
        conn.send(message.encode())
        print('Sent result to client')
        
        # Send a thank you message
        conn.send(b"\n->Thank you for connecting")
        conn.close()
        print('Connection closed\n')

# Main program
if __name__ == "__main__":
    run_server()
