from jinja2 import FileSystemLoader, Environment
import os
import re
import sys
import yaml

# jenv = Environment(loader=FileSystemLoader(os.getcwd()), trim_blocks=True, lstrip_blocks=True)
# template = jenv.get_template('templates/main.j2')

re_site_code = re.compile('[gGiImMpP][aAnNqQsSvVwW]\w{4}')


def intro():
    # TODO: Clear screen and write program usage
    pass

def get_device_type():
    device_type = raw_input('Device type (R/s): ').lower()
    if device_type == 'r' or '\n':
        return 'Router'
    elif device_type == 's':
        return 'Switch'
    else:
        print('Type r for Router[default] or s for Switch: ')
        return get_site_code()


def get_site_id():
    return raw_input('Site Code: ').upper()


def validate_site_id(site_id):
    return re_site_code.search(site_id).group()


def main():
    with open('./group_vars/site_details', 'r') as f:
        site_codes = yaml.load(f)
    
    intro()
    site_id = get_site_id()
    if not site_codes.get(site_id):
        if not validate_site_id(site_id):
            sys.exit("Invalid site code")
        else:
            pass
            # TODO options for entering in new site details
    else:
        for k, v in site_codes.get(site_id).iteritems():
            print('%-10s %s') % (k.title()+':', str(v))
    
    # TODO Enter is rest of the


if __name__ == "__main__":
    main()
