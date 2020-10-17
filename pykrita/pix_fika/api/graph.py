from collections import (
        OrderedDict as oDict, )

from uuid import (
        UUID,
        uuid4)

from PyQt5.QtCore import (
        Qt,
        pyqtSlot as QSlot,
        pyqtSignal as QSignal,
        pyqtProperty as QProperty,
        QObject,
        QRectF)

from pix_fika.utils_py import (
        underscore,
        uuid_cast)

from pix_fika.ordered_set import (
        OrderedSet as oSet, )


class PropertyRef(tuple):
    __slots__ = ()

    @staticmethod
    def __new__(cls, node_id, property_name):
        node_id = uuid_cast(node_id)
        property_name = str(property_name)
        return super(PropertyRef, cls).__new__(cls, (node_id, property_name))


    @classmethod
    def cast(cls, obj):
        if isinstance(obj, cls):
            return cls(
                    node_id=obj.node_id,
                    property_name=obj.property_name)
        elif isinstance(obj, str):
            obj = serializer.loads(obj)
            if not isinstance(obj, str):
                return cls.cast(obj)
        elif isinstance(obj, Mapping):
            return cls(
                    node_id=obj.get("node_id"),
                    property_name=obj.get("property_name"))
        elif isinstance(obj, Iterable):
            return cls(*tuple(obj))
        raise RuntimeError("Can not cast. (did get: {obj})".format(**locals()))


    def to_dict(self):
        return oDict([
                ("node_id", self.node_id),
                ("property_name", self.property_name)
                ])


    def get_node_id(self):
        return self[0]


    node_id = property(fget=get_node_id)


    def get_property_name(self):
        return self[1]


    property_name = property(fget=get_property_name)


    def __str__(self):
        return serializer.dumps(self)


    def __repr__(self):
        cls = type(self)
        return "{cls.__name__({self.node_id!r}, {self.property_name!r})}".format(**locals())


class Edge(tuple):
    __slots__ = ()

    @staticmethod
    def __new__(cls, from_property, to_property):
        from_property = PropertyRef.cast(from_property)
        to_property = PropertyRef.cast(to_property)
        return super(Edge, cls).__new__(cls, (from_property, to_property))


    @classmethod
    def cast(cls, obj):
        if isinstance(obj, cls):
            return cls(
                    from_property=obj.from_property,
                    to_property=obj.to_property)
        elif isinstance(obj, str):
            obj = serializer.loads(obj)
            if not isinstance(obj, str):
                return cls.cast(obj)
        elif isinstance(obj, Mapping):
            return cls(
                    from_property=obj.get("from_property"),
                    to_property=obj.get("to_property"))
        elif isinstance(obj, Iterable):
            return cls(*tuple(obj))
        raise RuntimeError("Can not cast. (did get: {obj})".format(**locals()))


    def to_dict(self):
        return oDict([
                ("from_property", self.from_property),
                ("to_property", self.to_property)
                ])


    def get_from_property(self):
        return self._from_property


    from_property = property(fget=get_from_property)


    def get_to_property(self):
        return self._to_property


    to_property = property(fget=get_to_property)


    def __str__(self):
        return serializer.dumps(self)


    def __repr__(self):
        cls = type(self)
        return "{cls.__name__({self.from_property!r}, {self.to_property!r})}".format(**locals())


class Node(QObject):
    edited = QSignal(PropertyRef)

    def __init__(self, node_id=None, rect=None, parent=None):
        super(Node, self).__init__(parent=parent)
        self._node_id = uuid4() if node_id is None else uuid_cast(node_id)
        self._rect = QRectF()
        self.setObjectName("{name}_{id_hex}".format(
                name=underscore(type(self).__name__),
                id_hex=self._node_id.hex))
        if rect is not None:
            self.set_rect(rect)


    @classmethod
    def cast(cls, obj):
        if isinstance(obj, cls):
            return cls(
                    node_id=obj.node_id,
                    rect=obj.rect())
        elif isinstance(obj, str):
            obj = serializer.loads(obj)
            if not isinstance(obj, str):
                return cls.cast(obj)
        elif isinstance(obj, Mapping):
            return cls(
                    node_id=obj.get("node_id"),
                    rect=obj.get("rect"))
        elif isinstance(obj, Iterable):
            return cls(*tuple(obj))
        raise RuntimeError("Can not cast. (did get: {obj})".format(**locals()))


    def to_dict(self):
        return oDict([
                ("node_id", self.node_id),
                ("rect", self.rect())
                ])


    @QSlot(UUID)
    def get_node_id(self):
        return self._node_id


    node_id = QProperty(UUID, fget=get_node_id)


    def get_rect(self):
        return QRectF(self._rect)


    @QSlot(QRectF)
    def set_rect(self, new_rect):
        self._rect = QRectF(new_rect)
        self.edited(self.property_ref("rect"))


    rect = QProperty(QRectF, fget=get_rect, fset=set_rect, notify=edited)


    def property_rect(self, property_name):
        r = QRectF()
        r.setWidth(5.0)
        r.setHeight(5.0)
        r.moveCenter(self._rect.center())
        return r


    def edges_from(self):
        """ Common short hand. """
        return self.parent().edges_from(self._node_id)


    def edges_to(self):
        """ Common short hand. """
        return self.parent().edges_to(self._node_id)


    def properties(self):
        meta = self.metaObject()
        for index in enumerate(meta.propertyCount()):
            meta_property = meta.property(index)
            yield meta_property.name()


    def has_property(self, property_name):
        return self.metaObject().indexOfProperty(property_name) != -1


    def property_ref(self, property_name):
        if not self.has_property(property_name):
            raise RuntimeError("Unknown property name. (did get: {property_name})".format(**locals()))
        return PropertyRef(self._node_id, property_name)


    def __hash__(self):
        return hash(self._node_id)


    def __eq__(self, other):
        if type(self) == type(other):
            return self._node_id == other.node_id
        return NotImplemented


    def __str__(self):
        return serializer.dumps(self)


    def __repr__(self):
        cls = type(self)
        return "{cls.__name__()}".format(**locals())


class Info(QObject):
    """
    Meta data about graph.
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(underscore(type(self).__name__))
        self._format_version = "0.0.1"
        self._time_stamp = utc_ms()
        self._author = ""
        self._app = "PixFika"


    @classmethod
    def cast(cls, obj):
        if isinstance(obj, cls):
            return cls(
                    format_version=obj.format_version(),
                    time_stamp=obj.time_stamp(),
                    author=obj.author(),
                    app=obj.app())
        elif isinstance(obj, str):
            obj = serializer.loads(obj)
            if not isinstance(obj, str):
                return cls.cast(obj)
        elif isinstance(obj, Mapping):
            return cls(
                    format_version=obj.get("format_version"),
                    time_stamp=obj.get("time_stamp"),
                    author=obj.get("author"),
                    app=obj.get("app"))
        elif isinstance(obj, Iterable):
            return cls(*tuple(obj))
        raise RuntimeError("Can not cast. (did get: {obj})".format(**locals()))


    def to_dict(self):
        return oDict([
                ("format_version", self.format_version()),
                ("time_stamp", self.time_stamp()),
                ("author", self.author()),
                ("app", self.app())
                ])


    def get_format_version(self):
        return self._format_version


    format_version = property(fget=get_format_version)


    def get_time_stamp(self):
        return self._time_stamp


    time_stamp = property(fget=get_time_stamp)


    def get_author(self):
        return self._author


    def set_author(self, new_author):
        self._author = "" if new_author is None else str(new_author)


    author = property(fget=get_author, fset=set_author)


    def get_app(self):
        return self._app


    def set_app(self, new_app):
        self._app = "" if new_app is None else str(new_app)


    app = property(fget=get_app, fset=set_app)


    def __str__(self):
        return serializer.dumps(self)


    def __repr__(self):
        cls = type(self)
        return ("{cls.__name__()}("
                "{self.format_version!r}, "
                "{self.time_stamp!r}, "
                "{self.author!r}, "
                "{self.app!r})"
                ).format(**locals())


class Graph(QObject, MutableSet, metaclass=MetaMeta):
    class Order(IntEnum):
        DEPTH_FIRST = 0
        BREADTH_FIRST = 1

    DEPTH_FIRST = Order.DEPTH_FIRST
    BREADTH_FIRST = Order.BREADTH_FIRST

    class Direction(IntEnum):
        UP =          0b0001
        DOWN =        0b0010
        UP_AND_DOWN = 0b0011

    UP = Direction.UP
    DOWN = Direction.DOWN
    UP_AND_DOWN = Direction.UP_AND_DOWN

    node_added = QSignal(Node)
    node_edited = QSignal(PropertyRef)
    node_removed = QSignal(Node)
    edge_added = QSignal(Edge)
    edge_removed = QSignal(Edge)

    def __init__(self, info=None, nodes=None, edges=None, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(underscore(type(self).__name__))
        self._info = Info(parent=self)
        self._nodes = oSet()
        self._edges = oSet()
        self._edges_from = dict()
        self._edges_to = dict()
        self._rect = QRectF()  # auto update. (not serialized!)
        if info is not None:
            self.set_info(info)
        if nodes is not None:
            self.update(nodes if isinstance(nodes, Mapping) else enumerate(nodes))
        if edges is not None:
            for from_property, to_property in edges:
                self.connect(PropertyRef.cast(from_property), PropertyRef.cast(to_property))


    @classmethod
    def cast(cls, obj):
        if isinstance(obj, cls):
            return cls(
                    info=obj.info(),
                    nodes=obj.items(),
                    edges=obj.edges())
        elif isinstance(obj, str):
            obj = serializer.loads(obj)
            if not isinstance(obj, str):
                return cls.cast(obj)
        elif isinstance(obj, Mapping):
            return cls(
                    info=obj.get("info"),
                    nodes=obj.get("nodes"),
                    edges=obj.get("edges"))
        elif isinstance(obj, Iterable):
            return cls(*tuple(obj))
        raise RuntimeError("Can not cast. (did get: {obj})".format(**locals()))


    def to_dict(self):
        return oDict([
                ("info", self.info()),
                ("nodes", self.items()),
                ("edges", self.edges()),
                ])


    def __len__(self):
        return len(self._nodes)


    def __iter__(self):
        return iter(self._nodes)


    def __contains__(self, node):
        return node.node_id in self._nodes


    def add(self, node):
        if node not in self:
            node_id = node.node_id
            old_parent = node.parent()
            if isinstance(old_parent, Graph):
                old_parent.discard(node)
            self._nodes.add(node)
            node.setParent(self)
            self._edges_from[node_id] = oSet()
            self._edges_to[node_id] = oSet()
            node.edited.connect(self.node_edited)
            self.node_added.emit(node_id)


    def discard(self, node):
        if node in self:
            # first remove edges to / from node
            node_id = node.node_id
            for edge in chain(
                        self._edges_from.pop(node_id, ()),
                        self._edges_to.pop(node_id, ())):
                self.disconnect(edge.from_property, edge.to_property)
            # second remove node
            node.edited.disconnect(self.node_edited)
            self._nodes.remove(node)
            if node.parent() is self:
                node.setParent(None)
            self.node_removed.emit(node)


    def edge_count(self):
        return len(self._edges)


    def edges(self):
        return iter(self._edges)


    def is_connected(self, from_property, to_property):
        edge = Edge(PropertyRef.cast(from_property), PropertyRef.cast(to_property))
        return edge in self._edges


    def add_edge(self, from_property, to_property):
        edge = Edge(PropertyRef.cast(from_property), PropertyRef.cast(to_property))
        # validate both end types.
        from_property_type = from_property.type_name
        to_property_type = to_property.type_name
        if from_property_type != to_property_type:
            raise RuntimeError((
                    "Edge property type mismatch. ("
                        "from_property type: {from_property_type}, "
                        "to_property type: {to_property_type})").format(**locals()))
        self._edges.add(adge)
        self._edges_from[edge.from_property.node_id].add(edge)
        self._edges_to[edge.to_property.node_id].add(edge)
        self.edge_added.emit(edge)


    def remove_edge(self, from_property, to_property):
        edge = Edge(PropertyRef.cast(from_property), PropertyRef.cast(to_property))
        self._edges.remove(edge)
        self._edges_from.pop(edge.from_property.node_id)
        self._edges_to.pop(edge.to_property.node_id)
        self.edge_removed.emit(edge)


    def edges_from(self, node_id):
        return iter(self._edges_from[node_id])


    def edges_to(self, node_id):
        return iter(self._edges_to[node_id])


    def traverse(self, start, propagate=UP_AND_DOWN, order=DEPTH_FIRST, max_depth=None, edge_filter=None):
        memo = set()
        stack = [(node, 0) for node in start]

        def _up_and_down(c, d):
            for e in c.to_edges():
                stack.insert(0, (e.to_property.node_id, d + 1))
            for e in c.from_edges():
                stack.insert(0, (e.from_property.node_id, d + 1))
        def _up(c, d):
            for e in c.to_edges():
                stack.insert(0, (e.to_property.node_id, d + 1))
        def _down(c, d):
            for e in c.from_edges():
                stack.insert(0, (e.from_property.node_id, d + 1))

        def _up_and_down_filter(c, d):
            for e in c.to_edges():
                if edge_filter(e):
                    stack.insert(0, (e.to_property.node_id, d + 1))
            for e in c.from_edges():
                if edge_filter(e):
                    stack.insert(0, (e.from_property.node_id, d + 1))
        def _up_filter(c, d):
            for e in c.to_edges():
                if edge_filter(e):
                    stack.insert(0, (e.to_property.node_id, d + 1))
        def _down_filter(c, d):
            for e in c.from_edges():
                if edge_filter(e):
                    stack.insert(0, (e.from_property.node_id, d + 1))

        if propagate == Direction.UP_AND_DOWN:
            propagate_func = _up_and_down if edge_filter is None else _up_and_down_filter
        elif propagate == Direction.UP:
            propagate_func = _up if edge_filter is None else _up_filter
        elif propagate == Direction.DOWN:
            propagate_func = _down if edge_filter is None else _down_filter
        else:
            raise RuntimeError("Unknown propagate. (did get: {propagate})".format(**locals()))

        if order == Order.DEPTH_FIRST:
            order_func = lambda : stack.pop(0)
        elif order == Order.BREATH_FIRST:
            order_func = lambda : stack.pop(-1)
        else:
            raise RuntimeError("Unknown order. (did get: {order})".format(**locals()))

        while stack:
            cursor, depth = order_func()
            if cursor not in memo:
                memo.add(cursor)
                yield cursor, depth
                if depth < max_depth:
                    propagate_func(cursor, depth)


    def rect(self):
        """
        bounding rect of all nodes and edges.
        """
        return self._rect


    def edge_rect(self, edge):
        """
        return bounding rect needed for edge drawing.
        """
        r = self._from_property.rect()
        r.united(self._to_node.rect())
        return r


    def __str__(self):
        return serializer.dumps(self)


    def __repr__(self):
        cls = type(self)
        return "{cls.__name__({self.nodes!r}, {self.edges!r})}".format(**locals())
