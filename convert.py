from PIL import Image

im1 = Image.open('view1.png').convert('RGB')
im1.save('view1.jpg')