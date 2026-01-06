import math
import asyncio

# ---------------- Mensuration Calculations ---------------- #
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
    
    # Total sum of all measurements
    total = (
        area_circle + peri_circle + area_rect + peri_rect +
        area_square + peri_square + area_triangle +
        sa_cube + vol_cube + sa_cuboid + vol_cuboid +
        sa_cylinder + vol_cylinder
    )
    
    return total

# ---------------- Asyncio Math Functions ---------------- #
async def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print(f'Asyncio.Task: Compute factorial({i})')
        await asyncio.sleep(1)
        fact *= i
    print(f'Asyncio.Task - factorial({number}) = {fact}')

async def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print(f'Asyncio.Task: Compute fibonacci({i})')
        await asyncio.sleep(1)
        a, b = b, a + b
    print(f'Asyncio.Task - fibonacci({number}) = {a}')

async def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print(f'Asyncio.Task: Compute binomial_coefficient({i})')
        await asyncio.sleep(1)
    print(f'Asyncio.Task - binomial_coefficient({n}, {k}) = {result}')

# ---------------- Main Program ---------------- #
async def main():
    # Run mensuration calculations
    total_mensuration = mensuration_calculations()
    print(f"\nMensuration calculation total: {total_mensuration:.2f}\n")
    
    # Run math tasks concurrently
    await asyncio.gather(
        factorial(10),
        fibonacci(10),
        binomial_coefficient(20, 10)
    )

# Run the main async function
if __name__ == "__main__":
    asyncio.run(main())
