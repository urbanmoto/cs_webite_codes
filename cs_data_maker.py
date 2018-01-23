def cs_data_maker(csv_file):

    import csv
    import numpy as np

    with open(csv_file, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        datalist = list(datareader)    #each row is a list item

    for i in range(0,len(datalist)):   #recreate cells in array
        datalist[i] = str(datalist[i])
        datalist[i] = datalist[i].split("', '")

    URL = [None] * len(datalist)       #re-open exsisting variables
    man = [None] * len(datalist)
    model = [None] * len(datalist)
    years = [None] * len(datalist)
    tags = [None] * len(datalist)
    front_sprocket = [None] * len(datalist)
    front_sprocket_teeth = [None] * len(datalist)
    rear_sprocket = [None] * len(datalist)
    rear_sprocket_teeth = [None] * len(datalist)
    chain_type = [None] * len(datalist)
    chain_length = [None] * len(datalist)
    HTML_table_row = [None] * len(datalist)

    JTF = [None] * len(datalist)       #new variables
    JTR = [None] * len(datalist)

    for i in range(0,len(datalist)):

        URL[i] = datalist[i][0][2:]    #re-assign exsisting variables
        man[i] = datalist[i][1]
        model[i] = datalist[i][2]
        years[i] = datalist[i][3]
        tags[i] = datalist[i][4]
        front_sprocket[i] = datalist[i][5]
        front_sprocket_teeth[i] = datalist[i][6]
        rear_sprocket[i] = datalist[i][7]
        rear_sprocket_teeth[i] = datalist[i][8]
        chain_type[i] = datalist[i][9]
        chain_length[i] = datalist[i][10]
        HTML_table_row[i] = datalist[i][11][:-2]

        if front_sprocket[i] != 'TBA':
            JTF[i] = str(front_sprocket[i]) + '.' + str(front_sprocket_teeth[i])
        else:
            ''

        if rear_sprocket[i] != 'TBA':
            JTR[i] = str(rear_sprocket[i]) + '.' + str(rear_sprocket_teeth[i])
        else:
            ''

    #FRONT SPROCKETS

    JTF_np = np.ascontiguousarray(JTF, dtype=str) #use numpy to get unique vaules
    JTF_np_list = np.unique(JTF_np)

    JTF_list = [None] * len(JTF_np_list)

    for i in range(0,len(JTF_np_list)):     #give list of unique values
        JTF_list[i] = JTF_np_list[i]

    for i in range(0,len(JTF_list)):        #removes erroneous data
        try:
            if len(JTF_list[i]) >12 or len(JTF_list[i]) < 3:
                JTF_list.remove(str(JTF_list[i]))
        except:
            pass

    JTF_np_list = None                       #clear / open variable for re-use
    index = [None] * len(JTF_list)

    JTF_np_list = np.asarray(JTF_list)

    for i in range(0,len(JTF_np_list)):     #return all index positions for model tags which use the front sprocket
        index[i] = np.where(JTF_np == str(JTF_np_list[i]))

    array = [None] * len(index)             #open variables
    HTML_array = [None] * len(index)
    JTF_tags_list = [None] * len(index)
    JTF_HTML_table = [None] * len(index)

    for i in range(0,len(index)):           #put model tags into array
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]


    for i in range(0,len(array)):           #sort model tags
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

    for i in range(0,len(array)):           #make tag list for shopify
        JTF_tags_list[i] = ','.join(array[i])
        JTF_HTML_table[i] = ''.join(HTML_array[i])

    #REAR SPROCKERS

    JTR_np = np.ascontiguousarray(JTR, dtype=str) #use numpy to get unique vaules
    JTR_np_list = np.unique(JTR_np)

    JTR_list = [None] * len(JTR_np_list)

    for i in range(0,len(JTR_np_list)):     #give list of unique values
        JTR_list[i] = JTR_np_list[i]

    for i in range(0,len(JTR_list)):        #removes erroneous data
        try:
            if len(JTR_list[i]) >12 or len(JTR_list[i]) < 3:
                JTR_list.remove(str(JTR_list[i]))
        except:
            pass

    JTR_np_list = None                       #clear / open variable for re-use
    index = [None] * len(JTR_list)

    JTR_np_list = np.asarray(JTR_list)

    for i in range(0,len(JTR_np_list)):     #return all index positions for model tags which use the front sprocket
        index[i] = np.where(JTR_np == str(JTR_np_list[i]))

    array = [None] * len(index)             #open variables
    HTML_array = [None] * len(index)
    JTR_tags_list = [None] * len(index)
    JTR_HTML_table = [None] * len(index)

    for i in range(0,len(index)):           #put model tags into array
        array[i] = [None] * len(index[i][0])
        HTML_array[i] = [None] * len(index[i][0])
        for j in range(0,len(index[i][0])):
            array[i][j] = tags[index[i][0][j]]
            HTML_array[i][j] = HTML_table_row[index[i][0][j]]

    for i in range(0,len(array)):           #sort model tags
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

    for i in range(0,len(array)):           #make tag list for shopify
        JTR_tags_list[i] = ','.join(array[i])
        JTR_HTML_table[i] = ''.join(HTML_array[i])


    front_rows = zip(JTF_list,JTF_tags_list,JTF_HTML_table)

    with open('cs_front_sprocket_tags.csv', 'w') as file:
        writer = csv.writer(file)
        for row in front_rows:
            writer.writerow(row)

    rear_rows = zip(JTR_list,JTR_tags_list,JTR_HTML_table)

    with open('cs_rear_sprocket_tags.csv', 'w') as file:
        writer = csv.writer(file)
        for row in rear_rows:
            writer.writerow(row)
