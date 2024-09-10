from PIL import Image, ImageDraw

def draw_dog():
    # Create a blank image with white background
    width, height = 200, 200
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Draw a simple representation of a dog
    # Draw the body
    draw.ellipse((50, 100, 150, 180), fill='yellow')

    # Draw the head
    draw.ellipse((80, 50, 120, 100), fill='yellow')

    # Draw the eyes
    draw.ellipse((90, 60, 95, 65), fill='blue')
    draw.ellipse((105, 60, 110, 65), fill='blue')
    
    draw.ellipse((90, 60, 95, 65), fill='black')
    draw.ellipse((105, 60, 110, 65), fill='black')

    # Draw the nose
    #draw.ellipse((95, 75, 105, 85), fill='purple')
    draw.ellipse((97, 72, 103, 78), fill='black')#nose
    draw.line((105, 85, 95, 85), fill='black', width=2)#mouth

    # Draw the ears
    #draw.polygon([(70, 60), (80, 50), (85, 70)], fill='yellow')
    draw.ellipse((80, 35, 90, 60), fill='yellow')#left ear
    
    #draw.polygon([(130, 60), (120, 50), (115, 70)], fill='yellow')
    draw.ellipse((110, 35, 120, 60), fill='yellow')#right ear

    # Draw the tail
    #draw.line((150, 130, 180, 110), fill='brown', width=500)

    # Draw the legs
    draw.line((70, 170, 70, 200), fill='yellow', width=5)
    draw.line((130, 170, 130, 200), fill='yellow', width=5)

    # Save the image
    image.save('dog.png')

draw_dog()

