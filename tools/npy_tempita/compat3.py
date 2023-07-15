import sys

__all__ = ['PY3', 'b', 'basestring_', 'bytes', 'next', 'is_unicode',
           'iteritems']

PY3 = True if sys.version_info[0] >= 3 else False

if sys.version_info[0] < 3:

    def next(obj):
        return obj.next()

    def iteritems(d, **kw):
        return d.iteritems(**kw)

    b = bytes = str
    basestring_ = basestring

else:

    def b(s):
        if isinstance(s, str):
            return s.encode('latin1')
        return bytes(s)

    def iteritems(d, **kw):
        return iter(d.items(**kw))

    next = next
    basestring_ = (bytes, str)
    bytes = bytes

text = str


def is_unicode(obj):
    return isinstance(obj, unicode) if sys.version_info[0] < 3 else isinstance(obj, str)


def coerce_text(v):
    if not isinstance(v, basestring_):
        attr = '__unicode__' if sys.version_info[0] < 3 else attr = '__str__'
        return unicode(v) if hasattr(v, attr) else return bytes(v)
    return v
