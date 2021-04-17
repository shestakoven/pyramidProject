import os


def main():
    """Create directory for saving captures."""
    if not os.path.isdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media')):
        try:
            os.mkdir(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media'))
        except OSError:
            'Fail to create media directory'
