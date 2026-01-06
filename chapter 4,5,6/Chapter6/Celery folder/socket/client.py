import math
import socket

def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""
    
    # Define dimensions
    r = 7.5      # radius
    l, b, h = 12, 8, 5  # length, breadth, height
    a = 6        # side length
    
    # 2D Shapes Calculations
    
    # Circle calculations
    area_circle = math.pi * r ** 2            # circle area
    peri_circle = 2 * math.pi * r             # circle perimeter (circumference)
    
    # Rectangle calculations
    area_rect = l * b                         # rectangle area
    peri_rect = 2 * (l + b)                   # rectangle perimeter
    
    # Square calculations
    area_square = a ** 2                      # square area
    peri_square = 4 * a                       # square perimeter
    
    # Triangle calculations
    area_triangle = 0.5 * b * h               # triangle area
    
    # 3D Shapes Calculations
    
    # Cube calculations
    sa_cube = 6 * a ** 2                      # cube surface area
    vol_cube = a ** 3                         # cube volume
    
    # Cuboid calculations
    sa_cuboid = 2 * (l*b + b*h + h*l)         # cuboid surface area
    vol_cuboid = l * b * h                    # cuboid volume
    
    # Cylinder calculations
    sa_cylinder = 2 * math.pi * r * (r + h)   # cylinder surface area
    vol_cylinder = math.pi * r ** 2 * h       # cylinder volume
    
    # Calculate total sum of all measurements
    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )
    
    return total

def connect_to_server():
    """Connect to local server and receive message"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()  # local machine
        port = 9999
        s.connect((host, port))
        message = s.recv(1024)
        s.close()
        return message.decode('ascii')
    except Exception as e:
        return f"Error connecting to server: {e}"

if __name__ == "__main__":
    # Perform mensuration calculations
    result = mensuration_calculations()
    print(f"Mensuration calculation total: {result:.2f}")
    
    # Connect to server
    server_message = connect_to_server()
    print(f"Time connection server: {server_message}")
