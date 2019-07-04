

import lldb
import os
import shlex
import optparse

def __lldb_init_module(debugger, internal_dict):
    debugger.HandleCommand(
    'command script add -f mom.handle_command print_mom')
def prepend(List, str):

    # Using format()
    str += '{0}'
    List = ((map(str.format, List)))
    return List
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

    commandString = 'po [GetModelBridgeInstance() getMOM:@[]]'

    if options.keys:
        keys = [x.strip() for x in options.keys.replace('"', '').split(',')]
        prepended = prepend(keys, '@"')
        appended = [s + '",' for s in prepended]
        string = ''.join(appended)
        string = string[:-1]
        commandString = 'po [GetModelBridgeInstance() getMOM:@[{}]]'.format(string)

    res = lldb.SBCommandReturnObject()
    lldb.debugger.GetCommandInterpreter().HandleCommand(commandString, res)
    returnVal = res.GetOutput()
    result.AppendMessage(returnVal)


def generateOptionParser():
    usage = "usage: %prog [options] TODO Description Here :]"
    parser = optparse.OptionParser(usage=usage, prog="mom")
    parser.add_option("-k", "--keys",
                      action="store",
                      default=None,
                      dest="keys",
                      help="This is a placeholder option to show you how to use options with strings")
    return parser

