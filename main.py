# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import ipfshttpclient
import csv


def csv1():
    with open('output.csv', 'rt') as f:
        data = csv.reader(f)
        cid_set = set()
        cid_dict = {}
        for row in data:
            cid_list, cids_dict = per_string(cid_set, cid_dict, row[0])

        # print(len(cid_list), cid_list)
        cids_dict = dict(sorted(cids_dict.items(), key=lambda x: x[1], reverse=True))
        print(len(cids_dict), cids_dict)
        with open('cids.txt', 'w') as f:
            for item in cid_list:
                f.write("%s\n" % item)

        with open('dict.csv', 'w') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in cids_dict.items():
                if key != '':
                    writer.writerow([key, value])


def per_string(cid_set, cid_dict, uri):
    try:
        cid = uri[:]
        qm_index = cid.find('Qm')
        unique_cid = cid[qm_index:qm_index+46].strip()
        cid_set.add(unique_cid)
        if unique_cid in cid_dict:
            cid_dict[unique_cid] += 1
        else:
            cid_dict[unique_cid] = 1
        return cid_set, cid_dict
    except Exception as e:
        print(e)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    csv1()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
