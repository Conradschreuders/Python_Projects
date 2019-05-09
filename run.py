import time
from clientFiles import findClientFile

write_file = open("log.txt", 'w')

path = 'H:\My Documents\Programming\joblog\\'
#import Histogram

write_file.write("creation Histogram finished")

path2 = 'H:\My Documents\Programming\joblog\\'
#import Capitalize
#MakeCapital.run(path2)

path3 = r'\\sb2210009332.ad.ing.net\FACTORLINK\Import\Clients\Handled'
findClientFile('75', 100)

write_file.write("creation capitalized files finished")
write_file.close()
time.sleep(2)
