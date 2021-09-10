def image_gen(count):

    from typing import Sized
    from PIL import Image, ImageDraw, ImageFont
    # from main import count
    W = 1145
    H = 487
    count = str(count)
    img = Image.open('assets/images/template.png')
    if int(count) == 1:
        img_text = count + " day"
    else: 
        img_text = count+" days"
    
    draw = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('assets/fonts/Spiderman-Homecoming.otf', 200)
    
    w, h = draw.textsize(img_text , font = fnt)
    
    draw.text(((W-w)/2,(H-h)/2), img_text, fill="white" ,font=fnt)
      
    # img.show()
    img.save('assets/images/'+count+'days.png')


