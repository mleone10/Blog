#!/venv/bin/python
import yaml

def loadMeta(path):
    f = open(path)
    return (yaml.load(f.read()))

if __name__ == '__main__':
    print loadMeta('../resource/sitemeta.yaml')
