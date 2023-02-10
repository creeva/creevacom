import glob
import os
for filepath in glob.iglob('../**/index.html', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace('http://10.10.2.102/creevacom', 'https://creeva.com')
    s = s.replace('http://localhost/wordpress', 'https://creeva.com')
    s = s.replace('https://localhost/wordpress', 'https://creeva.com')
    with open(filepath, "w") as file:
        file.write(s)
#os.system('git commit -am "test"')