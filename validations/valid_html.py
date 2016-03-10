import re


def detect_href(a_tag):
    """checks tag for a record"""
    if re.search(r'<a.+</a>', a_tag):
        return True

    else:
        return False


def detect_img(img_tag):
    if re.search(r'<img.+>', img_tag):
        return True

    else:
        return False


def detect_href_url(a_tag):
    url = re.search(r"""href=["'](?P<url>\S+)["']""", a_tag)
    return url.group('url') if url else None


def detect_href_title(a_tag):
    title = re.search(r'<a.+>(?P<title>.*)</a>', a_tag)
    return title.group('title') if title else None


def detect_img_url(img_tag):
    url = re.search(r"""src=["'](?P<url>\S+)["']""", img_tag)
    return url.group('url') if url else None


def detect_img_title(img_tag):
    title = re.search(r"""alt=["'](?P<title>.+)["']""", img_tag)
    return title.group('title') if title else None


def render_href_link(a_tag):
    if detect_href(a_tag):
        url = detect_href_url(a_tag)
        title = detect_href_title(a_tag)

        if url:
            return {
                'url': url,
                'title': title
                }
    else:
        return None


def render_image_link(img):
    if detect_img(img):
        url = detect_img_url(img)
        title = detect_img_title(img)

    if url:
        return {
            'url': url,
            'title': title
        }
