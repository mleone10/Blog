#!/venv/bin/python
import postGen, postLoad, os
from os import listdir
from os.path import isfile, join, abspath, dirname

def siteGen():
    postDir = abspath(join(dirname(__file__), '..', 'posts'))
    metaPath = abspath(join(
        dirname(__file__), '..', 'resource', 'sitemeta.yaml'))
    templatePath = abspath(join(
        dirname(__file__), '..', 'resource', 'template.html'))

    # Get all post paths
    posts = dict((f[:-3], join(postDir, f)) for f in 
        [f for f in listdir(postDir) if
            isfile(join(postDir, f)) and f.endswith('.md')])
    
    print posts
    # Generate all post pages
    for name, path in posts.items():
        try:
            postGen.postGen(metaPath, path, templatePath)
        except postLoad.PostFormattingError as err:
            print err


if __name__ == '__main__':
    print siteGen()
