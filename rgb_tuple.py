import random

def color_generator():
    color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    return color

def main():
    print(color_generator())
    print(color_generator())
    print(color_generator())

main()