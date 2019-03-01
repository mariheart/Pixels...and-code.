
def setup():
    global img
    size (782, 1054) # MAKE SURE THIS IS EQUAL TO THE IMAGE'S SIZE!!!!!!!!!!
    # Let's load the image.
    img = loadImage("park.png")


def draw():
    loadPixels()
    img.loadPixels()
    for y in xrange(height):
        for x in xrange(width):
            loc = x + y*width
            
            #Red, green, blue.
            
            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
            a = alpha(img.pixels[loc])
            
            # Here we would change RGB values.
            
            if r < 100: # Condition 1 - Sin City-ish..
                r = 255
                g = 255
                b = 255
            
            elif b > 100:
                r = 0
                g = 0
                b = 0
                
            else: # Whatever pixel has not been affected by the above is now red.
                r = 255
                g = 0
                b = 0

            if 100 < r < 200: # Condition 2 - Middle flavor switcheroo
                temp = r
                g = temp
            
            elif 100 < g < 200:
                temp = g
                b = temp
            
            elif 100 < b < 200:
                temp = b
                r = temp
            
            # This just switches the color if their values are in the middle.
            
            if r >= 127 and g >= 127 and b >= 127: # Condition 3 - Reverse shadings and opacities
                r = 255
                g = 255
                b = 255
            
            elif r < 127 and g < 127 and b < 127:
                r = 0
                g = 0
                b = 0
            
            else:
                a = 127 
            
            #I just now realized that this is NOT reverse shading.
            #That honor goes to Sin City-ish.
            #This just makes everything either black, white, or half-transparent.
            
            pixels[loc] = color(r,g,b,a)
    
    updatePixels()
    
    save() # Saves the pic
    
    
