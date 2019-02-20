#!/usr/bin/env python3
import imp
import os
import sys
import telegram
import yaml

with open("config.yml", 'r') as f:
    global conf
    conf = yaml.load(f)


if __name__ == '__main__':
    to_load = conf.conf['plugins']
    plugins_dir = [os.path.join(os.getcwd(), 'plugins')]
    
    for plugin in to_load:
        try:
            modinfo = imp.find_module(plugin, plugins_dir)
            plug = imp.load_source(plugin, modinfo[1])
        except ImportError as e:
            if str(e).startswith('No module named'):
                print(f"Can't find plugin {plugin}: Check your spelling and try again.")
            else:
                print(f"Failed to load plugin {plugin} import error {str(e)}")
