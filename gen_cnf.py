import os

# k_cnf = [3,4,5,6]
k_cnf = [2,3,4]

# nr_var = [60,100,150,300,600,1000]
nr_var = [30]

nr_of_cnfs = 3
trans_point = { 2:1, 3: 4.2, 4: 10.5, 5:6, 6:7}

# quality_per = [0.5, 0.75, 0.9, 1, 1.1, 1.25, 1.5]
quality_per = [1]

# cnf_folder_path = '/home/dw/Benchamrk_CNF_Gen/kCNFs/'
cnf_folder_path = '/home/dw/Benchamrk_CNF_Gen/hardestKCNFs/'


def gen_cnf():
    print "ello", str(trans_point[3])
    for i_k in k_cnf:
        for i_n in nr_var:
            for i_q in quality_per:
                for i_cnfs in range(0,nr_of_cnfs):
                    nr_clauses = i_n*trans_point[i_k]*i_q
                    command_string = 'cnfgen randkcnf %d %d %d'%(i_k, i_n, nr_clauses)
                    cnf_file_name = 'randkcnf_%d_%d_%d_%d.cnf'%(i_k, i_n, nr_clauses,i_cnfs)
                    os.system(command_string +' > '+cnf_folder_path+cnf_file_name)

if __name__ == "__main__":
    gen_cnf()
