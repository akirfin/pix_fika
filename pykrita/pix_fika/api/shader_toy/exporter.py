class ShaderToyExporter(FileExporter):
    def __init__(self, parent=None):
        self.setObjectName("shader_toy_exporter")


    def default_mime(self):
        return ""


    def default_ext(self):
        return "stoy"


    def write(self, stream_handle, pix_fika_document):
        json.dump(stream_handle, pix_fika_document)
