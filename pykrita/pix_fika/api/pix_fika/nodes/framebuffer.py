

class Framebuffer(Node):
    """
    Render target for output.
    Can be attached to texture. (render to texture)
    """

    def __init__(self, node_id=None, parent=None):
        super().__init__(node_id=node_id, parent=parent)
        # self._attachments = list()  # target textures


    render_pass = Plug(RenderPass, input=True)
    textures = Plug(Texture, output=True)
