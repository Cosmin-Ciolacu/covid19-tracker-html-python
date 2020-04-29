from browser import document, console
from browser import ajax

url = 'https://coronavirus-19-api.herokuapp.com/countries/'

def get_response(req):
  document['info'].style.display = 'flex'
  console.log('se cauta date')
  import json
  data = json.loads(req.responseText)
  console.log(data)
  cazuri_totale = data['cases']
  vindecati = data['recovered']
  decedati = data['deaths']
  cazuri_24h = data['todayCases']
  decedati_24h = data['todayDeaths']
  document['cases'].text = cazuri_totale
  document['vindecati'].text = vindecati
  document['decedati'].text = decedati
  document['cases24'].text = cazuri_24h
  document['decedati24'].text = decedati_24h



def cautare(e):
  country = document['country'].value
  #console.log(country)
  full_url = url + country 
  #console.log(full_url)
  req = ajax.ajax()
  req.open('GET', full_url, True)
  req.bind('complete', get_response)
  req.send()


document['cauta'].bind('click', cautare)

#alert("hello from python")