from PIL import Image


class PictureToAscii:

    def __init__(self, image_path):
            self.image_path = image_path

            try:
                # Check if the file exists
                self.image = Image.open(self.image_path).convert('L')
                print("Photo loaded succesfully!")
            except FileNotFoundError:
                print("File not found!")

            self.convertToAscii()

    def convertToAscii(self):

        width, height = self.image.size
        proportion = width/height
        width, height = 100, int(100/proportion)
        # Keep the new image to the same proportions as the original
        newImage = self.image.resize((width, height))

        pictureData = [[i for i in range(0,width)] for j in range(0, height)]
        print(list(newImage.getdata()))


convertor = PictureToAscii("eu.jpg")
