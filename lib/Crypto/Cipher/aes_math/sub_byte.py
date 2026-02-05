from aes_math.gf import gf_inv
from aes_math.affine_transformation import affine_transform

def sub_byte(byte):
    return affine_transform(gf_inv(byte))
