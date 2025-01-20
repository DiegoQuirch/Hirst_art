#import colorgram
import colorgram

# Extract 12 colors from an image.
colors = colorgram.extract('C:/Diego/Python/Projects/code projects/Hirst Art/hirst_paint.jpg', 12)
colors_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors_list.append((r, g, b))
    
print(colors_list)