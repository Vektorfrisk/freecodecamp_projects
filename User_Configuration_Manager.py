def add_setting(settings, key_value):
    key_value = tuple(value.lower() for value in key_value)
    if key_value[0] in settings:
        return f"Setting '{key_value[0]}' already exists! Cannot add a new setting with this name."
    else:
        settings[key_value[0]] = key_value[1]
        return f"Setting '{key_value[0]}' added with value '{key_value[1]}' successfully!"

def update_setting(settings, key_value):
    key_value = tuple(value.lower() for value in key_value)
    if key_value[0] in settings:
        settings[key_value[0]] = key_value[1]
        return f"Setting '{key_value[0]}' updated to '{key_value[1]}' successfully!"
    else:
        return f"Setting '{key_value[0]}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()
    #print(key)
    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if len(settings) == 0: 
        
        return f"No settings available."
    else:
        capital_settings = ''
        for key, value in tuple(settings.items()):
            capital_settings += f"\n{key.capitalize()}: {value}"
        return (f'Current User Settings:{capital_settings}\n')
        

test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}
print(add_setting(test_settings, ('language', 'English')))
