
class Texture(Node):
    """
    input for render program and/or output target for framebuffer
    """
    class SamplerType(Enum):
        TEXTURE_1D = "texture_1d"
        TEXTURE_2D = "texture_2d"
        TEXTURE_3D = "texture_3d"
        TEXTURE_CUBE_MAP = "texture_cube_map"

    class Warp(Enum):
        CLAMP = "clamp"
        REPEAT = "repeat"

    class MinFilter(Enum):
        NEAREST = "nearest"
        LINEAR = "linear"
        NEAREST_MIPMAP_NEAREST = "nearest_mipmap_nearest"
        NEAREST_MIPMAP_LINEAR = "nearest_mipmap_linear"
        LINEAR_MIPMAP_NEAREST = "linear_mipmap_nearest"
        LINEAR_MIPMAP_LINEAR = "linear_mipmap_linear"

    class MagFilter(Enum):
        NEAREST = "nearest"
        LINEAR = "linear"

    def __init__(self, object_id=None, parent=None):
        super().__init__(object_id=object_id, parent=parent)
        self._source_media = UrlMedia() | SoundCloudMedia() | CameraMedia() | MicMedia()
        self._sampler_type = TEXTURE_2D
        self._pixel_format =
        self._pixel_type =
        self._wrap_s = REPEAT
        self._wrap_t = REPEAT
        self._wrap_r = REPEAT
        self._min_filter = LINEAR
        self._mag_filter = LINEAR
        self._generate_mipmap = False  # glGenerateMipmap
        self._mipmap_dirty = True

    frame_buffer = Plug(FrameBuffer, input=True)
    render_passes = Plug(RenderPass, output=True)
