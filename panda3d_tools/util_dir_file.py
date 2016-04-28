import os
import shutil
    
# ������������ ���� ��� �����
def cor_path(path, type=None):
    raw = '{!r}'.format(path)
    rezr = raw.replace("\\", "/").replace("//", "/").replace("'", '')
    if type:
        rez = rezr.replace("\\", "/")
    else:
        u = rezr[0]
        p = rezr[:].split('/')
        x = p[1:]
        x.insert(0, p[0].lower().replace(":", ""))
        rez = '/' + '/'.join(x)
    return rez

# ��������� ������������� ���������� � ������������� ���������� � ������ �����
def getRelative(path_export, dir_copy_tex, tex_adress):

    # �������� ������ ����� �����, ��� ���������� �����
    # ���� �������� ������
    # ���� ����������� �������� ������
    
    # ������������ ����� ����������� �� ���������� � ���
    (dirName, fileName) = os.path.split(tex_adress)
    
    # ���������� �������������� ����
    relpath = os.path.relpath(dir_copy_tex, path_export)
    
    # � ���������� ��������� ��� �����, � �������� ������ ������������� �����
    fulrelpath = os.path.join(relpath, fileName)

    # ��������� �������������� ������������� ����
    return (relpath, fulrelpath)

def dir_create_save(dir_copy_tex, path_export, tex_adress):

    # ��������� ��� ������� ����������, ���� ���������
    fd = os.getcwd()
                                    
    # ��������� ���������� �� ����������
    if os.path.exists(path_export):
        # ��������� � ���������� ���� �� ����������� �gg
        os.chdir(path_export)
    else:
        # ���� ���, �� �������
        os.makedirs(path_export)
        # ��������� � ���������� ���� �� ����������� �gg
        os.chdir(path_export)
                                 
    # �������� ������������� ���� � ������������� ���� � ������ �����
    # ������������ ���������� ���� �������������� egg
    (relpath, fulrelpath) = getRelative(path_export, dir_copy_tex, tex_adress)

    # ��������� ���������� �� ����������
    if os.path.exists(relpath):
                            
        # �������� ��������
        shutil.copy(tex_adress, relpath)
                                
    else:
                            
        # ���� ���, �� �������
        os.makedirs(relpath)

        # �������� ��������
        shutil.copy(tex_adress, relpath)
                                
    # ����������� ����� � ������� ����������
    os.chdir(fd)
                                
    # ����������� ���� ��� �����
    path = cor_path(fulrelpath, type=1)

    return path