import colorgram

colors = colorgram.extract('img.jpg',30)
rgb_color = []

for color in colors:
     a = color.rgb
     red = a[0]
     green = a[1]
     blue = a[2]
     color_tuple = (red, green, blue)
     rgb_color.append(color_tuple)

