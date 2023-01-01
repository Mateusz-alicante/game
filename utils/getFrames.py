from PIL import Image, ImageSequence

def loadGIF(filename, pygame, scale=None):
    pilImage = Image.open(filename)
    frames = []
    for frame in ImageSequence.Iterator(pilImage):
        frame = frame.convert('RGBA')
        pygameImage = pygame.image.fromstring(
            frame.tobytes(), frame.size, frame.mode).convert_alpha()

        if scale:
            pygameImage = pygame.transform.scale(pygameImage, scale)

        frames.append(pygameImage)
    return frames