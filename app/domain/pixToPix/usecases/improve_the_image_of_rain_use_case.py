from abc import abstractmethod
from typing import Tuple

import tensorflow as tf
from PIL import Image
from fastapi import UploadFile


class ImproveImageRainUseCase(Tuple[UploadFile]):
    @abstractmethod
    def __call__(self, args: Tuple[UploadFile]):
        raise NotImplementedError()


class ImproveImageRainUseCaseImpl(ImproveImageRainUseCase):
    IMG_WIDTH = 256
    IMG_HEIGHT = 256

    def __init__(self):
        self.loaded_model = tf.saved_model.load("core/ai_models")

    def __call__(self, args: Tuple[UploadFile]):
        data, = args
        # img = tf.image.decode_jpeg(data.file)
        img = Image.open(data.file)

        input_api = tf.cast(img, tf.float32)[..., :3]
        resize_img = tf.image.resize(input_api, [self.IMG_HEIGHT, self.IMG_WIDTH])
        input_api_normalize = (resize_img / 127.5) - 1

        dimensions = tf.expand_dims(input_api_normalize, axis=0)

        model = self.loaded_model.signatures['predict1']

        result = model(dimensions)['outputs']
        img_r = (result + 1) / 2

        new_img = tf.keras.utils.array_to_img(img_r[0])

        return new_img
