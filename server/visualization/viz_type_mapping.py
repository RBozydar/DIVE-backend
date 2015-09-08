viz_types = ['tree', 'bar', 'scatter', 'hist', 'pie', 'network']

# TODO Come up with a better name for this...
types_to_viz_types = {
    'c:q': ['tree', 'pie', 'bar'],
    '[c]:q': ['tree', 'pie', 'bar'],
    'q:q': ['scatter', 'line'],
    'b:q': ['hist'],
    'c:c': ['network'],
    '[c]:q': ['network'],
    '[c]:[q]': ['network'],
    'c:[q]': ['line']
}

def get_viz_types_from_spec(spec):
    viz_types = data_types_to_viz_types[spec['type']]
    return viz_types
