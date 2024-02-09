from __future__ import absolute_import

# from chainer.links import batch_normalization as CBN
from chainer.links import BatchNormalization

#class BatchNormalization(CBN.BatchNormalization):
class BatchNormalization(BatchNormalization):
    def __init__(self, size, **kwargs):
        super(BatchNormalization, self).__init__(size, **kwargs)
        self.cname = "l_bn"