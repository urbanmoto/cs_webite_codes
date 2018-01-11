def cs_tag_maker(csv_file):

    import csv

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
    tags = [None] * len(datalist)

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
        model[i]=model[i].replace('Cagiva ','Cagiva_')
        model[i]=model[i].replace('CPI ', 'CPI_')
        model[i]=model[i].replace('Daelim ','Daelim_')
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

        years[i] = years[i].replace(' to ','-')      #re-format years string
        years[i] = years[i].replace(' onwards','-')

        tags[i] = str(man[i]) + '_' + str(model_iso[i]) +'_' +str(years[i])  #make shopify tags

    rows = zip(URL,man,model_iso,years,tags,front_sprocket,front_sprocket_teeth,rear_sprocket,\
    rear_sprocket_teeth,chain_type,chain_length)

    with open('jt_scrap_clean_tags.csv', 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
