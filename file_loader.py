import os
import pdf_reader


def get_abs_path(rel_path):

    this_dir = os.path.dirname(__file__)
    return os.path.join(this_dir, rel_path)


def save_text(filename,text_content):


    save_dir = 'Testes/logs/'
    save_file = 'log(' +filename+').txt'
    file_path =  get_abs_path(save_dir+save_file)

    with open(file_path, mode='wt', encoding='utf-8') as f_w:

        f_w.write(text_content)



def pdf_path(filename):


    save_dir = r'Testes/'
    load_file = filename+'.pdf'

    return get_abs_path(save_dir+load_file)



pdf_name = 'dom5995 - assinado'
pdf_file_path = pdf_path(pdf_name)
pdf_text = pdf_reader.pdf_to_text(pdf_file_path)
save_text(pdf_name, pdf_text)