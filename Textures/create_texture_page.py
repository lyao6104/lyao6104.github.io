# create_texture_page.py
# This file is meant to generate a page that lists all the available textures.

import os

def make_link(text, url):
    return "[" + text + "](" + url + ")"

def make_name(filename):
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    chars = list(filename)
    i = 1
    while i < len(chars):
        separate = ((chars[i] in caps) and (i >= len(chars) or (chars[i + 1] not in caps))) or ((chars[i] in numbers) and (chars[i - 1] not in numbers))
        if separate:
            chars.insert(i, " ")
            i += 1
        i += 1
    return "".join(chars)

dir_name = os.path.dirname(__file__)
dir_contents = os.listdir(dir_name)

texture_dict = {}
texture_categories = []
for i in range(len(dir_contents)):
    file = os.path.join(dir_name, dir_contents[i])
    if os.path.isdir(file):
        texture_categories.append((dir_contents[i], file))

for category in texture_categories:
    textures = os.listdir(category[1])
    for i in range(len(textures)):
        textures[i] = (textures[i], os.path.join(category[1], textures[i]))
    texture_dict[category[0]] = textures

with open(os.path.join(dir_name, "textures.md"), "w") as page:
    page.write("---\ntitle: Larry Yao\n---\n\n## Textures\n\n")
    page.write("On this page, you can find various textures that I've made, most of which are from\n")
    page.write("my work with McMaster Start Coding. Unless otherwise specified, all textures are licensed under\n")
    page.write(make_link("Creative Commons Attribution-ShareAlike 4.0 International", "https://creativecommons.org/licenses/by-sa/4.0/") + ".\n\n")

    page.write("Do note that, while I will *try* to make sure these URLs don't change, there is no guarantee that they will always stay the same.\n")

    for category, textures in texture_dict.items():
        page.write("\n## " + make_name(category) + "\n\n")
        for texture, path in textures:
            if texture.count("_notes.txt") > 0:
                continue
            name = make_name(str.partition(texture, ".")[0])
            relative_path = category + "/" + texture
            notes_path = str.rpartition(path, ".")[0] + "_notes.txt"
            page.write("- " + make_link(name, relative_path) + "\n")
            if os.path.exists(notes_path):
                with open(notes_path, "r") as notes_file:
                    notes = notes_file.read().replace("\n", " ")
                    page.write("  - " + notes + "\n")