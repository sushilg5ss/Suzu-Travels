#!/usr/bin/env python3
"""Build watermarked web copies of Suzu Travels' ISO 9001:2015 certificates.

Inputs (same folder): mqa-raw.png (MQA 2026 PDF rendered at 220 dpi), icv-photo.jpg (framed ICV 2022 photo)
Outputs: suzu-travels-iso-9001-2015-certificate-mqa-2026.webp
         suzu-travels-iso-9001-2015-certificate-icv-2022-previous.webp
Style matches the existing /certificates/ images: diagonal grey watermark + dark green credit strip.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
STRIP = "Published by Suzu Travels for verification only  ·  suzutravels.com/certificates/  ·  +91 70874 88961"


def persp_coeffs(src, dst):
    # maps output (dst) coords -> input (src) coords, as PIL expects
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return np.linalg.solve(np.array(A, float), np.array(B, float)).tolist()


def watermark(im, extra=None):
    W, H = im.size
    base = im.convert("RGBA")
    layer = Image.new("RGBA", (W * 2, H * 2), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    fs = max(26, W // 30)
    font = ImageFont.truetype(F, fs)
    txt = "suzutravels.com  ·  for verification only  ·  "
    step_y = int(fs * 5.2)
    for row, y in enumerate(range(0, H * 2, step_y)):
        x0 = -(row * fs * 4) % (fs * 20)
        d.text((x0 - fs * 20, y), txt * 8, font=font, fill=(110, 110, 110, 46))
    layer = layer.rotate(24, resample=Image.BICUBIC, center=(W, H))
    layer = layer.crop((W // 2, H // 2, W // 2 + W, H // 2 + H))
    out = Image.alpha_composite(base, layer)

    sh = max(46, W // 26)
    canvas = Image.new("RGB", (W, H + sh), (18, 38, 21))
    canvas.paste(out.convert("RGB"), (0, 0))
    d = ImageDraw.Draw(canvas)
    sf = ImageFont.truetype(FB, max(15, int(sh * 0.36)))
    label = STRIP if extra is None else extra + "  ·  " + STRIP
    while d.textlength(label, font=sf) > W - 40 and sf.size > 11:
        sf = ImageFont.truetype(FB, sf.size - 1)
    tw = d.textlength(label, font=sf)
    d.text(((W - tw) / 2, H + (sh - sf.size) / 2 - 2), label, font=sf, fill=(212, 175, 55))
    return canvas


# 1) MQA 2026 (current) — clean render of the PDF
mqa = Image.open("mqa-raw.png").convert("RGB")
mqa = mqa.resize((1300, round(mqa.height * 1300 / mqa.width)), Image.LANCZOS)
watermark(mqa).save("suzu-travels-iso-9001-2015-certificate-mqa-2026.webp", "WEBP", quality=82, method=6)

# 2) ICV 2022 (previous) — straighten the framed photo
ph = Image.open("icv-photo.jpg").convert("RGB")
src = [(116, 144), (1444, 124), (1504, 2256), (44, 2240)]  # TL, TR, BR, BL of the paper
OW, OH = 1300, 2020
dst = [(0, 0), (OW, 0), (OW, OH), (0, OH)]
flat = ph.transform((OW, OH), Image.PERSPECTIVE, persp_coeffs(src, dst), Image.BICUBIC)
flat = ImageEnhance.Contrast(flat).enhance(1.06)
flat = ImageEnhance.Brightness(flat).enhance(1.04)
watermark(flat, extra="Previous certificate, expired 24-03-2025").save(
    "suzu-travels-iso-9001-2015-certificate-icv-2022-previous.webp", "WEBP", quality=80, method=6)
print("ok")
