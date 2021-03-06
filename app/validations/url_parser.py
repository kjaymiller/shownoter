import re


def get_potential_link(content):
    """ Parses through content
    returns a list of  all "weak matches" of registry."""

    weak_re_match = re.compile(r'\S+\.\S+')

    results = re.findall(weak_re_match, content)
    return results


def image_detect(url):
    """Determines if the url is an image. """
    image_extension = ['.jpg', '.png', '.jpeg', '.gif']
    extension = re.search(r'\.[a-zA-Z]{2,}$', url, re.M)

    if extension is None:
        return False

    if extension.group(0) in image_extension:
        return True
