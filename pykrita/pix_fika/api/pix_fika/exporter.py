class PixFikaExporter(FileExporter):
    def __init__(self, parent=None):
        self.setObjectName("pix_fika__exporter")


    def default_mime(self):
        return ""


    def default_ext(self):
        return "fika"


    def write(self, stream_handle, pix_fika_document):
        json.dump(stream_handle, pix_fika_document)
