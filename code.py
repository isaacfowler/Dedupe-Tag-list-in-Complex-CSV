import csv

# Configuration
filename = 'source.csv' # CSV including entire export
col_index = 5 # Column that includes all tags

target_cell_list = None # Empty list used in code to contain the target cell contents
tag_list = [] # Empty list to contain deduped tag list

with open(filename, 'r') as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        target_cell_list = row[col_index].split(',')
        for item in target_cell_list:
            if item not in tag_list:
                tag_list.append(item)

tag_list.sort()
print(tag_list)
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([tag_list])
