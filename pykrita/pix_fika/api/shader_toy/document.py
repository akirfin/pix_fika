class ShaderToyDocument(object):
    """
    .stoy ext
    "Shader"
    """
    def __init__(self):
        self._ver = "0.1"
        self._info = Info()
        self._render_passes = list()


class Info(object):
    def __init__(self):
        self._id = "MdGfzh"
        self._name = "Himalayas"
        self._description = ""
        self._username = "reinder"
        self._published = 3  # version ?
        self._flags = 32
        self._date = "1527594357"  # UTC sec ?
        self._viewed = 0
        self._likes = 0
        self._hasliked = 0
        self._tags = set()


class RenderPass(object):
    class RenderPassType(Enum):
        IMAGE = "image"
        BUFFER = "buffer"
        CUBEMAP = "cubemap"
        SOUND = "sound"
        COMMON = "common"

    IMAGE = RenderPassType.IMAGE
    BUFFER = RenderPassType.BUFFER
    CUBEMAP = RenderPassType.CUBEMAP
    SOUND = RenderPassType.SOUND

    def __init__(self):
        self._pass_type = IMAGE
        self._name = "Image"
        self._description = ""
        self._inputs = list()  # Channels
        self._outputs = list()  # ChannelRefs  37 for final frame buffer
        self._code = ""


class Input(object):
    """
    37 Used for Output image (never saved)
    """
    class InputType(Enum):
        TEXTURE_2D = "texture2D"
        TEXTURE_3D = "texture3D"
        TEXTURE_CUBE = "textureCube"
        KEYBOARD = "keyboard"
        WEBCAM = "webCam"
        MUSIC = "music"
        MICROPHONE = "microphone"
        SOUNDCLOUD = "soundcloud"
        BUFFER = "buffer"


    OUT_IMAGE = InputType.OUT_IMAGE
    BUFFER = InputType.BUFFER
    TEXTURE = InputType.TEXTURE
    CUBEMAP = InputType.CUBEMAP
    SOUND = InputType.SOUND

    def __init__(self):
        self._channel_type = OUT_IMAGE
        self._channel = 0  # why? own index?
        self._id = 37  # Used for Output image
        self._src = "/media/previz/buffer02.png"
        self._sampler = Sampler()
        self._published = 1


class Sampler(object):
    def __init__(self):
        self._vflip = True
        self._srgb = False
        self._internal = "byte"  # component type
        self._wrap = "clamp"
        self._filter = "linear"


class ChannelRef(object):
    """
    Simple Reference to Input channel
    WeakRef ?
    """
    def __init__(self):
        self._channel = 0  # why? own index?
        self._id = 259
