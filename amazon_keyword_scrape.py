
import requests 
from bs4 import BeautifulSoup

def scrape_cities(url, st):
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    rows = soup.find_all('span')[1:11]
    data = []
    for row in rows:
        tds = row.find_all('span')
        data.append([tds[1].get_text().strip(),
             int(tds[2].get_text().replace(',',''))])
    if st.startswith('new'):
        st = 'New ' + st[3:]
    st = st.title()
    return pd.DataFrame(data, np.arange(1, 11), ['', st])

scrape_cities("https://www.amazon.com/s?k=egyptian&rh=n%3A1063278&dc&qid=1617131342&rnid=2941120011&ref=sr_nr_n_1",new)
