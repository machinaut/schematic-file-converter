from shape import Point

class Components:
    """ Container class for individual 'Component's.
    Only used for add_component and json() (export) """

    def __init__(self):
        self.components = dict()


    def add_component(self, library_id, component):
        """ Add a component to the library """
        self.components[library_id] = component


    def json(self):
        """ Copy to a new dictionary to return """
        d = dict()
        for library_id, component in self.components.items():
            d[library_id] = component.json()
        return d


class Component:
    """ The Component class represents a single kind of part (component).
    It can have multiple graphical representations (Symbols), each with
    multiple sections (Bodies).
    The 'components' of a design is basically it's library of available
    parts.  The actual placed parts on the design are 'Instances' of
    components, and reference their respective component via a unique
    library_id.
    """

    def __init__(self, name):
        self.name = name
        self.attributes = dict()
        self.symbols = list()


    def add_attribute(self, key, value):
        """ Add an attribute to a component """
        self.attributes[key] = value


    def add_symbol(self, symbol):
        """ Add a symbol to a component """
        self.symbols.append(symbol)


    def json(self):
        """ Return a component as JSON """
        return {
            "symbols": [s.json() for s in self.symbols],
            "attributes": self.attributes,
            "name": self.name
            }


class Symbol:
    """ This is a graphical representation of a Component.
    A Component can have many Symbols, and each Symbol can have
    multiple Bodies """

    def __init__(self):
        self.bodies = list()


    def add_body(self, body):
        """ Add a body to a symbol """
        self.bodies.append(body)


    def json(self):
        """ Return a symbol as JSON """
        return {"bodies":[b.json() for b in self.bodies]}


class Body:
    """ A body of a Symbol of a Component """

    def __init__(self):
        self.shapes = list()
        self.pins = list()


    def bounds(self):
        """ Return the in and max points of the bounding box around a body """
        limits = [s.bounds() for s in self.shapes + self.pins]
        xs = sum([list(b[0::2]) for b in limits], [])
        ys = sum([list(b[1::2]) for b in limits], [])
        return [Point(min(xs), min(ys)), Point(max(xs), max(ys))]


    def add_pin(self, pin):
        """ Add a pin to a symbol """
        self.pins.append(pin)


    def add_shape(self, shape):
        """ Add a shape to a symbol """
        self.shapes.append(shape)


    def json(self):
        """ Return a symbol as JSON """
        return {
            "shapes":[s.json() for s in self.shapes],
            "pins"  :[p.json() for p in self.pins]
            }


class Pin:
    """ Pins are the parts of Bodies (/symbols/components) that connect
    to nets. Basically a line segment, with a null end and a connect end
    """

    def __init__(self, pin_number, p1, p2, label=None):
        self.label = label # is a Label
        self.p1 = Point(p1) # null end
        self.p2 = Point(p2) # connect end
        self.pin_number = pin_number


    def bounds(self):
        """ Return the min and max points of a pin """
        xs = [self.p1.x, self.p2.x]
        ys = [self.p2.y, self.p2.y]
        if self.label is not None:
            xs += self.label.bounds()[0::2]
            ys += self.label.bounds()[1::2]
        return [Point(min(xs), min(ys)), Point(max(xs), max(ys))]


    def json(self):
        """ Return a pin as JSON """
        d = {
            "pin_number":self.pin_number,
            "p1":self.p1.json(),
            "p2":self.p2.json()
            }
        if self.label is not None:
            d["label"] = self.label.json()
        return d
