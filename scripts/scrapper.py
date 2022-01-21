def htmlTOdf(column_list):
    df = pd.DataFrame(columns=column_list)

    for row in tables[table_index].tbody.find_all("tr"):
        col = row.find_all("td")
        if (col != []):
            
            holde[0] = col[0].text
            holde[1] = col[1].text
            holde[2] = col[2].text.strip()
            holde[3] = col[3].text.strip() #to remove white spaces
            holde[4] = col[4].text.strip()
            df = df.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

    return df


# pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0]
# dataframe_list = pd.read_html(url, flavor='bs4'); print(len(dataframe_list)); print(dataframe_list[5]) #replace 5
# df = pd.read_html(str(tables[5]), flavor='bs4')[0]


"""
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

    print(link.get('href'))

"""

# data  = requests.get(url).text 
