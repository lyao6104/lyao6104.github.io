# create_texture_page.py
# This file is meant to generate a page that lists all the available textures.

import os

# Makes the given text and url into a Markdown link.
def make_link(text, url):
    return "[" + text + "](" + url + ")"

# Adds space separators to file names for readability.
def make_name(filename):
    caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    chars = list(filename)
    i = 1
    while i < len(chars):
        separate = ((chars[i] in caps) and (i >= len(chars) or (
            chars[i + 1] not in caps))) or ((chars[i] in numbers) and (chars[i - 1] not in numbers))
        if separate:
            chars.insert(i, " ")
            i += 1
        i += 1
    return "".join(chars)


# Get directory and contents.
dir_name = os.path.dirname(__file__)
dir_contents = os.listdir(dir_name)

# Create texture categories from folders in the directory.
texture_dict = {}
texture_categories = []
for i in range(len(dir_contents)):
    file = os.path.join(dir_name, dir_contents[i])
    if os.path.isdir(file):
        texture_categories.append((dir_contents[i], file))

# Add textures to categories
for category in texture_categories:
    textures = []
    category_contents = os.listdir(category[1])
    for file in category_contents:
        if file.count("_notes.txt") < 1:
            textures.append((file, os.path.join(category[1], file)))
    texture_dict[category[0]] = textures

# Write the texture list as a Markdown file, which will be included in the site by Jekyll.
with open(os.path.join(dir_name, "texture_list.md"), "w") as page:
    page.write("## Categories\n")

    # Loop through all categories.
    for category, textures in texture_dict.items():
        page.write("\n### " + make_name(category) + "\n\n")

        # Add notes if they exist.
        # Notes can contain things like additional details, license information, etc.
        category_notes_path = dir_name + "/" + category + "_notes.txt"
        if os.path.exists(category_notes_path):
            with open(category_notes_path, "r") as notes_file:
                notes = notes_file.read().replace("\n", " ")
                page.write(notes + "\n\n")

        # Loop through textures and write them to a Markdown list.
        for texture, path in textures:
            name = make_name(str.partition(texture, ".")[0])
            relative_path = "/Textures/" + category + "/" + texture
            texture_notes_path = str.rpartition(path, ".")[0] + "_notes.txt"
            page.write("- " + make_link(name, relative_path) + "\n")
            # Add notes if they exist.
            if os.path.exists(texture_notes_path):
                with open(texture_notes_path, "r") as notes_file:
                    notes = notes_file.read().replace("\n", " ")
                    page.write("  - " + notes + "\n")
