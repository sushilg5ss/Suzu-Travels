#!/usr/bin/env python3
"""Watermarked web copy of Suzu Travels' NIDHI pledge certificate (Ministry of Tourism), same style as /certificates/."""
import sys; sys.path.insert(0, '/home/claude/iso')
from PIL import Image
import importlib.util
spec = importlib.util.spec_from_file_location('b', '/home/claude/iso/build_iso.py')
src = open('/home/claude/iso/build_iso.py').read().split('# 1) MQA')[0]
ns = {}; exec(src, ns)
im = Image.open('page-1.png').convert('RGB')
im = im.crop((60, 50, 1640, 2150))
im = im.resize((1300, round(im.height * 1300 / im.width)), Image.LANCZOS)
ns['watermark'](im).save('suzu-travels-nidhi-pledge-certificate-ministry-of-tourism.webp', 'WEBP', quality=82, method=6)
print('ok')
