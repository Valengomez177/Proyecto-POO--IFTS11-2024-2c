from Proyecto.Clases.Str2Dic import Str2Dic
from Proyecto.Clases.Custom_exceptions import SchemaError

f = open("tests/files/users.csv", "rt")
schema = f.readline().replace("\n", "")
rows = f.readlines()
dic = []

try:
    parser = Str2Dic(schema)
    for row in rows:
        r = row.replace("\n", "")
        dic.append(parser.convert(r))
    for i in dic:
        print(i)
        
except SchemaError as e:
    print("Fallo algo en el schema", e)
except AttributeError as e:
    print("Pasaron mal el parametro", e)