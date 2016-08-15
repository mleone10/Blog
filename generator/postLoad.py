#!/venv/bin/python
import yaml

class PostFormattingError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def loadPost(path):
    yamlLeader = '---\n'
    metaYaml = dict()
    metaStr = str()
    post = str()

    with open(path) as f:
        if f.readline() != yamlLeader:
            raise PostFormattingError('Bad Formatting at: ' + path)
        else:
            line = f.readline()
            while line != yamlLeader:
                metaStr += line
                line = f.readline()
            metaYaml = yaml.load(metaStr)

        return (metaYaml, f.read())
        
if __name__ == '__main__':
    print loadPost('../posts/testPost.md')
