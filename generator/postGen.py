#!/venv/bin/python
from jinja2 import Environment, FileSystemLoader
import metaLoad, postLoad, markdown, os

def pageGen(metaPath, postPath, templatePath):
    # Load metadata
    meta = metaLoad.loadMeta(metaPath)

    # Load post
    postMeta, post = postLoad.loadPost(postPath)

    # Setup template parameters
    params = dict()
    params['siteMeta'] = meta
    params['postMeta'] = postMeta
    params['postContent'] = markdown.markdown(post,
        extensions=['markdown.extensions.attr_list'])

    # Load parameters
    templateDir = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'resource'))
    env = Environment(loader = FileSystemLoader(templateDir), trim_blocks=True)
    return env.get_template('template.html').render(params)


if __name__ == '__main__':
    print pageGen('../resource/sitemeta.yaml',
                  '../posts/testPost.md',
                  '../resource/template.html')
