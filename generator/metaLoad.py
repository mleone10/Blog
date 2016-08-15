#!/venv/bin/python
import yaml

def metaLoad(path):
    f = open(path)
    return (yaml.load(f.read()))

if __name__ == '__main__':
    print load('../template/sitemeta.yaml')
