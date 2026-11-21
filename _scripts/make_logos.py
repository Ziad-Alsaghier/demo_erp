import os
from PIL import Image, ImageOps, ImageDraw

os.makedirs('assets/images', exist_ok=True)
src_path = 'assets/temp_docx/word/media/543a124a8fb2e86168f5d148daef2d65e1792869.jpg'
orig = Image.open(src_path).convert('RGB')

# Find bounding box of logo
gray = ImageOps.invert(orig.convert('L'))
mask = gray.point(lambda p: 255 if p > 15 else 0)
bbox = mask.getbbox()

margin = 15
crop_box = (
    max(0, bbox[0] - margin),
    max(0, bbox[1] - margin),
    min(orig.width, bbox[2] + margin),
    min(orig.height, bbox[3] + margin)
)
cropped = orig.crop(crop_box)
w, h = cropped.size

# High-resolution alpha matting
orig_pixels = cropped.load()

# Create 1: Original logo with transparent background
logo_orig_trans = Image.new('RGBA', (w, h), (0, 0, 0, 0))
# Create 2: Dark-theme optimized logo (where dark navy is converted to crisp luminous white)
logo_dark_trans = Image.new('RGBA', (w, h), (0, 0, 0, 0))

draw_orig = logo_orig_trans.load()
draw_dark = logo_dark_trans.load()

for y in range(h):
    for x in range(w):
        r, g, b = orig_pixels[x, y]
        whiteness = min(r, g, b)
        
        if whiteness >= 250:
            a = 0
        elif whiteness <= 210:
            a = 255
        else:
            a = int((250 - whiteness) / 40.0 * 255)

        if a == 0:
            continue

        factor = a / 255.0
        # Defringe white edge
        ur = min(255, max(0, int((r - (1 - factor) * 255) / max(factor, 0.01))))
        ug = min(255, max(0, int((g - (1 - factor) * 255) / max(factor, 0.01))))
        ub = min(255, max(0, int((b - (1 - factor) * 255) / max(factor, 0.01))))

        draw_orig[x, y] = (ur, ug, ub, a)

        # Dark theme color mapping:
        # Check if this pixel is part of the cyan/blue gradient or the navy text
        # Cyan has significant blue and green, and ub > ur + 30
        is_cyan = (ub > 140 and ug > 90 and (ub - ur > 30))
        
        if is_cyan:
            # Keep vibrant electric cyan/blue
            draw_dark[x, y] = (ur, ug, ub, a)
        else:
            # Navy letters ('ISE' and 'DISTRIBUTION') -> transform to crisp white (#FFFFFF)
            draw_dark[x, y] = (245, 250, 255, a)

# Save the logos
logo_orig_trans.save('assets/images/wise-logo-original.png', 'PNG')
logo_orig_trans.save('assets/images/wise-logo-light.png', 'PNG')
logo_dark_trans.save('assets/images/wise-logo-dark.png', 'PNG')
# Set wise-logo.png as dark variant because default theme is dark
logo_dark_trans.save('assets/images/wise-logo.png', 'PNG')

print("Saved wise-logo.png, wise-logo-dark.png, wise-logo-light.png")

# Also create a Badge / Container version (Original logo on clean frosted glass pill)
badge_h = 76
scale = (badge_h - 16) / h
badge_w = int(w * scale) + 24
badge = Image.new('RGBA', (badge_w, badge_h), (0, 0, 0, 0))
d = ImageDraw.Draw(badge)
d.rounded_rectangle([0, 0, badge_w, badge_h], radius=16, fill=(255, 255, 255, 245), outline=(148, 204, 255, 100), width=1)
scaled_orig = logo_orig_trans.resize((int(w * scale), int(h * scale)), Image.Resampling.LANCZOS)
badge.paste(scaled_orig, (12, 8), scaled_orig)
badge.save('assets/images/wise-logo-pill.png', 'PNG')

# Create standalone square icon (The "W" with swoosh)
# Crop the "W" and swoosh alone
crop_w_box = (
    max(0, bbox[0] - 10),
    max(0, bbox[1] - 10),
    int(orig.width * 0.58), # Just past the swoosh tip
    min(orig.height, bbox[3] + 10)
)
w_cropped = orig.crop(crop_w_box)
w_w, w_h = w_cropped.size
w_pixels = w_cropped.load()

w_icon_img = Image.new('RGBA', (w_w, w_h), (0, 0, 0, 0))
draw_icon = w_icon_img.load()

for y in range(w_h):
    for x in range(w_w):
        r, g, b = w_pixels[x, y]
        whiteness = min(r, g, b)
        if whiteness >= 245:
            continue
        elif whiteness <= 210:
            a = 255
        else:
            a = int((245 - whiteness) / 35.0 * 255)

        factor = a / 255.0
        ur = min(255, max(0, int((r - (1 - factor) * 255) / max(factor, 0.01))))
        ug = min(255, max(0, int((g - (1 - factor) * 255) / max(factor, 0.01))))
        ub = min(255, max(0, int((b - (1 - factor) * 255) / max(factor, 0.01))))

        # Only keep the cyan/blue parts of W and swoosh
        is_cyan = (ub > 130 and ug > 80 and (ub - ur > 25))
        if is_cyan:
            draw_icon[x, y] = (ur, ug, ub, a)

bbox_w_icon = w_icon_img.getbbox()
if bbox_w_icon:
    w_icon_img = w_icon_img.crop(bbox_w_icon)

# Create 512x512 square icon
icon_512 = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
scale_w = min(420 / w_icon_img.width, 420 / w_icon_img.height)
nw = int(w_icon_img.width * scale_w)
nh = int(w_icon_img.height * scale_w)
w_scaled = w_icon_img.resize((nw, nh), Image.Resampling.LANCZOS)
icon_512.paste(w_scaled, ((512 - nw) // 2, (512 - nh) // 2), w_scaled)
icon_512.save('assets/images/wise-logo-icon.png', 'PNG')

# Also create a squircle app icon for avatar and favicon
app_icon = Image.new('RGBA', (512, 512), (0, 0, 0, 0))
d_app = ImageDraw.Draw(app_icon)
d_app.rounded_rectangle([16, 16, 496, 496], radius=110, fill=(10, 32, 56, 255), outline=(118, 209, 255, 120), width=6)
app_icon.paste(w_scaled, ((512 - nw) // 2, (512 - nh) // 2), w_scaled)
app_icon.save('assets/images/wise-app-icon.png', 'PNG')

# Favicon
app_icon.resize((32, 32), Image.Resampling.LANCZOS).save('assets/images/favicon.png', 'PNG')
app_icon.resize((32, 32), Image.Resampling.LANCZOS).save('assets/images/favicon.ico', 'ICO')

# Also copy to Laragon public directory if present
laragon_public = r'C:\laragon\www\wise\public\images'
if os.path.exists(r'C:\laragon\www\wise\public'):
    os.makedirs(laragon_public, exist_ok=True)
    logo_dark_trans.save(os.path.join(laragon_public, 'wise-logo.png'), 'PNG')
    logo_dark_trans.save(os.path.join(laragon_public, 'wise-logo-dark.png'), 'PNG')
    logo_orig_trans.save(os.path.join(laragon_public, 'wise-logo-light.png'), 'PNG')
    icon_512.save(os.path.join(laragon_public, 'wise-logo-icon.png'), 'PNG')
    app_icon.resize((32, 32), Image.Resampling.LANCZOS).save(r'C:\laragon\www\wise\public\favicon.ico', 'ICO')
    print("Copied optimized logos to C:\\laragon\\www\\wise\\public\\images")

print("All logo optimizations completed successfully!")
