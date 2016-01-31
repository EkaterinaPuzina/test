def count_one(input_filename, output_filename):
    op_file = open(input_filename)
    file_string = op_file.read()

    string_one = ""
    max_len = 0
    i = 0
    while i < len(file_string):
        if file_string[i] == "0" or i == len(file_string)-1:
            if max_len < len(string_one):
                max_len = len(string_one)
            string_one = ""
        else:
            string_one = string_one + file_string[i]
        i += 1

    wr_file = open(output_filename, "w")
    wr_file.write(str(max_len))
    wr_file.close()

    return wr_file

count_one("INPUT.TXT", "OUTPUT.TXT")
