import os
import setuptools


here = os.path.abspath(os.path.dirname(__file__))
# Get __version__ variable
exec(open(os.path.join(here, 'pytorch_pfn_extras', '_version.py')).read())


setuptools.setup(
    name='pytorch-pfn-extras',
    version=__version__,        # NOQA
    description='Supplementary components to accelerate research and '
                'development in PyTorch.',
    author='Preferred Networks, Inc.',
    license='MIT License',
    install_requires=['numpy', 'torch'],
    extras_require={
        'test': ['pytest'],
        'tou': ['onnx'],
    },
    packages=[
        'pytorch_pfn_extras',
        'pytorch_pfn_extras.nn',
        'pytorch_pfn_extras.nn.modules',
        'pytorch_pfn_extras.tou',
        'pytorch_pfn_extras.training',
        'pytorch_pfn_extras.training.extensions',
        'pytorch_pfn_extras.training.triggers',
    ],
)
