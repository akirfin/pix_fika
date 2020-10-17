
class ShaderModule(Node):
    class ShaderTypeFlag(IntEnum):
        VERTEX =                  0b00000001  # Vertex shader written in GLSL.
        FRAGMENT =                0b00000010  # Fragment shader written in GLSL.
        GEOMETRY =                0b00000100  # Geometry shaders written in GLSL (requires OpenGL >= 3.2 or OpenGL ES >= 3.2).
        TESSELLATION_CONTROL =    0b00001000  # Tessellation control shaders written in GLSL (requires OpenGL >= 4.0 or OpenGL ES >= 3.2).
        TESSELLATION_EVALUATION = 0b00010000  # Tessellation evaluation shaders written in GLSL (requires OpenGL >= 4.0 or OpenGL ES >= 3.2).
        COMPUTE =                 0b00100000  # Compute shaders written in GLSL (requires OpenGL >= 4.3 or OpenGL ES >= 3.1).

    def __init__(self, object_id=None, parent=None):
        super().__init__(object_id=object_id, parent=parent)
        self._shader_type = FRAGMENT
        self._code = ""

    shader_programs = Plug(ShaderProgram, output=True)
