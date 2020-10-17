class GlslSandboxExporter(FileExporter):
    def __init__(self, parent=None):
        self.setObjectName("glsl_sandbox_exporter")


    def default_mime(self):
        return ""


    def default_ext(self):
        return "frag"


    def write(self, stream_handle, pix_fika_document):
        json.dump(stream_handle, pix_fika_document)
