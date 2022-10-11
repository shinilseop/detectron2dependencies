from setuptools import setup, find_packages

setup(
    name='detectron2dependencies',
    packages=find_packages(),
    url='https://github.abc.com/abc/myabc',
    description='detectron2 dependencies',
    long_description=open('README.md').read(),
    install_requires=[
        "torch==1.11.0",
        "torchvision==0.12.0",
        "torchaudio==0.11.0",
        "pyyaml==5.1",
        "opencv-python==4.6.0.66",
        "detectron2==0.6",
        # "git+https://github.com/facebookresearch/detectron2.git"
    ],
    dependency_links=[
        "git+https://github.com/facebookresearch/detectron2.git",
        "https://download.pytorch.org/whl/cpu"
    ],
    include_package_data=True,
)

