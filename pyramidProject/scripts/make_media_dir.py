import os


def create_dir():
    """Create directory for saving captures."""
    if not os.path.isdir(os.path.join('..', 'media')):
        try:
            os.mkdir('../media')
        except OSError:
            'Fail to create media directory'
