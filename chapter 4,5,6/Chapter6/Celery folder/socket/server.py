import math
import socket

def mensuration_calculations():
    """Calculate various 2D and 3D shapes measurements"""
    
    # Define dimensions
    r = 7.5      # radius
    l, b, h = 12, 8, 5  # length, breadth, height
    a = 6        # side length
    
    # 2D Shapes Calculations
    area_circle = math.pi * r ** 2            # circle area
    peri_circle = 2 * math.pi * r             # circle perimeter (circumference)
    area_rect = l * b                          # rectangle area
    peri_rect = 2 * (l + b)                    # rectangle perimeter
    area_square = a ** 2                       # square area
    peri_square = 4 * a                        # square perimeter
    area_triangle = 0.5 * b * h                # triangle area
    
    # 3D Shapes Calculations
    sa_cube = 6 * a ** 2                       # cube surface area
    vol_cube = a ** 3                          # cube volume
    sa_cuboid = 2 * (l*b + b*h + h*l)          # cuboid surface area
    vol_cuboid = l * b * h                     # cuboid volume
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


# ----------------- Server Code -----------------
def run_server():
    # create a socket object
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # get local machine name
    host = socket.gethostname()
    port = 9999
    # bind to the port
    serversocket.bind((host, port))
    # queue up to 5 requests
    serversocket.listen(5)
    print(f"Server started on {host}:{port}...")
    
    # establish a connection
    while True:
        clientsocket, addr = serversocket.accept()
        print(f"Connected with {addr}")
        
        # Get mensuration calculation result
        result = mensuration_calculations()
        message = f"Mensuration calculation total: {result:.2f}\r\n"
        
        # send the result to client
        clientsocket.send(message.encode('ascii'))
        clientsocket.close()


# ----------------- Main -----------------
if __name__ == "__main__":
    run_server()
