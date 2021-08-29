class DesignacaoConverter:
    regex = '[0-9]{2}\.[0-9]{2}\.[0-9]{3}'

    def to_python(self, value):
        return str(value)

    def to_url(self, value):         
        return str(value)