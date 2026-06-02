# Text Recognition using OCR

import cv2
import pytesseract

# Path of image
image_path = "sample.jpg"

# Read image
img = cv2.imread(image_path)

# Check image loaded or not
if img is None:
    print("Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Remove noise using Gaussian Blur
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Extract text from image
text = pytesseract.image_to_string(gray)

# Display extracted text
print("Detected Text:")
print("")
print(text)

# Show image
cv2.imshow("Input Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()