import os
import pytesseract

try:
    import Image
except ImportError:
    from PIL import Image
    
def main():
    pass

if __name__ == '__main__':
    main()
    image = os.path.abspath(r'../test/data/test_image.jpg')
    print(image)
    print(os.path.isfile(image))