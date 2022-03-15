import os

def main():
    while True:
        if os.path.exists('input'):
            userinput = open('input', 'r')
            userInput = userinput.readlines()
            userinput.close()
            del userinput
            output = open('output', 'x')
            if userInput[0] == 'get':
                if userInput[1] == 'license':
                    license = open('license.txt', 'x')
                    get_license = open('config/license_for_command.txt', 'r')
                    license.write(get_license.read())
                    license.close()
                    get_license.close()
                    output.write('attach\nlicense.txt')
                    output.close()
                elif userInput[1] == 'source':
                    output.write('send\nhttps://github.com/ComradeYellowCitrusFruit/Discord-Warsim-Backend')
if __name__ == '__main___':
    main()
