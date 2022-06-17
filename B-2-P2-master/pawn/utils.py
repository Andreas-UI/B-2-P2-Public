from markdown import markdown
from PIL import Image
from .settings import (
    PAWN_MARKDOWN_EXTENSIONS, 
    PAWN_MARKDOWN_EXTENSION_CONFIGS
)
def markdownify(content):

    extensions = PAWN_MARKDOWN_EXTENSIONS
    extension_configs = PAWN_MARKDOWN_EXTENSION_CONFIGS

    md = markdown(text=content, extensions=extensions, extension_configs=extension_configs)
    return md

def _crop(im, target_x, target_y):

    # Use integer values now.
    source_x, source_y = im.size
    # Difference between new image size and requested size.
    diff_x = int(source_x - min(source_x, target_x))
    diff_y = int(source_y - min(source_y, target_y))

    if diff_x or diff_y:
        # Center cropping (default).
        halfdiff_x, halfdiff_y = diff_x // 2, diff_y // 2
        box = [
            halfdiff_x,
            halfdiff_y,
            min(source_x, int(target_x) + halfdiff_x),
            min(source_y, int(target_y) + halfdiff_y)
        ]

        # Finally, crop the image!
        im = im.crop(box)
    return im


def _scale(im, x, y):

    im = im.resize(
        (int(x), int(y)),
        resample=Image.ANTIALIAS
    )
    return im


def scale_and_crop(image, size, crop=False, upscale=False, quality=None):

    # Open image and store format/metadata.
    image.open()
    im = Image.open(image)
    im_format, im_info = im.format, im.info
    if quality:
        im_info['quality'] = quality

    # Force PIL to load image data.
    im.load()

    source_x, source_y = map(float, im.size)
    target_x, target_y = map(float, size)

    if crop or not target_x or not target_y:
        scale = max(target_x / source_x, target_y / source_y)
    else:
        scale = min(target_x / source_x, target_y / source_y)

    # Handle one-dimensional targets.
    if not target_x:
        target_x = source_x * scale
    elif not target_y:
        target_y = source_y * scale

    if scale < 1.0 or (scale > 1.0 and upscale):
        im = _scale(im=im, x=source_x * scale, y=source_y * scale)

    if crop:
        im = _crop(im=im, target_x=target_x, target_y=target_y)

    # Close image and replace format/metadata, as PIL blows this away.
    im.format, im.info = im_format, im_info

    image.close()

    return im


def xml_has_javascript(data):

    from re import search, IGNORECASE, MULTILINE

    data = str(data, encoding='UTF-8')
    # ------------------------------------------------
    # Handles JavaScript nodes and stringified nodes.
    # ------------------------------------------------
    # Filters against "script" / "if" / "for" within node attributes.
    pattern = r'(<\s*\bscript\b.*>.*)|(.*\bif\b\s*\(.?={2,3}.*\))|(.*\bfor\b\s*\(.*\))'

    found = search(
        pattern=pattern,
        string=data,
        flags=IGNORECASE | MULTILINE
    )

    if found is not None:
        return True

    # ------------------------------------------------
    # Handles JavaScript injection into attributes
    # for element creation.
    # ------------------------------------------------
    from xml.etree.ElementTree import fromstring

    parsed_xml = (
        (attribute, value)
        for elm in fromstring(data).iter()
        for attribute, value in elm.attrib.items()
    )

    for key, val in parsed_xml:
        if '"' in val or "'" in val:
            return True

    # It is (hopefully) safe.
    return False