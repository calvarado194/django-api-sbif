**PyAPI-SBIF**
=================================================
Un wrapper para el API de la Superintendencia de Bancos e Instituciones Financieras de Chile, https://api.sbif.cl/

Uso
====
```
>>> from sbif import API
>>> api = API(my-key)

>>> api.get_usd()
{u'Dolares': [{u'Fecha': u'2019-06-25', u'Valor': u'682,31'}]}
>>> api.get_usd(2019,1,4)
{u'Dolares': [{u'Fecha': u'2019-01-04', u'Valor': u'697,64'}]}
```
