from PIL import Image, ImageDraw
import sys
import os
from .mappings import MAPPINGS as MAP


def build_card(command: str = "Example Command", out_file="out_card.png"):
    if len(command) > 72:
        raise Exception("Command too long")
    # Template image taken from Columbia University
    # http://www.columbia.edu/cu/computinghistory/karlsruhe-card.jpg
    # im = Image.open('PyPunch/template_card.jpg').copy()
    im = Image.open(os.path.join(os.path.dirname(__file__), 'template_card.jpg')).copy()
    draw = ImageDraw.Draw(im)
    counter = 0
    for c in command:
        if c != ' ':
            draw_punch(draw, counter, c)
        counter += 1
    im.save(out_file)


def draw_punch(draw: ImageDraw, col: int, c: chr):
    row_offset = 51
    col_offset = 17.4

    for cell in MAP[c.upper()]:
        row_start = 38 + (cell * row_offset)
        col_start = 38 + (col * col_offset)
        _draw_punch(draw, row_start=row_start, col_start=col_start)


def _draw_punch(draw: ImageDraw, col_start, row_start):
    punch_height = 19
    punch_width = 10
    punch_color = (0, 0, 0)

    col_end = col_start + punch_width
    row_end = row_start + punch_height

    draw.rectangle([col_start, row_start, col_end, row_end], fill=punch_color)


if __name__ == '__main__':
    args = sys.argv
    args.remove(sys.argv[0])
    while len(args):
        build_card(sys.argv.pop())
    build_card("test")
