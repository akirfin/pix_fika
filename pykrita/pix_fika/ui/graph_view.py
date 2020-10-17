from PyQt5.QtCore import (
        Qt,
        pyqtSlot as QSlot,
        pyqtSignal as QSignal,
        pyqtProperty as QProperty,
        QSize)

from PyQt5.QtGui import (
        QPainter,
        QPalette,
        QTransform)

from PyQt5.QtWidgets import (
        QWidget,
        QAbstractScrollArea)

from pix_fika.common.utils_qt import (
        create_painter,
        keep_painter)


class GraphViewport(QWidget):
    """
    graph painting widget and transform
    """
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("pix_fika_graph_viewport")
        self.setBackgroundRole(QPalette.Base)
        self.setAutoFillBackground(True)
        self._transform = QTransform()


    def graph(self):
        return self._graph


    def set_graph(self, new_graph):
        old_graph = self._graph
        if old_graph is not None:
            old_graph.node_added.disconnect(self.on_node_added)
            old_graph.node_edited.disconnect(self.on_node_edited)
            old_graph.node_removed.disconnect(self.on_node_removed)
            old_graph.edge_added.disconnect(self.on_edge_added)
            old_graph.edge_removed.disconnect(self.on_edge_removed)
        self._graph = new_graph
        if new_graph is not None:
            new_graph.node_added.connect(self.on_node_added)
            new_graph.node_edited.connect(self.on_node_edited)
            new_graph.node_removed.connect(self.on_node_removed)
            new_graph.edge_added.connect(self.on_edge_added)
            new_graph.edge_removed.connect(self.on_edge_removed)
        self.update()


    def on_node_added(self, node_id):
        node = self._graph.get_node(node_id)
        self.update(node.rect())


    def on_node_edited(self, node_id):
        node = self._graph.get_node(node_id)
        self.update(node.rect())


    def on_node_removed(self, node_id, node):
        self.update(node.rect())


    def on_edge_added(self, edge_id):
        r.union(edge.from_plug.node().rect())
        r.union(edge.to_plug.node().rect())
        self.update(r)


    def on_edge_removed(self, edge_id, edge):
        r.union(edge.from_plug.node().rect())
        r.union(edge.to_plug.node().rect())
        self.update(r)


    def on_data_about_to_reset(self):
        pass


    def on_data_reseted(self):
        self.update()


    def paintEvent(self, e):
        r = self.rect()
        is_in_view = lambda item_rect: self._transform.mapRect(item_rect).intersects(r)
        with create_painter(self):
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setTransform(self._transform)
            graph = self._graph
            draw_node = self.draw_node
            draw_edge = self.draw_edge
            for node in graph.iter_nodes():
                r = node.rect()
                if is_in_view(r):
                    with keep_painter(painter):
                        self.draw_node(painter, node)
            for edge in graph.iter_edges():
                r = edge.rect()
                if is_in_view(r):
                    with keep_painter(painter):
                        self.draw_edge(painter, edge)


    def draw_node(self, painter, node):
        painter.drawBox(node.rect())
        painter.drawText(node.text())


    def draw_edge(self, painter, edge):
        painter.drawSpline()
        # draw_start_knot
        # draw_end_knot


class GraphView(QAbstractScrollArea):
    """
    Viewport and scrollbars.
    """
    def __init__(self, parent=None):
        super(GraphView, self).__init__(parent=parent)
        self.setObjectName("pix_fika_graph_view")
        self._graph = None
        self.setupViewport(GraphViewport())


    def translate_viewport(self):
        x_pos = self.horizontalScrollBar().value()
        y_pos = self.verticalScrollBar().value()


    def update_scroll_bars(self):
        viewport_size = self.viewport().size()
        graph_size = self.graph().size()
        self.verticalScrollBar().setPageStep(graph_size.height())
        self.horizontalScrollBar().setPageStep(graph_size.width())
        self.verticalScrollBar().setRange(0, graph_size.height() - viewport_size.height())
        self.horizontalScrollBar().setRange(0, graph_size.width() - viewport_size.width())
        self.translate_viewport()


    def scrollContentsBy(self, dx, dy):
        self.translate_viewport()


    # def viewportEvent(self, e):


    def viewportSizeHint(self):
        """
        Returns the recommended size for the viewport.
        The default implementation returns viewport() -> sizeHint().
        Note that the size is just the viewport’s size,
        without any scroll bars visible.
        """
        return QSize()


    def resizeEvent(self, e):
        result = super().resizeEvent(e)
        self.update_scroll_bars()
        return result

    def fit_to_view(self, items=None, selected=None):
        if items is not None:
            pass  # fit to given
        elif selected is not None:
            pass  # fit to selected
        else:
            pass  # fit all


    def mouseMoveEvent(self, e):
        return super(GraphView, self).mouseMoveEvent(e)


    def mousePressEvent(self, e):
        return super(GraphView, self).mousePressEvent(e)


    def mouseReleaseEvent(self, e):
        return super(GraphView, self).mouseReleaseEvent(e)


    def wheelEvent(self, e):
        return super(GraphView, self).wheelEvent(e)


    def contextMenuEvent(self, e):
        return super(GraphView, self).contextMenuEvent(e)
