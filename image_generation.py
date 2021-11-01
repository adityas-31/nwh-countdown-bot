def image_gen(count , template):

    from typing import Sized
    from PIL import Image, ImageDraw, ImageFont
    import random
    
    # from main import count
    if template == 'assets/images/template.png':
        W = 1145
        H = 487
        fnt = ImageFont.truetype('assets/fonts/Spiderman-Homecoming.otf', 200)
        col = 'white' 
    elif template == 'assets/images/template2.png':
        W = 1087
        H = 610
        fnt = ImageFont.truetype('assets/fonts/Amazing Spider Man.ttf', 200)
        col = 0xc0c0c0
    elif template == 'assets/images/template3.png':
        W = 1222
        H = 602
        fnt = ImageFont.truetype('assets/fonts/homoarakhn.regular.ttf', 200)
        col = 0xc0c0c0


    count = str(count)
    img = Image.open(template)
    if int(count) == 1:
        
        if template == 'assets/images/template3.png' :
            img_text = count + "day"
        else:
            img_text = count + " day"

    elif int(count) == 0:
        img_text = 'TODAY!'
        
    else: 
        if template == 'assets/images/template3.png' :
            img_text = count+"days"
        else: 
            img_text = count + " days"
    
    draw = ImageDraw.Draw(img)
    
    w, h = draw.textsize(img_text , font = fnt)
    
    draw.text(((W-w)/2,(H-h)/2), img_text, fill=col ,font=fnt)
      
    
    img.save('assets/images/'+count+'days.png')
    


