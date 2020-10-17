

class ShaderProgram(Node):
    def __init__(self, object_id=None, parent=None):
        super().__init__(object_id=object_id, parent=parent)

    shader_modules = Plug(ShaderModule, input=True, multi=True))
    render_passes = Plug(RenderPass, output=True)
