import numpy as np
import torch.nn as nn

from logger import Logger


class BaseModel(nn.Module):
    """
    Base class for all models
    """

    def __init__(self, config):
        super(BaseModel, self).__init__()
        self.config = config
        self.logger = Logger(self.__class__.__name__).logger

    def forward(self, *input):
        """
        Forward pass logic

        :return: Model output
        """
        raise NotImplementedError

    def summary(self):
        """
        Model summary
        """
        model_parameters = filter(lambda p: p.requires_grad, self.parameters())
        params = sum([np.prod(p.size()) for p in model_parameters])
        self.logger.info('Trainable parameters: {}'.format(params))
        self.logger.info(self)
