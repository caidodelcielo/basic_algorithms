import liangs_algorithm
import http_client
import dice_roller
import merge_sort
import message_html_generator
import prostreno_leaderboard

selectedAlg = input('Hello. Please select an algorithm you would like to preview\n'
                    ' 1.: Liang\'s algorithm\n'
                    ' 2.: HttpClient\n'
                    ' 3.: DnD Dice Roller\n'
                    ' 4.: Merge Sort\n'
                    ' 5.: Prostřeno leaderboard\n')
                    ' 6.: HTML generator\n')

if int(selectedAlg) == 1:
    liangs_algorithm.start_liangs_algorithm()
elif int(selectedAlg) == 2:
    http_client.getAddress()
elif int(selectedAlg) == 3:
    dice_roller.get_input()
elif int(selectedAlg) == 4:
    merge_sort.start_sort()
elif int(selectedAlg) == 5:
    prostreno_leaderboard.start_scraping()
elif int(selectedAlg) == 6:
    message_html_generator.generateHTML()

