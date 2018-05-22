def retrieve_settings():
    with open("settings/settings", "r") as settings_file:
        settings = {}

        lines = settings_file.readlines()
        for line in lines:
            if line[0] == "#" or line == "\\n" or line == "\n" or line == "":
                continue
            setting = line[:-1].split("=")
            settings[setting[0]] = setting[1]

    return settings
