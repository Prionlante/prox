import yaml, proxmoxer, argparse

arg = argparse.ArgumentParser()

arg.add_argument('-c', '--create', action='append', help="creating vm")
arg.add_argument('-l', '--login', action='append', help="login in proxmox service")

arg_parse = arg.parse_args()

yaml_path = arg_parse.create[0]
user_data = arg_parse.login[0].split('@')

with open(yaml_path, 'r') as setup:
    file_data = yaml.safe_load(setup)

print('\n\n\n\thello from yaml\t\n\n\n')
print(file_data, end='\n\n\n')

pxmx = proxmoxer.ProxmoxAPI(user_data[1], user=f'{user_data[0]}@pam', password=user_data[3], 
                                    verify_ssl=False, service='PVE')
pxmx.nodes(user_data[2]).qemu.create(vmid='1002')
