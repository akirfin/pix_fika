import os
from contextlib import contextmanager
from datetime import datetime
import time
from collections import OrderedDict as oDict

from PyQt5.QtCore import (
        Qt,
        pyqtSlot as QSlot,
        pyqtSignal as QSignal,
        pyqtProperty as QProperty
        QPointF,
        QDir,
        QFile,
        QIODevice)

from PyQt5.QtGui import (
        QOpenGLShader,
        QOpenGLShaderProgram,
        QOpenGLVersionProfile,
        QSurfaceFormat)

from PyQt5.QtWidgets import (
        QWidget,
        QVBoxLayout,
        QOpenGLWidget)


_vertex_code = """\
#version 410 core

void main(void) {
    vec2 pos;
    pos = 2.0 * vec2(gl_VertexID % 2, gl_VertexID / 2) - 1.0;
    gl_Position = vec4(pos.x, pos.y, 0.0, 1.0);
}"""


_fragment_code = """\
#version 410 core

out vec4 out_color;

void main(void) {
    vec2 n_pos;
    n_pos = gl_FragCoord.xy / vec2(800.0, 600.0);
    out_color = vec4(n_pos.x, n_pos.y, 0.0, 1.0);
}"""


def now_ms():
    return time.monotonic()


def read_file(file_path):
    file_handle = QFile(file_path)
    if file_handle.open(QIODevice.ReadOnly):
        try:
            q_byte_array = file_handle.readAll()
            return bytes(q_byte_array.data()).decode('utf-8')
        finally:
            file_handle.close()


def add_resource_path():
    this_dir = os.path.dirname(__file__)
    resource_dir = os.path.abspath(os.path.join(this_dir, "shaders"))
    if resource_dir not in QDir.searchPaths("shaders"):
        QDir.addSearchPath("shaders", resource_dir)


def texture_from_image_file(file_path):
    image = QImage(file_path)
    texture = Texture(sampler_type=gl.GL_TEXTURE_2D)
    texture.push_data(
            image_bytes=image.constBits(),
            width=image.width(),
            height=image.height(),
            components=gl.GL_RGB,  # image.components()
            component_size=gl.GL_UNSIGNED_BYTE)  # image.componentSize()
    texture.set_wrap(s_wrap=gl.GL_REPEAT, s_wrap=gl.GL_REPEAT)
    texture.set_filtering(min=gl.GL_NEAREST, mag=gl.GL_NEAREST)
    return texture


def create_key_table():
    result = oDict()
    keys = list()
    for name in dir(Qt.Key):
        attr = getattr(Qt.Key, name)
        if isinstance(attr, Qt.Key):
            keys.append(attr)
    keys.sort()
    for k in keys:
        result[k] = False
    return result


def create_native_key_table():
    result = oDict()
    keys = list()
    for name in dir(VirtualKeyCodes):
        attr = getattr(VirtualKeyCodes, name)
        if isinstance(attr, VirtualKeyCodes):
            keys.append(attr)
    keys.sort()
    for k in keys:
        result[k] = False
    return result


def update_key_texture(texture, key_table):
    data = array("B", key_table.values())
    texture.setData(data)


class Viewport(QOpenGLWidget):
    def __init__(self, parent=None):
        super(Viewport, self).__init__(parent=parent)
        self.setObjectName("pix_fika_viewport")
        self._pressed_keys = create_key_table()
        self._native_pressed_keys = create_native_key_table()
        self._mouse = QPointF()
        self._last_click = QPointF()

        add_resource_path()
        self._default_vert = read_file("shaders:shader_toy.vert")
        self._default_frag = read_file("shaders:shader_toy.frag")
        # default codes
        self._default_sound_code = read_file("shaders:default_sound.stoy")
        self._default_buffer_code = read_file("shaders:default_buffer.stoy")
        self._default_cubemap_code = read_file("shaders:default_cubemap.stoy")
        self._default_image_code = read_file("shaders:default_image.stoy")



    def get_basic_uniforms(self):
        utc = datetime.utcnow()
        year, month, day = utc.year, utc.month, utc.day
        now = now_ms()
        size = self.size()
        width, height = size.width(), size.height()
        pixel_aspect = self.devicePixelRatioF()
        mouse = self._mouse
        last_click = self._last_click
        return {"iResolution": (width, height, pixel_aspect),
                "iFrame": (self._frame_number, ),
                "iTime": (now - self._start_time, ),
                "iTimeDelta": (now - self._last_frame_time, ),
                "iDate": (year, month, day, now),
                "iMouse": (mouse.x(), height - mouse.y(), last_click.x(), last_click.y()),
                "iSampleRate": (44100.0, )}
    def set_uniforms(self,
                    shader_program,
                    iResolution=(0.0, 0.0, 1.0),
                    iFrame=(0),
                    iTime=(0.0),
                    iTimeDelta=(0.0),
                    iDate=(0.0, 0.0, 0.0, 0.0),
                    iMouse=(0.0, 0.0, 0.0, 0.0),
                    iSampleRate=(0.0)):
        shader_program.set_uniform_f("iResolution", *iResolution)
        shader_program.set_uniform_i("iFrame", *iFrame)
        shader_program.set_uniform_f("iTime", *iTime)
        shader_program.set_uniform_f("iTimeDelta", *iTimeDelta)
        shader_program.set_uniform_f("iDate", *iDate)
        shader_program.set_uniform_f("iMouse", *iMouse)
        shader_program.set_uniform_f("iSampleRate", *iSampleRate)


    def create_shader_program(self):
        vert = QOpenGLShader(QOpenGLShader.Vertex)
        vert.compileSourceCode(_vertex_code)

        frag = QOpenGLShader(QOpenGLShader.Fragment)
        frag.compileSourceCode(_fragment_code)

        shader_program = QOpenGLShaderProgram(self.context())
        shader_program.addShader(vert)
        shader_program.addShader(frag)
        shader_program.link()
        return shader_program


    def initializeGL(self):
        context = self.context()
        profile = QOpenGLVersionProfile()
        profile.setVersion(4, 1)
        profile.setProfile(QSurfaceFormat.CoreProfile)
        self.gl = gl = context.versionFunctions(profile)

        now = now_ms()
        self._frame_number = 0
        self._start_time = now
        self._last_frame_time = now
        self._shader_program = self.create_shader_program()
        self._timer_id = self.startTimer(60.0 / 1000.0)


    def paintGL(self):
        gl = self.gl
        utc = datetime.utcnow()
        year, month, day = utc.year, utc.month, utc.day
        now = now_ms()
        size = self.size()
        width, height = size.width(), size.height()
        pixel_aspect = self.devicePixelRatioF()
        mouse = self._mouse
        last_click = self._last_click
        uniforms = {
                "iResolution": (width, height, pixel_aspect),
                "iFrame": (self._frame_number, ),
                "iTime": (now - self._start_time, ),
                "iTimeDelta": (now - self._last_frame_time, ),
                "iDate": (year, month, day, now),
                "iMouse": (mouse.x(), height - mouse.y(), last_click.x(), last_click.y()),
                "iSampleRate": (44100.0, )}

        shader_program = self._shader_program
        # self.set_uniforms(shader_program, **basic_uniforms)
        # render_pass.set_inputs()
        # render_pass.set_output()
        # render_pass.set_uniforms(basic_uniforms)
        shader_program.bind()
        gl.glClearColor(0.0, 1.0, 0.0, 1.0)
        gl.glDrawArrays(gl.GL_TRIANGLE_STRIP, 0, 4)
        self._frame_number += 1
        self._last_frame_time = now


    def resizeGL(self, width, height):
        gl = self.gl
        gl.glViewport(0, 0, width, height)


    def deleteGL(self):
        print("booom!")


    def timerEvent(self, e):
        self.update()
        return super(Viewport, self).timerEvent(e)


    def wheelEvent(self, e):
        return super(Viewport, self).wheelEvent(e)


    def mousePressEvent(self, e):
        if e.buttons() & Qt.LeftButton:
            e.timestamp()
            e.modifiers()
            size = self.size()
            pos = e.localPos()
            self._last_click = QPointF(pos.x(), size.height() - pos.y())
        return super(Viewport, self).mousePressEvent(e)


    def mouseMoveEvent(self, e):
        if e.buttons() & Qt.LeftButton:
            e.timestamp()
            e.modifiers()
            size = self.size()
            pos = e.localPos()
            self._mouse = QPointF(pos.x(), size.height() - pos.y())
        return super(Viewport, self).mouseMoveEvent(e)


    def tabletEvent(self, e):
        e_type = e.type()
        if e_type == TabletMove:
            e.timestamp()
            e.pointerType()
            e.globalPosF()
            e.posF()
            e.xTilt()
            e.yTilt()
            e.pressure()
            e.modifiers()
            e.buttons()
            e.accept()
        elif e_type == TabletPress:
            e.timestamp()
            e.pointerType()
            e.globalPosF()
            e.posF()
            e.xTilt()
            e.yTilt()
            e.pressure()
            e.modifiers()
            e.buttons()
            e.accept()
        elif e_type == TabletRelease:
            e.timestamp()
            e.pointerType()
            e.globalPosF()
            e.posF()
            e.xTilt()
            e.yTilt()
            e.pressure()
            e.modifiers()
            e.buttons()
            e.accept()
        return super(Viewport, self).tabletEvent(e)


    def keyPressEvent(self, e):
        if not e.isAutoRepeat():
            e.timestamp()
            e.modifiers()
            self._pressed_keys[e.key()] = True
            self._native_pressed_keys[e.nativeVirtualKey()] = True
        return super(Viewport, self).keyPressEvent(e)


    def keyReleaseEvent(self, e):
        if not e.isAutoRepeat():
            e.timestamp()
            e.modifiers()
            self._pressed_keys[e.key()] = False
            self._native_pressed_keys[e.nativeVirtualKey()] = True
        return super(Viewport, self).keyReleaseEvent(e)


    def focusInEvent(self, e):
        return super(Viewport, self).focusInEvent(e)


    def focusOutEvent(self, e):
        """
        reset all keys if keyboard focus is lost.
        """
        for k in self._pressed_keys:
            self._pressed_keys[k] = False
        return super(Viewport, self).focusOutEvent(e)
