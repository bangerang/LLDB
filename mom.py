

import lldb
import os
import shlex
import optparse

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand(
    'command script add -f mom.handle_command mom')

def handle_command(debugger, command, result, internal_dict):
    '''
    Documentation for how to use mom goes here
    '''

    command_args = shlex.split(command, posix=False)
    parser = generateOptionParser()
    try:
        (options, args) = parser.parse_args(command_args)
    except:
        result.SetError(parser.usage)
        return

    # Uncomment if you are expecting at least one argument
    # clean_command = shlex.split(args[0])[0]
    target = debugger.GetSelectedTarget()
    result.AppendMessage(findMainViewModelBridge(target))

def findMainViewModelBridge(target):
    instances = target.FindGlobalVariables('gInstance', 100)
    for value in instances:
        if "PHeadMainViewModelBridge" in value.GetDisplayTypeName():
            return value.GetChildMemberWithName('_viewModel').GetChildAtIndex(0).GetChildAtIndex(0).GetChildAtIndex(0).GetValue()


def generateOptionParser():
    usage = "usage: %prog [options] TODO Description Here :]"
    parser = optparse.OptionParser(usage=usage, prog="mom")
    parser.add_option("-m", "--module",
                      action="store",
                      default=None,
                      dest="module",
                      help="This is a placeholder option to show you how to use options with strings")
    parser.add_option("-c", "--check_if_true",
                      action="store_true",
                      default=False,
                      dest="store_true",
                      help="This is a placeholder option to show you how to use options with bools")
    return parser

