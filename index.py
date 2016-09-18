import rinobot_plugin as bot
import ast
import yaml

def main():
    filepath = bot.filepath()

    obj = {}

    with open(filepath) as f:
        for line in f.readlines():
            if '[' not in line and ']' not in line:
                x, y = line.split('=')
                try:
                    y = ast.literal_eval(y.strip())
                except:
                    y = y.strip()
                obj[x.strip()] = y

    outname = bot.no_extension() + '.yaml'
    outpath = bot.output_filepath(outname)

    with open(outpath, 'w') as outfile:
        outfile.write(yaml.dump(obj, default_flow_style=False))

if __name__ == "__main__":
    main()
