from jinja2 import Environment, FileSystemLoader
import markdown, yaml, os

thisDir = os.path.dirname(os.path.abspath(__file__))

pageVars = dict()
metaDict = dict()
meta = str()

with open('testPost.md') as f:
    f.readline()
    line = f.readline()
    while (line != '---\n'):
        meta += line
        line = f.readline()
    metaDict = yaml.load(meta) 
    post = markdown.markdown(f.read(),
    extensions=['markdown.extensions.attr_list'])

pageVars['pageTitle'] = 'Static'
pageVars['name'] = 'Mario Leone'
pageVars['blurb'] = 'Short profile blurb goes here'
pageVars['postTitle'] = metaDict['title']
pageVars['postSubtitle'] = metaDict['subtitle']
pageVars['postDate'] = metaDict['date']
pageVars['postBody'] = post

env = Environment(loader = FileSystemLoader(thisDir), trim_blocks = True)
print env.get_template('template.html').render(pageVars)
