import sys
import ast
import os
import yaml

def main(filepath):
    filepath_without_ext = os.path.splitext(filepath)[0]
    obj = {}

    with open(sys.argv[1]) as f:
        for line in f.readlines():
            if '[' not in line and ']' not in line:
                x, y = line.split('=')
                try:
                    y = ast.literal_eval(y.strip())
                except:
                    y = y.strip()
                obj[x.strip()] = y

    with open(filepath_without_ext + '.yaml', 'w') as outfile:
        outfile.write(yaml.dump(obj, default_flow_style=False))


if __name__ == "__main__":
    main(sys.argv[1])
