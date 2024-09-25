schema= "Nombre, Apellido, Edad, Email"
row= "Valentina, Gomez Pereyra, 22, Valengomezp177@gmai.com"

class Str2Dic():
    def __init__(self, schema, separator=","):
        self.schema = schema.split(separator)
        self.separator = separator
    def convert(self,row):
        tmp = row.split(self.separator)
        if len(tmp) == len(self.schema):
            i = 0
            d = {}
            while i < len(tmp):
                d[self.schema[i]] = tmp[i]
                i += 1
            return d
o = Str2Dic(schema)
d = o.convert(row)

print(d)
