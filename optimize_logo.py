import os
from PIL import Image, ImageOps, ImageFilter

orig = Image.open('assets/temp_docx/word/media/543a124a8fb2e86168f5d148daef2d65e1792869.jpg').convert('RGB')
gray = ImageOps.invert(orig.convert('L'))
mask = gray.point(lambda p: 255 if p > 15 else 0)
bbox = mask.getbbox()

margin = 20
crop_box = (
    max(0, bbox[0] - margin),
    max(0, bbox[1] - margin),
    min(orig.width, bbox[2] + margin),
    min(orig.height, bbox[3] + margin)
)
cropped = orig.crop(crop_box)
w, h = cropped.size

# High-quality alpha matting for light version
light_img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
dark_img = Image.new('RGBA', (w, h), (0, 0, 0, 0))

pixels = list(cropped.getdata())
light_data = []
dark_data = []

for idx, (r, g, b) in enumerate(pixels):
    whiteness = min(r, g, b)
    if whiteness >= 250:
        a = 0
    elif whiteness <= 210:
        a = 255
    else:
        a = int((250 - whiteness) / 40.0 * 255)

    if a == 0:
        light_data.append((0, 0, 0, 0))
        dark_data.append((0, 0, 0, 0))
        continue

    # Defringe
    factor = a / 255.0
    ur = min(255, max(0, int((r - (1 - factor) * 255) / max(factor, 0.01))))
    ug = min(255, max(0, int((g - (1 - factor) * 255) / max(factor, 0.01))))
    ub = min(255, max(0, int((b - (1 - factor) * 255) / max(factor, 0.01))))

    light_data.append((ur, ug, ub, a))

    # For dark version:
    # Notice: The cyan elements have (b > 160 and g > 110 and r < 140)
    # The navy elements have (r < 75 and g < 75 and b < 115)
    # The middle bar of E has cyan (b > 180 and g > 130)
    is_cyan = (ub > 140 and ug > 90 and (ub - ur > 40))
    
    if is_cyan:
        # Keep radiant cyan / sky blue
        dark_data.append((ur, ug, ub, a))
    else:
        # It's the navy part (letters I, S, parts of E, and DISTRIBUTION text)
        # Turn it into pure, crisp, solid white with subtle cool blue tint (#F0F7FF)
        # Alpha preserves the exact anti-aliased edge
        dark_data.append((240, 248, 255, a))

light_img.putdata(light_data)
dark_img.putdata(dark_data)

light_img.save('assets/images/wise-logo-light.png', 'PNG')
dark_img.save('assets/images/wise-logo-dark.png', 'PNG')
dark_img.save('assets/images/wise-logo.png', 'PNG')
print("Successfully generated wise-logo-light.png and wise-logo-dark.png")

# Now let's create a badge version:
# Dark logo on an elegant subtle glass container
badge_w = w + 60
badge_h = h + 40
badge = Image.new('RGBA', (badge_w, badge_h), (0, 0, 0, 0))
# Create rounded rectangle mask
from PIL import ImageDraw
draw = ImageDraw.Draw(badge)
draw.rounded_rectangle([0, 0, badge_w, badge_h], radius=24, fill=(10, 32, 56, 210), outline=(148, 204, 255, 60), width=2)
# Paste dark_img in center
badge.paste(dark_img, (30, 20), dark_img)
badge.save('assets/images/wise-logo-badge.png', 'PNG')
print("Successfully generated wise-logo-badge.png")

# Create standalone Icon (just the W and swoosh)
# The W and swoosh end around x=740 in orig, let's find exact coordinates
orig_w_crop = orig.crop((230, 220, 930, 620))
orig_w_pixels = list(orig_w_crop.getdata())
icon_w_data = []

for r, g, b in orig_w_pixels:
    whiteness = min(r, g, b)
    if whiteness >= 250:
        a = 0
    elif whiteness <= 210:
        a = 255
    else:
        a = int((250 - whiteness) / 40.0 * 255)

    if a == 0:
        icon_w_data.append((0, 0, 0, 0))
        continue

    factor = a / 255.0
    ur = min(255, max(0, int((r - (1 - factor) * 255) / max(factor, 0.01))))
    ug = min(255, max(0, int((g - (1 - factor) * 255) / max(factor, 0.01))))
    ub = min(255, max(0, int((b - (1 - factor) * 255) / max(factor, 0.01))))

    # In icon, only include the cyan "W" and swoosh (not the navy "I")
    is_cyan = (ub > 130 and ug > 80 and (ub - ur > 30))
    if is_cyan:
        icon_w_data.append((ur, ug, ub, a))
    else:
        # Skip the navy "I" and "DISTRIBUTION" in the standalone icon!
        icon_w_data.append((0, 0, 0, 0))

icon_raw = Image.new('RGBA', orig_w_crop.size, (0, 0, 0, 0))
icon_raw.putdata(icon_w_data)
bbox_icon = icon_raw.getbbox()
if bbox_icon:
    icon_raw = icon_raw.crop(bbox_icon)

# Create 512x512 icon
icon_512 = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
sc = min(420 / icon_raw.width, 420 / icon_raw.height)
iw = int(icon_raw.width * sc)
ih = int(icon_raw.height * sc)
icon_resized = icon_raw.resize((iw, ih), Image.Resampling.LANCZOS)
icon_512.paste(icon_resized, ((512 - iw) // 2, (512 - ih) // 2), icon_resized)
icon_512.save('assets/images/wise-logo-icon.png', 'PNG')

# Create Icon with rounded squircle background (App Icon)
app_icon = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
draw_app = ImageDraw.Draw(app_icon)
draw_app.rounded_rectangle([16, 16, 496, 496], radius=110, fill=(10, 32, 56, 255), outline=(118, 209, 255, 120), width=6)
# Paste icon
app_icon.paste(icon_resized, ((512 - iw) // 2, (512 - ih) // 2), icon_resized)
app_icon.save('assets/images/wise-app-icon.png', 'PNG')

# Favicons
app_icon.resize((64, 64), Image.Resampling.LANCZOS).save('assets/images/favicon.png', 'PNG')
app_icon.resize((32, 32), Image.Resampling.LANCZOS).save('assets/images/favicon.ico', 'ICO')
print("Successfully generated wise-logo-icon.png, wise-app-icon.png, favicon.png, favicon.ico")
