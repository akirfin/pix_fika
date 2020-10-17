class ShaderToyImporter(FileImporter):
    def __init__(self, parent=None):
        self.setObjectName("shader_toy_importer")


    def default_mime(self):
        return ""


    def default_ext(self):
        return "stoy"


    def read(self, stream_handle):
        pix_fika_document = json.load(stream_handle)
        return pix_fika_document
