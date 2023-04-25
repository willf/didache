import re


def interleave_files(file1_path, file2_path, output_path):
    with open(file1_path, "r") as file1, open(file2_path, "r") as file2, open(output_path, "w") as output_file:
        for line1, line2 in zip(file1, file2):
            line1 = line1.strip()
            line2 = line2.strip()

            if re.match(r"^\s*[IVXLCDM]+\s*$", line1):
                output_file.write("\n\\chapter " + line1 + "\n")
            elif re.match(r"^\s*\d+\.", line1):
                verse_num, line1 = line1.split(".", 1)
                output_file.write("\\verse " + verse_num + " " + line1.strip() + "\n")
            else:
                output_file.write(line1 + "\n")

            if re.match(r"^\s*[IVXLCDM]+\s*$", line2):
                output_file.write("\n")
            elif re.match(r"^\s*\d+\.", line2):
                verse_num, line2 = line2.split(".", 1)
                output_file.write("\\verse " + verse_num + " " + line2.strip() + "\n\n")
            else:
                output_file.write(line2 + "\n\n")

if __name__ == "__main__":
    interleave_files("english.txt", "greek.txt", "bilingual.txt")
