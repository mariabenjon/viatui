from PIL import Image
import pytesseract

def find_text_coordinates(image_path, target_text):
    # Open the image file
    img = Image.open(image_path)

    # Use pytesseract to do OCR on the image
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)

    # Iterate over each text instance in the image
    for i in range(len(data['text'])):
        if target_text in data['text'][i]:
            # Extract coordinates
            x = data['left'][i]
            y = data['top'][i]
            return (x, y)

    return None

## Example usage
#image_path = 'chromium-nix-screenshots/posh-8.png'
#target_text = 'Followers'
#(x, y) = find_text_coordinates(image_path, target_text)
#
#if (x, y):
#    print(f"Coordinates of '{target_text}': {x} {y}")
#else:
#    print(f"'{target_text}' not found in the image.")
#