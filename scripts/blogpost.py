import glob
import os
for filepath in glob.iglob('../**/index.html', recursive=True):
    with open(filepath) as file:
        s = file.read()
    s = s.replace('http://10.10.2.102/creevacom', 'https://creeva.com')
    s = s.replace('http://localhost/wordpress', 'https://creeva.com')
    s = s.replace('https://localhost/wordpress', 'https://creeva.com')
    s = s.replace('<!-- Powered by Staatic (https://staatic.com/) -->', '')
    s = s.replace('<div class="rb row text-center">WordPress Theme by <a href="https://richwp.com/">RichWP</a></div></footer><script type="text/javascript" src="https://creeva.com/wp-content/plugins/simple-share-buttons-adder/js/ssba.js?ver=1676009712" id="simple-share-buttons-adder-ssba-js"></script>', '')
    with open(filepath, "w") as file:
        file.write(s)
os.system('git commit -am "test"')
