import liangs_algorithm
import http_client
import dice_roller

selectedAlg = input('Hello. Please select an algorithm you would like to preview\n'
                    ' 1.: Liang\'s algorithm\n'
                    ' 2.: HttpClient\n'
                    ' 3.: DnD Dice Roller\n')

if int(selectedAlg) == 1:
    liangs_algorithm.start_liangs_algorithm()
elif int(selectedAlg) == 2:
    http_client.getAddress()
elif int(selectedAlg) == 3:
    dice_roller.get_input()

