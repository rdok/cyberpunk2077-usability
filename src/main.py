import os
from argparse import ArgumentParser
from xml.etree import ElementTree
from xml.etree.ElementTree import SubElement

DIR_NAME = os.path.dirname(__file__)


def capitilize_message(value):
    return value.upper()


def main(args):
    filename = os.path.join(DIR_NAME, args.input_user_mappings_path)
    tree = ElementTree.parse(filename)

    y_axis_movement_el = tree.find('.//mapping[@name="LeftY_Axis"][@type="Axis"]')

    SubElement(
        y_axis_movement_el,
        'button',
        {'id': 'IK_CapsLock', 'val': '0', 'overridableUI': 'forward'}
    )

    tree.write(filename)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "-iump",
        "--input_user_mappings_path",
        dest="input_user_mappings_path",
        default='r6/config/inputUserMappings.xml'
    )
    args = parser.parse_args()

    main(args)
