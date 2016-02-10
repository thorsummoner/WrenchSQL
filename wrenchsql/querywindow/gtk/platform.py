
class Platform(object):
    pass

class Debian(Platform):
    # Ubuntu/Debian/Mint
    libgtksourceview3 = '/usr/lib/x86_64-linux-gnu/libgtksourceview-3.0.so.1'

    apt_requirements = [
        'libgtksourceview-3.0-1:amd64'
    ]

class LinuxMint(Debian):
    pass

