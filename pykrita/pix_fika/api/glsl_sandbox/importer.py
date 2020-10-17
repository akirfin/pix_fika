class GlslSandboxImporter(FileImporter):
    def __init__(self, parent=None):
        self.setObjectName("glsl_sandbox_importer")


    def default_mime(self):
        return ""


    def default_ext(self):
        return "frag"


    def read(self, stream_handle):
        pix_fika_document = json.load(stream_handle)
        return pix_fika_document
