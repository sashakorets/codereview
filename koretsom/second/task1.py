'''
перевірити чи існує певна папка на вашому компютері
приклад файлової системи ['C:',['baackup.log','ideas.txt',['same_directory,same_file.txt]]]
'''

def run_list(same_list,parametr_stop):
    for element in same_list:
        if element==parametr_stop:
            return True
        else:
            continue

def list_yes_or_no()


def file_search(folder,file_path):
    file_list = file_path.split('/')
    if folder[0]==file_list[0]:
        if run_list(folder[1],file_list[1]):
            print('ok')
        else:
            print('error')
    else:
        print('error')
    return 'end'

print(file_search(['C:',['baackup.log','ideas.txt']],'C:/ideas.txt'))

print('C:/ideas.txt'.split('/'))
