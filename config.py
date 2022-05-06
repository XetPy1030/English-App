import configparser
config = configparser.ConfigParser()
config.read("config.ini")

app_name = config["DEFAULT"]["app_name"]
app_size = config["DEFAULT"]["app_size"]
button_search = config["DEFAULT"]["button_search"]
not_found = config["DEFAULT"]["not_found"]
search_in = config["DEFAULT"]["search_in"].split(",")
info = config["DEFAULT"]["info"]