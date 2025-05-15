import B
import C


def show_name():
    print(__name__)


if __name__ == '__main__':
    show_name()
    B.show_name()
    C.show_name()
