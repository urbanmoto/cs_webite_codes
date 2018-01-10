def jt_web_scrape_cleaner(csv_file):

    import csv

    with open(csv_file, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        datalist = list(datareader)    #each row is a list item

    for i in range(0,len(datalist)):   #recreate cells in array
        datalist[i] = str(datalist[i])
        datalist[i] = datalist[i].split(', ')

    URL = [None] * len(datalist)       #re-open exsisting variables
    model = [None] * len(datalist)
    years = [None] * len(datalist)
    front_sprocket = [None] * len(datalist)
    front_sprocket_teeth = [None] * len(datalist)
    rear_sprocket = [None] * len(datalist)
    rear_sprocket_teeth = [None] * len(datalist)
    chain_type = [None] * len(datalist)
    chain_length = [None] * len(datalist)

    for i in range(0,len(datalist)):
        
        datalist[i][0] = datalist[i][0][2:-1] #format URL field
        datalist[i][1] = datalist[i][1][3:-2] #format model field
        datalist[i][2] = datalist[i][2][2:-2] #format years field
        datalist[i][3] = datalist[i][3][1:-1] #format front_sprocket field
        datalist[i][4] = datalist[i][4][1:-1] #format front_sprocket_teeth field
        datalist[i][5] = datalist[i][5][1:-1] #format rear_sprocket field
        datalist[i][6] = datalist[i][6][1:-1] #fomat rear_sprocket_teeth field
        datalist[i][7] = datalist[i][7][1:-1] #format chain_type field
        datalist[i][8] = datalist[i][8][1:-2] #format chain_length field

        URL[i] = datalist[i][0]
        model[i] = datalist[i][1]
        years[i] = datalist[i][2]
        front_sprocket[i] = datalist[i][3]
        front_sprocket_teeth[i] = datalist[i][4]
        rear_sprocket[i] = datalist[i][5]
        rear_sprocket_teeth[i] = datalist[i][6]
        chain_type[i] = datalist[i][7]
        chain_length[i] = datalist[i][8]

        rows = zip(URL,model,years,front_sprocket,front_sprocket_teeth,\
               rear_sprocket, rear_sprocket_teeth, chain_type , chain_length)

    with open('jt_scrap_clean.csv', 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
