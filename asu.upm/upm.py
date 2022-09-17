#!/usr/bin/env python
import os
import argparse

    # Universal Package Manager/upm
    # written and maintained by alyxx

    # exit codes are related to how high i was at the time of coding that segment block
    # apologies if the code is not as readable as possible, i think it's fun though.

def __to_do__():
    print(
    '''
    To-Do list:
        --add all package managers
        --finish adding all options and main functions
        --find a way to push and pull from repos from within script?
        --add manager.conf file
        --make downloader function
        --add winget commands
        --add pacstall
        --finish help/man page
    '''
    )
def __exit(code_): 
    print(
        'err::%s' % (
            code_
        )        #had to add an actual exit function in to ensure... exiting.\
                #definitely like an 8 right now but it got annoying having two 'exit' codes
    )
    exit()     

def _run(command_):
    os.system(
        '%s' % (
            command_
        )
    )

def downloader(package_, uri):
    _run(
        command_='sudo %s download %s' % (
            __manager.stored__,
            package_
        )
    )
    __exit(code_=4)

def _install(package_):
    print(
            'Installing %s with %s' % (
                dialogHandler.sysout, __manager.stored__
            )
        )
    if __manager.stored__ == 'pacman':
        _run(
            command_='sudo pacman -S %s' % (
                package_
            )
        )
    elif __manager.stored__ == 'pacstall':
        __exit(code=4)
    else:
        if args.noconfirm == True:
            _run(
                command_='sudo %s install %s -y' % (
                    __manager.stored__,
                    package_
                )
            )
        else:
            _run(
                command_='sudo %s install %s' % (
                    __manager.stored__, package_
                )
            )
        
def _remove(package_):
    print(
            'Removing %s with %s' % (
                dialogHandler.sysout, __manager.stored__
            )
    )
    if __manager.stored__ == 'pacman':
        _run(
            command_='sudo pacman -R %s' % (
                package_
            )
        )
    else:
        if args.noconfirm == True:
            _run(
                command_='sudo %s remove %s -y' % (
                    __manager.stored__,
                    package_
                )
            )
        else:
            _run(
                command_='sudo %s remove %s' % (
                    __manager.stored__,
                    package_
                )
            )

def _update(package_):
    print(
        'Updating system packages with %s' % (
            __manager.stored__
        )
    )
    if __manager.stored__ == 'pacman':
        _run(
            command_='sudo pacman -Syu'
        )
    else:
        if args.noconfirm == True:
            print(
                'running updates in background..'
            )
            _run(
                command_='sudo %s update -y >> ~/.updates' % (
                    __manager.stored__
                )
            )
            print(
                'upgrading installs'
            )
            _run(
                command_='sudo %s upgrade -y' % (
                    __manager.stored__
                )
            )
        else:
            print(
                'running updates in background..'
            )
            _run(
                command_='sudo %s update -y >> ~/.updates' % (
                    __manager.stored__
                )
            )
            print(
                'upgrading installs'
            )
            _run(
                command_='sudo %s upgrade' % (
                    __manager.stored__
                )
            )
def _help():    #argparse's built in help function is ass and i want as much customization as possible
    print(
        '''
        Universal Package Manager/upm     
        [written/maintained by Alyxx]

    !! might/should work with winget? !!

Usage: [-I] [-R] [-U] [-P] [-d]
       [--manager] [--sandbox] [--autoremove] [--debug]

ex. [upm -I firefox] Would install the firefox from our repository
ex. [upm -I firefox --manager snap] Would install the snap version of firefox

Options:
-I, --install        Installs specified package
-R, --remove         Removes specified package
-U, --update         Updates packages in background then upgrades available packages
-P, --purge          Remove package as well as all dependencies/unused related packages
-d, --details        Gives information on the specified package as well as the dependencies

Long commands only:
--no-confirm         Don't require confirmation for further permissions
--manager            If a specific package manager needs to be used, use this flag
--autoremove         Autoremove unused/unneeded packages from system

Dev tools:
--sandbox            sandbox and test package without installing to system [WIP]
--debug
        '''
    )

def _purge(package_):
    print(
        'Purging files associated with %s' % (
            package_
        )
    )
    if args.noconfirm == True:
        _run(
            command_='sudo %s purge %s -y' % (
                __manager.stored__,
                package_
            )
        )
    else:
        _run(
            command_='sudo %s purge %s' % (
                __manager.stored__,
                package_
            )
        )

#fuck it's 3am, i have to be up for work at 5
def _details(package_):
    print(
        'searching for information on package %s' % (
            package_
        )
    )
    _run(
        command_='sudo %s show %s' % (
            __manager.stored__,
            package_
        )
    )

parser = argparse.ArgumentParser(add_help=True)
class flags():
    parser.add_argument(
        '-m', '--manual',
        dest='man',
        help='nicer help page/manual (more effort pls use)',
        action='store_true'
    )
    parser.add_argument(
        '-I', '--install',
        dest='install',
        help='install package',
        action='store_true'    
    )
    parser.add_argument(
        '-R', '--remove',
        dest='remove',
        help='remove package',
        action='store_true'
    )
    parser.add_argument(
        '-U', '--update',
        dest='update',
        help='update packages',
        action='store_true'
    )
    #im lazy asl
    argument = parser.add_argument
    argument(
        '-P', '--purge',
        dest='purge',
        action='store_true'
    )
    argument(
        '-d', '--details',
        dest='show',
        action='store_true'
    )
    argument(
        '--no-confirm',
        dest='noconfirm',
        action='store_true', default=False
    )
    argument(
        '--autoremove',
        dest='autoremove',
        action='store_true'
    )
    parser.add_argument(
        '--sandbox',
        dest='sandbox',
        help='sandbox and test package without installing to system',
        action='store_true', default=False
    )
    parser.add_argument(
        '--debug',
        dest='debug',
        action='store_true'
    )
    parser.add_argument(
        '--manager',
        dest='manager',
        help='change targetted package manager',
        action='append', nargs='?'
    )
    parser.add_argument(
        dest='target',
        help='points to targeted item',
        action='append',
        nargs='?'
    )
args = parser.parse_args()


class dialogHandler():
    rawInput = '%s' % (args.target)
    bracketless1 = rawInput.replace('[', '')
    bracketless2 = bracketless1.replace(']', '')
    quotes = bracketless2.replace("'", '')
    commasWspace = quotes.replace(', ', ' ')
    commas = commasWspace.replace(',', ' ')
    syscom = commas
    sysout = syscom.replace(' ', ', ')
class __manager():
    rawInput = '%s' % (args.manager)
    bracketless1 = rawInput.replace('[', '')
    bracketless2 = bracketless1.replace(']', '')
    quotes = bracketless2.replace("'", '')
    commasWspace = quotes.replace(', ', ' ')
    commas = commasWspace.replace(',', ' ')
    stored__ = commas
    if stored__ == 'None':
        stored__ = 'nala'

def _test_():     #keep test function maintained, actually useful for new variables/conditions
    print(
        'sysout:', 
        dialogHandler.sysout
    )
    print( 
        'syscom:', 
        dialogHandler.syscom
    )
    print(
        'manager:',
        __manager.stored__
    )
    #__exit(code_=0)

def pipeline():
    if args.debug == True:
        _test_()
        __exit(code_=8.5)
    if args.install == True:
        _install(
            package_='%s' % (
                dialogHandler.syscom
            )
        )
        __exit(code_=1)
    if args.remove == True:
        _remove(
            package_='%s' % (
                dialogHandler.syscom
            )
        )
        __exit(code_=5)
    if args.update == True:
        _update(
            package_='%s' % (
                dialogHandler.syscom
            )
        )
        __exit(code_=0)
    if args.purge == True:
        _purge(
            package_='%s' % (
                dialogHandler.syscom
            )
        )
        __exit(code_='6 maybe 7')
    if args.show == True:
        _details(
            package_='%s' % (
                dialogHandler.syscom
            )
        )
        __exit(code_=6)
    if args.man == True:
        if dialogHandler.syscom == 'todo':
            __to_do__()
        else:
            _help()
        __exit(code_=4)

pipeline()