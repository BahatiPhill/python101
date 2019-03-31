import configparser
import os

def create_config(path):
	"""
	create a configuration file
	"""

	config = configparser.ConfigParser()
	config.add_section("Settings")
	config.set("Settings", "font", "Courier")
	config.set("Settings", "font_size", "10")
	config.set("Settings", "font_style", "Normal")
	#config.set("settings", "font_info", "You are using {0} at {1} pt".format(font, font_size))

	with open(path, 'w') as config_file:
		config.write(config_file)


def crud_config(path):
	"""
	create, read, update, delete a configuration file
	"""
	if not os.path.exists(path):
		create_config(path)


	config = configparser.ConfigParser()
	config.read(path)

	#read some values from the config
	font = config.get("Settings", "font")
	font_size = config.get("Settings", "font_size")

	#Change Value in the config
	config.set("Settings", "font_size", "12")

	#Delete a value from config
	config.remove_option("Settings", "font_style")

	#Writing changes back to the config file
	with open(path, 'w') as config_file:
		config.write(config_file)





if __name__ == '__main__':
	path = 'settings.ini'
	crud_config(path)
