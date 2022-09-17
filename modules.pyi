import argparse
import os
class betterargs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--filler',
        dest='target'
    )
    args = parser.parse_args()
    class dialogHandler():
        rawInput = betterargs.args.target
        bracketless1 = rawInput.replace('[', '')
        bracketless2 = bracketless1.replace(']', '')
        quotes = bracketless2.replace("'", '')
        commasWspace = quotes.replace(', ', ' ')
        commas = commasWspace.replace(',', ' ')
        syscom = commas
        sysout = syscom.replace(' ', ', ')

    print(
        dialogHandler.sysout
    )

class exit():
    def _exit(__code__):
        print(
            '%s' % (__code__)
        )
class run():
    def _run(__command__):
        os.system(
            '%s' % (__command__)
        )