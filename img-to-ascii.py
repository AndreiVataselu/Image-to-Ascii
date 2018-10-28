from PIL import Image


class PictureToAscii:

    def __init__(self, image_path):
        self.image_path = image_path
        
        self.characters = '!%&@0$+B?=4*1QT;{X<"Fejs#Yc.|~Znk'

        try:
            # Check if the file exists
            self.image = Image.open(self.image_path).convert('L')
            self.convert_to_ascii()
            print("Photo converted successfully!")
        except FileNotFoundError:
            print("File not found!")

    def convert_to_ascii(self):

        width, height = self.image.size
        proportion = width / height
        width, height = 100, int(100 / proportion)
        # Keep the new image to the same proportions as the original
        new_image = self.image.resize((width, height))
        data = list(new_image.getdata())  # Get picture's grey scales pixels

        # Turn the 1D array of pixels into a 2D array so we can replace the pixels with ASCII chars
        # thus creating the ASCII art
        picture_data = [[data.pop(0) for i in range(width)] for j in range(height)]

        with open("picture.txt", "w") as art:
            for arr in picture_data:
                for item in arr:
                    # We divide the 256 pixels into 32 ranges of 8 pixels each
                    art.write("{0}".format(self.characters[int(item / 8)]))
                art.write("\n")


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("imagepath", help="Path of the image you want to use", type=str)
    args = parser.parse_args()
    photo_path = args.imagepath
    convertor = PictureToAscii(photo_path)
