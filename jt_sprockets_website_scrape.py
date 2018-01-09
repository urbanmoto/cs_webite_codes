def jt_web_scraper(x):

    import csv , requests, time
    from lxml import html
    from bs4 import BeautifulSoup

    max_index = x    #max = 5040

    model = [None] * max_index
    model_en = [None] * max_index
    years = [None] * max_index
    sprockets = [None] * max_index
    front_sprocket = [None] * max_index
    rear_sprocket = [None] * max_index
    paragraph_content = [None] * max_index
    front_sprocket_teeth = [None] * max_index
    rear_sprocket_teeth = [None] * max_index
    chain_length = [None] * max_index
    chain_type = [None] * max_index
    URL_out = [None] * max_index

    for i in range(0,len(model)):

        URL = 'http://www.jtsprockets.com/catalogue/model/' + str((i + 1)) + '/'
        page = requests.get(URL)
        content = BeautifulSoup(page.content, 'lxml')

        URL_out[i] = URL

        model[i] = content.h2.get_text()
        model[i] = model[i].replace('—','-')
        model[i] = str(model[i]).strip()
        model_en[i] = model[i].encode('utf-8')

        years[i] = content.findAll('div', {'class': 'yeartext'})
        years[i] =str(years[i])
        years[i] = years[i].replace('<div class="yeartext">','')
        years[i] = years[i].replace('</div>','')

        paragraph_content = content.find_all('p')
        titles = content.find_all('h3')

        if len(titles) == 3:

            front_sprocket[i] = paragraph_content[0].get_text()
            front_sprocket[i] = front_sprocket[i].replace('Part Number: ','')

            front_sprocket_teeth[i] = paragraph_content[1].get_text()
            front_sprocket_teeth[i] = front_sprocket_teeth[i].replace('Teeth: ','')

            rear_sprocket[i] = paragraph_content[3].get_text()
            rear_sprocket[i] = rear_sprocket[i].replace('Part Number: ','')

            if len(rear_sprocket[i]) <= 10:

                rear_sprocket_teeth[i] = paragraph_content[4].get_text()
                rear_sprocket_teeth[i] = rear_sprocket_teeth[i].replace('Teeth: ','')

                chain_type[i] = paragraph_content[6].get_text()
                chain_type[i] = chain_type[i].replace('Pitch: ','')

                chain_length[i] = paragraph_content[7].get_text()
                chain_length[i] = chain_length[i].replace('Length: ','')

            else:

                rear_sprocket[i] = paragraph_content[4].get_text()
                rear_sprocket[i] = rear_sprocket[i].replace('Part Number: ','')

                rear_sprocket_teeth[i] = paragraph_content[5].get_text()
                rear_sprocket_teeth[i] = rear_sprocket_teeth[i].replace('Teeth: ','')

                chain_type[i] = paragraph_content[7].get_text()
                chain_type[i] = chain_type[i].replace('Pitch: ','')

                chain_length[i] = paragraph_content[8].get_text()
                chain_length[i] = chain_length[i].replace('Length: ','')

            if len(chain_type[i]) > 3:

                chain_type[i] = paragraph_content[7].get_text()
                chain_type[i] = chain_type[i].replace('Pitch: ','')

                chain_length[i] = paragraph_content[8].get_text()
                chain_length[i] = chain_length[i].replace('Length: ','')
                
        else:

            front_sprocket[i] = paragraph_content[0].get_text()
            front_sprocket[i] = front_sprocket[i].replace('Part Number: ','')

            front_sprocket_teeth[i] = paragraph_content[1].get_text()
            front_sprocket_teeth[i] = front_sprocket_teeth[i].replace('Teeth: ','')

            rear_sprocket[i] = paragraph_content[3].get_text()
            rear_sprocket[i] = rear_sprocket[i].replace('Part Number: ','')

            if len(rear_sprocket[i]) <= 10:

                rear_sprocket_teeth[i] = paragraph_content[4].get_text()
                rear_sprocket_teeth[i] = rear_sprocket_teeth[i].replace('Teeth: ','')

                chain_type[i] = paragraph_content[9].get_text()
                chain_type[i] = chain_type[i].replace('Pitch: ','')

                chain_length[i] = paragraph_content[10].get_text()
                chain_length[i] = chain_length[i].replace('Length: ','')

            else:

                rear_sprocket[i] = paragraph_content[4].get_text()
                rear_sprocket[i] = rear_sprocket[i].replace('Part Number: ','')

                rear_sprocket_teeth[i] = paragraph_content[5].get_text()
                rear_sprocket_teeth[i] = rear_sprocket_teeth[i].replace('Teeth: ','')

                chain_type[i] = paragraph_content[10].get_text()
                chain_type[i] = chain_type[i].replace('Pitch: ','')

                if len(chain_type[i]) <= 4:

                    chain_length[i] = paragraph_content[11].get_text()
                    chain_length[i] = chain_length[i].replace('Length: ','')

                else:

                    chain_type[i] = paragraph_content[12].get_text()
                    chain_type[i] = chain_type[i].replace('Pitch: ','')

                    chain_length[i] = paragraph_content[13].get_text()
                    chain_length[i] = chain_length[i].replace('Length: ','')
                    

        time.sleep(0.1)

    rows = zip(URL_out,model_en,years,front_sprocket,front_sprocket_teeth,\
               rear_sprocket, rear_sprocket_teeth, chain_type , chain_length)

    with open('jt_scrap.csv', 'w') as file:
        writer = csv.writer(file)
        for row in rows:
            try:
                writer.writerow(row)
            except:
                print, i
