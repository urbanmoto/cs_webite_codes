def cs_tag_maker(csv_file):

    import csv
    from functools import reduce

    with open(csv_file, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        datalist = list(datareader)    #each row is a list item

    for i in range(0,len(datalist)):   #recreate cells in array
        datalist[i] = str(datalist[i])
        datalist[i] = datalist[i].split("', '")

    URL = [None] * len(datalist)       #re-open exsisting variables
    model = [None] * len(datalist)
    years = [None] * len(datalist)
    front_sprocket = [None] * len(datalist)
    front_sprocket_teeth = [None] * len(datalist)
    rear_sprocket = [None] * len(datalist)
    rear_sprocket_teeth = [None] * len(datalist)
    chain_type = [None] * len(datalist)
    chain_length = [None] * len(datalist)

    man = [None] * len(datalist)      #new variables
    model_iso = [None] * len(datalist)
    model_iso_cs = [None] * len(datalist)
    model_iso_cs_part = [None] * len(datalist)
    split_years = [None] * len(datalist)
    range_years = [None] * len(datalist)
    HTML_table_row = [None] * len(datalist)

    broken_URL = [None] * len(datalist)       #more variables
    broken_model = [None] * len(datalist)
    broken_model_iso_cs = [None] * len(datalist)
    broken_man = [None] * len(datalist) 
    broken_years = [None] * len(datalist)
    broken_front_sprocket = [None] * len(datalist)
    broken_front_sprocket_teeth = [None] * len(datalist)
    broken_rear_sprocket = [None] * len(datalist)
    broken_rear_sprocket_teeth = [None] * len(datalist)
    broken_chain_type = [None] * len(datalist)
    broken_chain_length = [None] * len(datalist)
    broken_HTML_table_row = [None] * len(datalist)

    for i in range(0,len(datalist)):

        URL[i] = datalist[i][0][2:]    #re-assign exsisting variables
        model[i] = datalist[i][1]
        years[i] = datalist[i][2]
        front_sprocket[i] = datalist[i][3]
        front_sprocket_teeth[i] = datalist[i][4]
        rear_sprocket[i] = datalist[i][5]
        rear_sprocket_teeth[i] = datalist[i][6]
        chain_type[i] = datalist[i][7]
        chain_length[i] = datalist[i][8][:-2]

        model[i]=model[i].replace('ADLY ','Adly_')  #isolate manufacturer names
        model[i]=model[i].replace('AEON ','Aeon_')
        model[i]=model[i].replace('Aprilia ','Aprilia_')
        model[i]=model[i].replace('Betamotor ','Betamotor_')
        model[i]=model[i].replace('BMW ','BMW_')
        model[i]=model[i].replace('Bombardier ','Bombardier_')
        model[i]=model[i].replace('Bultaco ','Bultaco_')
        model[i]=model[i].replace('Cagiva ','Cagiva_')
        model[i]=model[i].replace('CPI ', 'CPI_')
        model[i]=model[i].replace('Daelim ','Daelim_')
        model[i]=model[i].replace('Daytona ', 'Daytona_')
        model[i]=model[i].replace('Derbi ','Derbi_')
        model[i]=model[i].replace('Ducati ','Ducati_')
        model[i]=model[i].replace('Fantic ','Fantic_')
        model[i]=model[i].replace('Gas Gas ','Gas Gas_')
        model[i]=model[i].replace('Generic ','Generic_')
        model[i]=model[i].replace('Gilera ','Gilera_')
        model[i]=model[i].replace('Harley Davidson ','Harley Davidson_')
        model[i]=model[i].replace('HMZ ','HMZ_')
        model[i]=model[i].replace('Honda ','Honda_')
        model[i]=model[i].replace('Husaberg ','Husaberg_')
        model[i]=model[i].replace('Husqvarna ','Husqvarna_')
        model[i]=model[i].replace('Hyosung ','Hyosung_')
        model[i]=model[i].replace('Jincheng ','Jincheng_')
        model[i]=model[i].replace('Kawasaki ','Kawasaki_')
        model[i]=model[i].replace('Kreidler ','Kreidler_')
        model[i]=model[i].replace('KTM ','KTM_')
        model[i]=model[i].replace('Kymco ','Kymco_')
        model[i]=model[i].replace('Malaguti ','Malaguti_')
        model[i]=model[i].replace('MBK ','MBK_')
        model[i]=model[i].replace('Modenas ','Modenas_')
        model[i]=model[i].replace('Motor Hispania ','Motor Hispania_')
        model[i]=model[i].replace('MuZ ','MuZ_')
        model[i]=model[i].replace('Peugeot ','Peugeot_')
        model[i]=model[i].replace('Rieju ','Rieju_')
        model[i]=model[i].replace('Suzuki ','Suzuki_')
        model[i]=model[i].replace('Triumph ','Triumph_')
        model[i]=model[i].replace('Yamaha ','Yamaha_')

        model[i] = model[i].split('_')  #split into manufacturers and models

        man[i] = model[i][0]           #create manufacturers list
        try:
                model_iso[i] = model[i][1]     #create models list
        except:
            pass

        model_iso[i] = model_iso[i].strip()
        model_iso[i] = model_iso[i].replace('  ',' ')
        model_iso[i] = model_iso[i].replace('( ','(')
        model_iso[i] = model_iso[i].replace(' )',')')

        years[i] = years[i].replace(' to ','-')      #re-format years string
        years[i] = years[i].replace(' onwards','-')

        HTML_table_row[i] = '<tr><td>' + str(man[i]) + '</td><td>' + str(model_iso[i]) + '</td><td>' + str(years[i]) + '</td></tr>' #make HTML table rows

        #clever code to remove year model tags if bike data contains years

        model_iso_cs[i] = str(model_iso[i])

        try:
            model_iso_cs[i] = model_iso_cs[i].split(' ')
        except:
            pass

        if years[i] != '':
            for j in range(0,len(model_iso_cs[i])):
                try:
                    if model_iso_cs[i][j].find(',') != -1:
                        if model_iso_cs[i][j].find('-') != -1:
                            model_iso_cs_part[i] = model_iso_cs[i][j]
                            model_iso_cs_part[i] = model_iso_cs_part[i].split('-')
                            model_iso_cs[i][j] = model_iso_cs_part[i][0]
                        else:
                            model_iso_cs[i].remove(model_iso_cs[i][j])
                    #if model_iso_cs[i][j].find('(') != -1:
                        #if model_iso_cs[i][j].find(')') == -1:
                            #model_iso_cs[i][j] = model_iso_cs[i][j] + ')'
                except:
                    pass

        try:
            model_iso_cs[i] = ' '.join(model_iso_cs[i])
        except:
            pass

        model_iso_cs[i] = str(model_iso_cs[i])

        model_iso_cs[i] = model_iso_cs[i].replace(',',' ')      #shopify tags cannot contain commas

        split_years[i] = years[i].split('-')                    #split years into beginning and end

        try:    #take beginning and end years and make range
            if split_years[i][0].isnumeric() and split_years[i][1].isnumeric():
                range_years[i] = range(int(split_years[i][0]),(int(split_years[i][1])+1))
            else:
                range_years[i] = years[i]
        except:
            range_years[i] = years[i]

        broken_years[i] = [None] * len(range_years[i])          #assign variable the correct length

        if type(range_years[i]) is range:         #important if statement to prevent strings being split
            for j in range(0,len(range_years[i])):
                broken_years[i][j] = range_years[i][j]
        else:
            broken_years[i] = range_years[i]

        if type(broken_years[i]) != list:
            broken_years[i] = [broken_years[i]]   #make str into single item list

        broken_URL[i] = [None] * len(broken_years[i])           #assign rest of varibles correct length and shape
        broken_man[i] = [None] * len(broken_years[i])
        broken_model[i] = [None] * len(broken_years[i])
        broken_model_iso_cs[i] = [None] * len(broken_years[i])
        broken_front_sprocket[i] = [None] * len(broken_years[i])
        broken_front_sprocket_teeth[i] = [None] * len(broken_years[i])
        broken_rear_sprocket[i] = [None] * len(broken_years[i])
        broken_rear_sprocket_teeth[i] = [None] * len(broken_years[i])
        broken_chain_type[i] = [None] * len(broken_years[i])
        broken_chain_length[i] = [None] * len(broken_years[i])
        broken_HTML_table_row[i] = [None] * len(broken_years[i])
        
        for j in range(0,len(broken_years[i])):                #fill variables with data
            broken_URL[i][j] = URL[i]
            broken_man[i][j] = man[i]
            broken_model_iso_cs[i][j] = model_iso_cs[i]
            broken_model[i][j] = model_iso[i]
            broken_front_sprocket[i][j] = front_sprocket[i]
            broken_front_sprocket_teeth[i][j] = front_sprocket_teeth[i]
            broken_rear_sprocket[i][j] = rear_sprocket[i]
            broken_rear_sprocket_teeth[i][j] = rear_sprocket_teeth[i]
            broken_chain_type[i][j] = chain_type[i]
            broken_chain_length[i][j] = chain_length[i]
            broken_HTML_table_row[i][j] = HTML_table_row[i]
                       
        if type(broken_years[i]) != list:        #make str into single item list
            broken_URL[i] = [broken_URL[i]]
            broken_man[i] = [broken_man[i]]
            broken_model[i] = [broken_model[i]]
            broken_model_iso_cs[i] = [broken_model_iso_cs[i]]
            broken_front_sprocket[i] = [broken_front_sprocket[i]]
            broken_front_sprocket_teeth[i] = [broken_front_sprocket_teeth[i]]
            broken_rear_sprocket[i] = [broken_rear_sprocket[i]]
            broken_rear_sprocket_teeth[i] = [broken_rear_sprocket_teeth[i]]
            broken_chain_type[i] = [broken_chain_type[i]]
            broken_chain_length[i] = [broken_chain_length[i]]
            broken_HTML_table_row[i] = [broken_HTML_table_row[i]]
            
    years_out = reduce(lambda x,y :x+y ,broken_years)       #reduce 2d arrays to lists
    URL_out = reduce(lambda x,y :x+y ,broken_URL)
    man_out = reduce(lambda x,y :x+y ,broken_man)
    model_out = reduce(lambda x,y :x+y ,broken_model)
    model_iso_cs_out = reduce(lambda x,y :x+y ,broken_model_iso_cs)
    front_sprocket_out = reduce(lambda x,y :x+y ,broken_front_sprocket)
    front_sprocket_teeth_out = reduce(lambda x,y :x+y ,broken_front_sprocket_teeth)
    rear_sprocket_out = reduce(lambda x,y :x+y ,broken_rear_sprocket)
    rear_sprocket_teeth_out = reduce(lambda x,y :x+y ,broken_rear_sprocket_teeth)
    chain_type_out = reduce(lambda x,y :x+y ,broken_chain_type)
    chain_length_out = reduce(lambda x,y :x+y ,broken_chain_length)
    HTML_table_row_out = reduce(lambda x,y :x+y ,broken_HTML_table_row)

    tags = [None] * len(years_out)
    
    for i in range(0,len(years_out)):
        tags[i] = str(man_out[i]) + '_' + str(model_iso_cs_out[i]) + '_' +str(years_out[i])  #make shopify tags

    rows = zip(URL_out,man_out,model_out,years_out,tags,front_sprocket_out,front_sprocket_teeth_out,rear_sprocket_out,\
               rear_sprocket_teeth_out,chain_type_out,chain_length_out,HTML_table_row_out)

    with open('jt_scrap_clean_tags.csv', 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
