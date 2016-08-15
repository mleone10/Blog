#!/venv/bin/python
import postGen, postLoad, os, shutil
from os import listdir
from os.path import isfile, join, abspath, dirname

def siteGen():
    postDir = abspath(join(dirname(__file__), '..', 'posts'))
    metaPath = abspath(join(
        dirname(__file__), '..', 'resource', 'sitemeta.yaml'))
    templatePath = abspath(join(
        dirname(__file__), '..', 'resource', 'template.html'))
    cssPath = abspath(join(
        dirname(__file__), '..', 'resource', 'layoutStyle.css'))
    sitePath = abspath(join(
        dirname(__file__), '..', 'site'))

    # Get all post paths
    posts = dict((f[:-3], join(postDir, f)) for f in 
        [f for f in listdir(postDir) if
            isfile(join(postDir, f)) and f.endswith('.md')])
    
    # Generate all post pages
    for name, path in posts.items():
        try:
            # Create the HTML for each individual page
            post = postGen.postGen(metaPath, path, templatePath)

            # Write the post to a file
            with open(abspath(join(sitePath, name + '.html')), 'w') as f:
                f.write(post)
                f.close()
        except postLoad.PostFormattingError as err:
            print err

    # Copy the stylesheet over to the site directory
    shutil.copyfile(cssPath, join(sitePath, 'layoutStyle.css'))

    return posts


if __name__ == '__main__':
    print siteGen()
