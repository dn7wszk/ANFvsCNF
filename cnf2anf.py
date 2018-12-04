import os


def cnf2anf():
    cnf_folder_path = '/home/dw/Benchamrk_CNF_Gen/hardestKCNFs/'
    anf_folder_path = '/home/dw/Benchamrk_CNF_Gen/hardestKANFs/'

    all_cnf_files = os.listdir(cnf_folder_path)
    for i_file in all_cnf_files:
        anf_file = open(anf_folder_path+i_file[:-3]+'anf.sage','w')
        anf_file_string = ""
        ring_string="R.<"
        eqs_string = "F=["
        for line in open(cnf_folder_path+i_file,'r'):
            if line[0] == 'c':
                continue
            elif line[0] == 'p':
                nr_var = int(line.split()[2])
                for i_n in range(1,nr_var+1):
                    ring_string+="x_%d,"%(i_n)
                ring_string = ring_string[:-1] + ">=BooleanPolynomialRing()\n\n"
            else:
                var_in_eqs = line.split(" ")
                eqs_temp = ""
                for i_var in range(0,len(var_in_eqs)-1):
                    if int(var_in_eqs[i_var]) < 0:
                        eqs_temp += "(x_%d+1)*"%(-1*int(var_in_eqs[i_var]))
                    if int(var_in_eqs[i_var]) > 0:
                        eqs_temp += "x_%d*"%(int(var_in_eqs[i_var]))
                eqs_temp = eqs_temp[:-1]+", "
                eqs_string += eqs_temp
        eqs_string = eqs_string[:-2]+"]"
        anf_file.write(ring_string)
        anf_file.write(eqs_string)
        anf_file.close()


if __name__ == "__main__":
    cnf2anf()

#
# for line in open(filename, 'r'):
#         if line[0] in ['p']:
#             verticesNumber = int(line.split()[2])
#             f.write('<nodes count="%d">\n' %(verticesNumber))
#             #for i in range(1,verticesNumber+1):
#             #    f.write('<node id="%d.0" label="%d"/>\n' %(i,i))
#             f.write('</nodes>\n')
#             f.write('<edges count="250">\n')
#         if not line[0] in ['c','p']:
#             edgeIndex = writeEdge(f, line.split(), edgeIndex)
