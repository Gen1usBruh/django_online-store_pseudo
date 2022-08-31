import os

def replace_static_source(filename):

    """ Does not work if a link in quotes starts on one line 
        and ends on the other """

    path_to_file = f"{path_to_templates_dir}\\{filename}"
    prefix_file = "rename_"
    prefix_filename = prefix_file + filename
    path_to_prefix_file = f"{path_to_templates_dir}\\{prefix_filename}"

    file_ptr = open(path_to_file, 'r', encoding="utf-8")
    file_ptr_buf = open(path_to_prefix_file, 'w', encoding="utf-8")

    for line in file_ptr:
        for word in match_words:
            index_str = line.find(word)
            if index_str != -1:
                index_quote = line.find("\"")
                index_quote_save = index_quote
                while index_quote != -1:
                    if index_str - index_quote < 0:
                        break
                    index_quote_save = index_quote
                    index_quote = line.find("\"", index_quote + 1)
                if index_quote != -1:
                    found_slice = line[index_quote_save + 1 : index_quote]
                    if found_slice.find("http") != -1:
                        break
                    line = line.replace(found_slice, \
                    replace_with_string[:-(replace_with_list[:-1].__len__())] \
                    + ('\'{}\' '.format(found_slice.strip(" .."))) + replace_with_list[-1], 1)
                    break
        file_ptr_buf.write(line)

    file_ptr.close()
    file_ptr_buf.close()

    os.remove(path_to_file)
    os.rename(path_to_prefix_file, path_to_file)
    

match_words = ['vendor/', 'css/', 'js/']

replace_with_string = "{% static %}"

replace_with_list = list(replace_with_string.split())

path_to_templates_dir = "C:\django-site\projects_and_venv\mystore\store-template-master\\auth"


for filename in os.listdir(path_to_templates_dir):
    if filename.endswith(".html"):
        replace_static_source(filename)
                    