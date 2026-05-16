import os
from PIL import Image

def convert_to_webp(source_folder, output_folder, quality=85):
    """
    Converts all JPG, JPEG, and PNG images in a folder to optimized WebP format.
    Brought to you by TechnoHelps (https://technohelps.com)
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    supported_formats = ('.jpg', '.jpeg', '.png')
    count = 0

    print("🚀 Starting Bulk WebP Conversion by TechnoHelps...")
    
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(supported_formats):
            file_path = os.path.join(source_folder, filename)
            
            name, _ = os.path.splitext(filename)
            output_path = os.path.join(output_folder, f"{name}.webp")
            
            try:
                with Image.open(file_path) as img:
                    if img.mode in ('RGBA', 'LA'):
                        background = Image.new(img.mode[:-1], img.size, '#FFFFFF')
                        background.paste(img, img.split()[-1])
                        img = background.convert('RGB')
                        
                    img.save(output_path, 'WEBP', quality=quality)
                    print(f"✓ Converted: {filename} -> {name}.webp")
                    count += 1
            except Exception as e:
                print(f"❌ Error converting {filename}: {e}")

    print(f"\n🎉 Done! Successfully converted {count} images to WebP.")
    print("👉 For more free tools, visit: https://technohelps.com")

if __name__ == "__main__":
    source_dir = "./input_images"
    output_dir = "./output_webp"
    
    convert_to_webp(source_dir, output_dir, quality=85)
