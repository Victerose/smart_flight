#from pws import Google
from .pws import Bing as Bing

class Link:
    def get_link(company_name):
        data = Bing.search('%s book flight' % (company_name), 1, 0) 
        #print(data)
        return data
