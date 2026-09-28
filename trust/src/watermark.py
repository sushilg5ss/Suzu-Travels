from PIL import Image, ImageDraw, ImageFont
import math, sys
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def watermark(src, dst, width, text='suzutravels.com  ·  for verification only'):
    im = Image.open(src).convert('RGB')
    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    W, H = im.size
    fs = max(22, W // 44)
    font = ImageFont.truetype(FONT, fs)
    # build one big transparent layer, draw rows of text, rotate
    diag = int(math.hypot(W, H)) + 200
    layer = Image.new('RGBA', (diag, diag), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    tw = d.textlength(text, font=font)
    gap_x, gap_y = int(tw * 0.55), int(fs * 7.5)
    y, row = 0, 0
    while y < diag:
        x = -((row % 2) * (tw + gap_x) // 2)
        while x < diag:
            d.text((x, y), text, font=font, fill=(18, 38, 21, 24))
            x += tw + gap_x
        y += gap_y; row += 1
    layer = layer.rotate(28, resample=Image.BICUBIC)
    ox, oy = (diag - W) // 2, (diag - H) // 2
    layer = layer.crop((ox, oy, ox + W, oy + H))
    out = Image.alpha_composite(im.convert('RGBA'), layer).convert('RGB')
    # thin footer credit strip
    strip_h = max(36, W // 38)
    canvas = Image.new('RGB', (W, H + strip_h), (18, 38, 21))
    canvas.paste(out, (0, 0))
    d2 = ImageDraw.Draw(canvas)
    f2 = ImageFont.truetype(FONT, max(14, W // 82))
    cap = 'Published by Suzu Travels for verification only  ·  suzutravels.com/certificates/  ·  +91 70874 88961'
    cw = d2.textlength(cap, font=f2)
    d2.text(((W - cw) / 2, H + (strip_h - f2.size) / 2 - 2), cap, font=f2, fill=(212, 175, 55))
    canvas.save(dst, 'WEBP', quality=82, method=6)
    print(dst, canvas.size)
watermark('hpt200-1.png', 'suzu-travels-hp-tourism-registration-certificate.webp', 1800)
watermark('gst200-1.png', 'suzu-travels-gst-registration-certificate.webp', 1300)
