class RenderPass(Node):
    """
    setup for one render pass,
    shader_program & uniforms & inputs & outputs
    """

    def __init__(self, object_id=None, parent=None):
        super().__init__(object_id=object_id, parent=parent)
        self._uniform_values = dict()  # generic uniform values

    shader_program = Plug(ShaderProgram, input=True)
    uniforms = Plug(UniformsDict, input=True)
    vertex_attribs = Plug(VertexAttribPointer, input=True, multi=True)
    inputs = Plug(Texture, input=True, multi=True)
    output = Plug(FrameBuffer, output=True)  # frame buffers  # frame buffer -1 is default?

    pipelines = Plug(RenderPass, output=True)
