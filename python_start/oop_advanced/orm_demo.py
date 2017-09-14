#ORM全称“Object Relational Mapping”，即对象-关系映射
#编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。

class Field(object):
    def __init__(self,name,column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)


class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')



class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == "Model":
            return type.__new__(cls,name,bases,attrs)
        print("Found model :%s" % name)
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v, Field):
                print("Found mapping: %s==>%s" % (k, v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings
        attrs['__table__'] =name
        return type.__new__(cls,name,bases,attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self,**kw):
        super(Model,self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v.name)
            params.append("?")
            args.append(getattr(self,k,None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__,','.join(fields),','.join(params))
        print('SQL : %s ' % sql)
        print("ARGS : %s " % str(args))


class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=123,name="Micheal",email='cmr@126.com',password='123456')
u.save()