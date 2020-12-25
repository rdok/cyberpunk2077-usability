from argparse import ArgumentParser
from unittest.mock import MagicMock, call

from src import main
from src.config import Config
from src.gui import GUI
from src.ioc import IOC

ioc = IOC()

argument_parser = MagicMock(spec=ArgumentParser)
ioc.set(ArgumentParser, argument_parser)

config = MagicMock(spec=Config)
ioc.set(Config, config)

ioc.instantiate_dependencies()

gui = MagicMock(spec=GUI)
ioc.set(GUI, gui)


def test_it_creates_the_gui():
    main.main(ioc)

    gui.mainloop.assert_called_once()


def test_it_loads_xml_files_path():
    main.configure_app(ioc)

    input_user_mappings_args_call = call(
        "-i",
        "--input_user_mappings_path",
        dest="input_user_mappings_path",
        default='r6/config/inputUserMappings.xml'
    )
    input_contexts_args_call = call(
        "-ic",
        "--input_contexts_path",
        dest="input_contexts_path",
        default='r6/config/inputContexts.xml'
    )
    argument_parser.add_argument.assert_has_calls([
        input_user_mappings_args_call, input_contexts_args_call
    ])

    args = argument_parser.parse_args.return_value
    config.set_input_user_mappings_path \
        .assert_called_once_with(args.input_user_mappings_path)

    config.set_input_contexts_path \
        .assert_called_once_with(args.input_contexts_path)


def test_it_creates_remap_walk_frame():
    gui.create_remap_walk_frame.assert_called_once()


def test_it_creates_crafting_speed_frame():
    gui.create_crafting_speed_frame.assert_called_once()
