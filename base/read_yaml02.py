import yaml


def read_yaml():
    with open("../data/data_login.yaml","r",encoding="utf-8")as f:
        return yaml.load(f)

if __name__ == '__main__':
    print (read_yaml())
