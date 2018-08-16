def cs_chain_maker(csv_file):

    import csv
    import numpy as np

    with open(csv_file, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        datalist = list(datareader)    #each row is a list item

    for i in range(0,len(datalist)):   #recreate cells in array
        datalist[i] = str(datalist[i])
        datalist[i] = datalist[i].split("', '")

    man = [None] * len(datalist)      #re-create exsiting variables
    model = [None] * len(datalist)
    years = [None] * len(datalist)
    HTML_table_row = [None] * len(datalist)
    tags = [None] * len(datalist)
    CC = [None] * len(datalist)
    chain_type = [None] * len(datalist)
    chain_length = [None] * len(datalist)


    chain1 = [None] * len(datalist)   #new variables
    chain2 = [None] * len(datalist)
    chain3 = [None] * len(datalist)
    chain4 = [None] * len(datalist)
    chain5 = [None] * len(datalist)
    chain6 = [None] * len(datalist)
    chain7 = [None] * len(datalist)
    chain8 = [None] * len(datalist)
    chain9 = [None] * len(datalist)
    chain10 = [None] * len(datalist)
    chain11 = [None] * len(datalist)
    chain12 = [None] * len(datalist)
    chain13 = [None] * len(datalist)
    chain14 = [None] * len(datalist)
    chain15 = [None] * len(datalist)
    chain16 = [None] * len(datalist)
    chain17 = [None] * len(datalist)
    chain18 = [None] * len(datalist)
    chain19 = [None] * len(datalist)
    chain20 = [None] * len(datalist)
    chain21 = [None] * len(datalist)
    chain22 = [None] * len(datalist)
    chain23 = [None] * len(datalist)
    chain24 = [None] * len(datalist)
    chain25 = [None] * len(datalist)
    chain26 = [None] * len(datalist)
    chain27 = [None] * len(datalist)
    chain28 = [None] * len(datalist)
    chain29 = [None] * len(datalist)
    chain30 = [None] * len(datalist)
    chain31 = [None] * len(datalist)
    chain32 = [None] * len(datalist)
    chain33 = [None] * len(datalist)
    chain34 = [None] * len(datalist)
    chain35 = [None] * len(datalist)
    chain36 = [None] * len(datalist)
    chain37 = [None] * len(datalist)
    chain38 = [None] * len(datalist)
    chain39 = [None] * len(datalist)
    chain40 = [None] * len(datalist)
    chain41 = [None] * len(datalist)
    chain42 = [None] * len(datalist)
    chain43 = [None] * len(datalist)
    chain44 = [None] * len(datalist)
    chain45 = [None] * len(datalist)
    chain46 = [None] * len(datalist)
    chain47 = [None] * len(datalist)
    chain48 = [None] * len(datalist)
    chain49 = [None] * len(datalist)
    chain50 = [None] * len(datalist)
    chain51 = [None] * len(datalist)

    for i in range(0,len(datalist)):

        man[i] = datalist[i][0][2:]    #re-assign exsisting variables
        model[i] = datalist[i][1]
        years[i] = datalist[i][2]
        HTML_table_row[i] = datalist[i][3]
        tags[i] = datalist[i][4]
        CC[i] = datalist[i][5]
        chain_type[i] = datalist[i][6]
        chain_length[i] = datalist[i][7][:-2]

    #Chain assignment

        chain_type[i] = str(chain_type[i])
        CC[i] = int(CC[i])

        if chain_type[i] == '420':
            if CC[i] <= 100:
                chain1[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'D(RJ)-' + str(chain_length[i])
                chain2[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'DGB(RJ)-' + str(chain_length[i])
            if CC[i] <= 150:
                chain3[i] = 'JTC' + str(chain_type[i]) + 'HDR' + str(chain_length[i]) + 'SL'
                chain4[i] = 'JTC' + str(chain_type[i]) + 'HDRNB' + str(chain_length[i]) + 'SL'
                chain5[i] = 'JTC' + str(chain_type[i]) + 'HPGB' + str(chain_length[i]) + 'SL'

        if chain_type[i] == '428':
            if CC[i] <= 125:
                chain6[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'D(RJ)-' + str(chain_length[i])
                chain7[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'DGB(RJ)-' + str(chain_length[i])
                chain8[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'HD(RJ)-' + str(chain_length[i])
                chain9[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'HDGG(RJ)-' + str(chain_length[i])
            if CC[i] <= 200:
                chain10[i] = 'JTC' + str(chain_type[i]) + 'HDR' + str(chain_length[i]) + 'SL'
                chain11[i] = 'JTC' + str(chain_type[i]) + 'HPONB' + str(chain_length[i]) + 'SL'
                chain12[i] = 'JTC' + str(chain_type[i]) + 'HPOGB' + str(chain_length[i]) + 'SL'
            if CC[i] <= 250:
                chain13[i] = 'JTC' + str(chain_type[i]) + 'X1R' + str(chain_length[i]) + 'SL'
            if CC[i] <= 600:
                chain14[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'VX(FJ)-' + str(chain_length[i])
                chain15[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'VXGB(FJ)-' + str(chain_length[i])

        if chain_type[i] == '520':
            if CC[i] <= 250:
                chain16[i] = 'CHAIN-DID-' + str(chain_type[i]) + '(RJ)-' + str(chain_length[i])
                chain17[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'GB(RJ)-' + str(chain_length[i])
                #Update
                chain42[i] = 'CHAIN-RK-' + str(chain_type[i]) + '-' + str(chain_length[i])
                chain43[i] = 'CHAIN-RK-' + str(chain_type[i]) + 'H-' + str(chain_length[i])
            if CC[i] <= 500:
                chain18[i] = 'JTC' + str(chain_type[i]) + 'HDS2' + str(chain_length[i]) + 'SL'
                chain19[i] = 'JTC' + str(chain_type[i]) + 'HDS2NN' + str(chain_length[i]) + 'SL'
                #Update
                chain41[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'NZ(FJ)-' + str(chain_length[i])
            if CC[i] <= 750 and CC[i] > 250:
                chain20[i] = 'JTC' + str(chain_type[i]) + 'X1R2' + str(chain_length[i]) + 'DL'
                chain21[i] = 'JTC' + str(chain_type[i]) + 'X1R2NN' + str(chain_length[i]) + 'DL'
                chain22[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'VX2(ZJ)-' + str(chain_length[i])
                chain23[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'VX2GB(ZJ)-' + str(chain_length[i])
                #Update
                chain44[i] = 'CHAIN-RK-' + str(chain_type[i]) + 'XSO-' + str(chain_length[i])
                chain45[i] = 'CHAIN-RK-' + str(chain_type[i]) + 'XSOGB-' + str(chain_length[i])
            if CC[i] <= 1000 and CC[i] > 500:
                chain24[i] = 'JTC' + str(chain_type[i]) + 'Z3' + str(chain_length[i]) + 'RL'
                chain25[i] = 'JTC' + str(chain_type[i]) + 'Z3NN' + str(chain_length[i]) + 'RL'
            if CC[i] <= 1200 and CC[i] > 500:
                chain26[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'ZVMXGG(ZJ)-' + str(chain_length[i])

        if chain_type[i] == '525':
            if CC[i] <= 800:
                chain27[i] = 'JTC' + str(chain_type[i]) + 'X1R' + str(chain_length[i]) +'RL'
                chain28[i] = 'JTC' + str(chain_type[i]) + 'X1RNN' + str(chain_length[i]) +'RL'
            if CC[i] <= 900:
                chain29[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'VX(ZJ)-' + str(chain_length[i])
                chain30[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'VXGB(ZJ)-' + str(chain_length[i])
                #Update
                chain46[i] = 'CHAIN-RK-' + str(chain_type[i]) + 'XSO-' + str(chain_length[i])
                chain47[i] = 'CHAIN-RK-' + str(chain_type[i]) + 'XSOGB-' + str(chain_length[i])
            if CC[i] <= 1300:
                chain31[i] = 'JTC' + str(chain_type[i]) + 'Z3' + str(chain_length[i]) + 'RL'
                chain32[i] = 'JTC' + str(chain_type[i]) + 'Z3NN' + str(chain_length[i]) + 'RL'
                chain33[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'ZVMXGG(ZJ)-' + str(chain_length[i])
                #Update
                chain48[i] = 'CHAIN-RK-' + str(chain_type[i]) + 'ZXWGB-' + str(chain_length[i])

        if chain_type[i] == '530':
            if CC[i] <= 900:
                chain34[i] = 'JTC' + str(chain_type[i]) + 'X1R' + str(chain_length[i]) + 'RL'
                chain35[i] = 'JTC' + str(chain_type[i]) + 'X1RNN' + str(chain_length[i]) + 'RL'

            if CC[i] <= 1000:
                chain36[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'VX(ZJ)-' + str(chain_length[i])
                chain37[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'VXGB(ZJ)-' + str(chain_length[i])
                #Update
                chain49[i] = 'CHAIN-RK-' + str(chain_type[i]) + 'XSOZ1-' + str(chain_length[i])
                chain50[i] = 'CHAIN-RK-' + str(chain_type[i]) + 'XSOZ1GB-' + str(chain_length[i])

            if CC[i] <= 1400:
                chain38[i] = 'JTC' + str(chain_type[i]) + 'Z3' + str(chain_length[i]) + 'RL'
                chain39[i] = 'JTC' + str(chain_type[i]) + 'Z3NN' + str(chain_length[i]) + 'RL'
                chain40[i] = 'CHAIN-DID-' + str(chain_type[i]) + 'ZVMXGG(ZJ)-' + str(chain_length[i])
                #Update
                chain51[i] = 'CHAIN-RK-' + str(chain_type[i]) + 'ZXWGB-' + str(chain_length[i])


    #chain1 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain1, dtype=str)
    chain_np_list = np.unique(chain_np)

    chain1_list = [None] * len(chain_np_list)
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain1_list[i] = chain_np_list[i]
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain1_tags_list = [None] * len(index)
    chain1_HTML_table = [None] * len(index)

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain1_tags_list[i] = ','.join(array[i])
        chain1_HTML_table[i] = ''.join(HTML_array[i])

    #chain1_HTML_table = chain1_HTML_table[:-1]

    #chain2 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain2, dtype=str)
    chain_np_list = np.unique(chain_np)

    chain2_list = [None] * len(chain_np_list)
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain2_list[i] = chain_np_list[i]
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain2_tags_list = [None] * len(index)
    chain2_HTML_table = [None] * len(index)

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain2_tags_list[i] = ','.join(array[i])
        chain2_HTML_table[i] = ''.join(HTML_array[i])

    #chain3 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain3, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain3_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain3_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain3_tags_list = [None] * len(index)       #
    chain3_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain3_tags_list[i] = ','.join(array[i])        #
        chain3_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain4 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain4, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain4_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain4_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain4_tags_list = [None] * len(index)       #
    chain4_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain4_tags_list[i] = ','.join(array[i])        #
        chain4_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain5 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain5, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain5_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain5_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain5_tags_list = [None] * len(index)       #
    chain5_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain5_tags_list[i] = ','.join(array[i])        #
        chain5_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain6 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain6, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain6_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain6_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain6_tags_list = [None] * len(index)       #
    chain6_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain6_tags_list[i] = ','.join(array[i])        #
        chain6_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain7 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain7, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain7_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain7_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain7_tags_list = [None] * len(index)       #
    chain7_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain7_tags_list[i] = ','.join(array[i])        #
        chain7_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain8 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain8, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain8_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain8_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain8_tags_list = [None] * len(index)       #
    chain8_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain8_tags_list[i] = ','.join(array[i])        #
        chain8_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain9 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain9, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain9_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain9_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain9_tags_list = [None] * len(index)       #
    chain9_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain9_tags_list[i] = ','.join(array[i])        #
        chain9_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain10 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain10, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain10_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain10_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain10_tags_list = [None] * len(index)       #
    chain10_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain10_tags_list[i] = ','.join(array[i])        #
        chain10_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain11 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain11, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain11_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain11_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain11_tags_list = [None] * len(index)       #
    chain11_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain11_tags_list[i] = ','.join(array[i])        #
        chain11_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain12 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain12, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain12_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain12_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain12_tags_list = [None] * len(index)       #
    chain12_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain12_tags_list[i] = ','.join(array[i])        #
        chain12_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain13 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain13, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain13_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain13_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain13_tags_list = [None] * len(index)       #
    chain13_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain13_tags_list[i] = ','.join(array[i])        #
        chain13_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain14 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain14, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain14_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain14_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain14_tags_list = [None] * len(index)       #
    chain14_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain14_tags_list[i] = ','.join(array[i])        #
        chain14_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain15 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain15, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain15_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain15_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain15_tags_list = [None] * len(index)       #
    chain15_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain15_tags_list[i] = ','.join(array[i])        #
        chain15_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain16 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain16, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain16_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain16_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain16_tags_list = [None] * len(index)       #
    chain16_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain16_tags_list[i] = ','.join(array[i])        #
        chain16_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain17 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain17, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain17_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain17_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain17_tags_list = [None] * len(index)       #
    chain17_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain17_tags_list[i] = ','.join(array[i])        #
        chain17_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain18 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain18, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain18_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain18_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain18_tags_list = [None] * len(index)       #
    chain18_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain18_tags_list[i] = ','.join(array[i])        #
        chain18_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain19 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain19, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain19_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain19_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain19_tags_list = [None] * len(index)       #
    chain19_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain19_tags_list[i] = ','.join(array[i])        #
        chain19_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain20 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain20, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain20_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain20_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain20_tags_list = [None] * len(index)       #
    chain20_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain20_tags_list[i] = ','.join(array[i])        #
        chain20_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain21 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain21, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain21_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain21_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain21_tags_list = [None] * len(index)       #
    chain21_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain21_tags_list[i] = ','.join(array[i])        #
        chain21_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain22 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain22, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain22_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain22_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain22_tags_list = [None] * len(index)       #
    chain22_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain22_tags_list[i] = ','.join(array[i])        #
        chain22_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain23 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain23, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain23_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain23_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain23_tags_list = [None] * len(index)       #
    chain23_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain23_tags_list[i] = ','.join(array[i])        #
        chain23_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain24 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain24, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain24_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain24_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain24_tags_list = [None] * len(index)       #
    chain24_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain24_tags_list[i] = ','.join(array[i])        #
        chain24_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain25 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain25, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain25_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain25_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain25_tags_list = [None] * len(index)       #
    chain25_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain25_tags_list[i] = ','.join(array[i])        #
        chain25_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain26 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain26, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain26_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain26_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain26_tags_list = [None] * len(index)       #
    chain26_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain26_tags_list[i] = ','.join(array[i])        #
        chain26_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain27 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain27, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain27_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain27_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain27_tags_list = [None] * len(index)       #
    chain27_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain27_tags_list[i] = ','.join(array[i])        #
        chain27_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain28 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain28, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain28_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain28_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain28_tags_list = [None] * len(index)       #
    chain28_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain28_tags_list[i] = ','.join(array[i])        #
        chain28_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain29 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain29, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain29_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain29_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain29_tags_list = [None] * len(index)       #
    chain29_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain29_tags_list[i] = ','.join(array[i])        #
        chain29_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain30 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain30, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain30_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain30_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain30_tags_list = [None] * len(index)       #
    chain30_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain30_tags_list[i] = ','.join(array[i])        #
        chain30_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain31 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain31, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain31_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain31_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain31_tags_list = [None] * len(index)       #
    chain31_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain31_tags_list[i] = ','.join(array[i])        #
        chain31_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain32 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain32, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain32_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain32_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain32_tags_list = [None] * len(index)       #
    chain32_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain32_tags_list[i] = ','.join(array[i])        #
        chain32_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain33 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain33, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain33_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain33_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain33_tags_list = [None] * len(index)       #
    chain33_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain33_tags_list[i] = ','.join(array[i])        #
        chain33_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain34 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain34, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain34_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain34_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain34_tags_list = [None] * len(index)       #
    chain34_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain34_tags_list[i] = ','.join(array[i])        #
        chain34_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain35 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain35, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain35_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain35_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain35_tags_list = [None] * len(index)       #
    chain35_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain35_tags_list[i] = ','.join(array[i])        #
        chain35_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain36 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain36, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain36_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain36_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain36_tags_list = [None] * len(index)       #
    chain36_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain36_tags_list[i] = ','.join(array[i])        #
        chain36_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain37 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain37, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain37_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain37_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain37_tags_list = [None] * len(index)       #
    chain37_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain37_tags_list[i] = ','.join(array[i])        #
        chain37_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain38 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain38, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain38_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain38_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain38_tags_list = [None] * len(index)       #
    chain38_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain38_tags_list[i] = ','.join(array[i])        #
        chain38_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain39 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain39, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain39_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain39_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain39_tags_list = [None] * len(index)       #
    chain39_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain39_tags_list[i] = ','.join(array[i])        #
        chain39_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain40 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain40, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain40_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain40_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain40_tags_list = [None] * len(index)       #
    chain40_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain40_tags_list[i] = ','.join(array[i])        #
        chain40_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain41 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain41, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain41_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain41_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain41_tags_list = [None] * len(index)       #
    chain41_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain41_tags_list[i] = ','.join(array[i])        #
        chain41_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain42 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain42, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain42_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain42_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain42_tags_list = [None] * len(index)       #
    chain42_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain42_tags_list[i] = ','.join(array[i])        #
        chain42_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain43 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain43, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain43_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain43_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain43_tags_list = [None] * len(index)       #
    chain43_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain43_tags_list[i] = ','.join(array[i])        #
        chain43_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain44 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain44, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain44_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain44_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain44_tags_list = [None] * len(index)       #
    chain44_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain44_tags_list[i] = ','.join(array[i])        #
        chain44_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain45 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain45, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain45_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain45_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain45_tags_list = [None] * len(index)       #
    chain45_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain45_tags_list[i] = ','.join(array[i])        #
        chain45_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain46 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain46, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain46_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain46_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain46_tags_list = [None] * len(index)       #
    chain46_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain46_tags_list[i] = ','.join(array[i])        #
        chain46_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain47 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain47, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain47_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain47_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain47_tags_list = [None] * len(index)       #
    chain47_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain47_tags_list[i] = ','.join(array[i])        #
        chain47_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain48 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain48, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain48_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain48_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain48_tags_list = [None] * len(index)       #
    chain48_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain48_tags_list[i] = ','.join(array[i])        #
        chain48_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain49 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain49, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain49_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain49_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain49_tags_list = [None] * len(index)       #
    chain49_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain49_tags_list[i] = ','.join(array[i])        #
        chain49_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain50 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain50, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain50_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain50_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain50_tags_list = [None] * len(index)       #
    chain50_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain50_tags_list[i] = ','.join(array[i])        #
        chain50_HTML_table[i] = ''.join(HTML_array[i])   #

    #chain51 output list maker
    chain_np = None
    chain_np_list = None

    chain_np = np.ascontiguousarray(chain51, dtype=str)   #
    chain_np_list = np.unique(chain_np)

    chain51_list = [None] * len(chain_np_list)    #
    index = [None] * len(chain_np_list)

    for i in range(0,len(chain_np_list)):
        chain51_list[i] = chain_np_list[i]        #
        index[i] = np.where(chain_np == str(chain_np_list[i]))

    array = [None] * len(index)
    HTML_array = [None] * len(index)
    chain51_tags_list = [None] * len(index)       #
    chain51_HTML_table = [None] * len(index)      #

    for i in range(0,len(index)):
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):
        array[i].sort()
        HTML_array[i].sort()

    for i in range (0,len(array)):
        np_array = np.ascontiguousarray(array[i], dtype=str)
        np_array = np.unique(np_array)
        array[i] = np_array
        np_array = None

    for i in range (0,len(HTML_array)):
        np_HTML_array = np.ascontiguousarray(HTML_array[i], dtype=str)
        np_HTML_array = np.unique(np_HTML_array)
        HTML_array[i] = np_HTML_array
        np_HTML_array = None

    for i in range(0,len(array)):
        chain51_tags_list[i] = ','.join(array[i])        #
        chain51_HTML_table[i] = ''.join(HTML_array[i])   #

    #join lists

    chain_list_out = chain1_list + chain2_list + chain3_list + chain4_list  + chain5_list \
                    + chain6_list + chain7_list + chain8_list + chain9_list + chain10_list \
                    + chain11_list + chain12_list + chain13_list + chain14_list + chain15_list \
                    + chain16_list + chain17_list + chain18_list + chain19_list + chain20_list \
                    + chain21_list + chain22_list + chain23_list + chain24_list + chain25_list \
                    + chain26_list + chain27_list + chain28_list + chain29_list + chain30_list \
                    + chain31_list + chain32_list + chain33_list + chain34_list + chain35_list \
                    + chain36_list + chain37_list + chain38_list + chain39_list + chain40_list \
                    + chain41_list + chain42_list + chain43_list + chain44_list + chain45_list \
                    + chain46_list + chain47_list + chain48_list + chain49_list + chain50_list \
                    + chain51_list

    chain_tags_out = chain1_tags_list + chain2_tags_list + chain3_tags_list + chain4_tags_list \
                     + chain5_tags_list + chain6_tags_list + chain7_tags_list + chain8_tags_list \
                     + chain9_tags_list + chain10_tags_list + chain11_tags_list + chain12_tags_list \
                     + chain13_tags_list + chain14_tags_list + chain15_tags_list + chain16_tags_list \
                     + chain17_tags_list + chain18_tags_list + chain19_tags_list + chain20_tags_list \
                     + chain21_tags_list + chain22_tags_list + chain23_tags_list + chain24_tags_list \
                     + chain25_tags_list + chain26_tags_list + chain27_tags_list + chain28_tags_list \
                     + chain29_tags_list + chain30_tags_list + chain31_tags_list + chain32_tags_list \
                     + chain33_tags_list + chain34_tags_list + chain35_tags_list + chain36_tags_list \
                     + chain37_tags_list + chain38_tags_list + chain39_tags_list + chain40_tags_list \
                     + chain41_tags_list + chain42_tags_list + chain43_tags_list + chain44_tags_list \
                     + chain45_tags_list + chain46_tags_list + chain47_tags_list + chain48_tags_list \
                     + chain49_tags_list + chain50_tags_list + chain51_tags_list

    chain_HTML_out = chain1_HTML_table + chain2_HTML_table + chain3_HTML_table + chain4_HTML_table \
                     + chain5_HTML_table + chain6_HTML_table + chain7_HTML_table + chain8_HTML_table \
                     + chain9_HTML_table + chain10_HTML_table + chain11_HTML_table + chain12_HTML_table \
                     + chain13_HTML_table + chain14_HTML_table + chain15_HTML_table + chain16_HTML_table \
                     + chain17_HTML_table + chain18_HTML_table + chain19_HTML_table + chain20_HTML_table \
                     + chain21_HTML_table + chain22_HTML_table + chain23_HTML_table + chain24_HTML_table \
                     + chain25_HTML_table + chain26_HTML_table + chain27_HTML_table + chain28_HTML_table \
                     + chain29_HTML_table + chain30_HTML_table + chain31_HTML_table + chain32_HTML_table \
                     + chain33_HTML_table + chain34_HTML_table + chain35_HTML_table + chain36_HTML_table \
                     + chain37_HTML_table + chain38_HTML_table + chain39_HTML_table + chain40_HTML_table \
                     + chain41_HTML_table + chain42_HTML_table + chain43_HTML_table + chain44_HTML_table \
                     + chain45_HTML_table + chain46_HTML_table + chain47_HTML_table + chain48_HTML_table \
                     + chain49_HTML_table + chain50_HTML_table + chain51_HTML_table


    chain_rows = zip(chain_list_out,chain_tags_out,chain_HTML_out)

    with open('chain_tags.csv', 'w') as file:
        writer = csv.writer(file)
        for row in chain_rows:
            writer.writerow(row)
