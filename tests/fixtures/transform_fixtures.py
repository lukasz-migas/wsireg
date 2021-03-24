import pytest
import numpy as np


@pytest.fixture
def complex_transform():
    return {
        'initial': [
            {
                'Transform': ['EulerTransform'],
                'NumberOfParameters': ['3'],
                'TransformParameters': [
                    '1.5707963267948966',
                    '601.5749999999998',
                    '-601.5749999999998',
                ],
                'InitialTransformParametersFileName': ['NoInitialTransform'],
                'HowToCombineTransforms': ['Compose'],
                'FixedImageDimension': ['2'],
                'MovingImageDimension': ['2'],
                'FixedInternalImagePixelType': ['float'],
                'MovingInternalImagePixelType': ['float'],
                'Size': ['6769', '7386'],
                'Index': ['0', '0'],
                'Spacing': ['1.95', '1.95'],
                'Origin': ['0.0000', '0.0000'],
                'Direction': [
                    '1.0000000000',
                    '0.0000000000',
                    '0.0000000000',
                    '1.0000000000',
                ],
                'UseDirectionCosines': ['true'],
                'CenterOfRotationPoint': ['6598.8', '7200.375'],
                'ResampleInterpolator': ['FinalNearestNeighborInterpolator'],
                'Resampler': ['DefaultResampler'],
                'DefaultPixelValue': ['0.000000'],
                'ResultImageFormat': ['mha'],
                'ResultImagePixelType': ['float'],
                'CompressResultImage': ['true'],
            },
            {
                'Transform': ['AffineTransform'],
                'NumberOfParameters': ['6'],
                'TransformParameters': ['-1', '0', '0', '1', '0', '0'],
                'InitialTransformParametersFileName': ['NoInitialTransform'],
                'HowToCombineTransforms': ['Compose'],
                'FixedImageDimension': ['2'],
                'MovingImageDimension': ['2'],
                'FixedInternalImagePixelType': ['float'],
                'MovingInternalImagePixelType': ['float'],
                'Size': ['6769', '7386'],
                'Index': ['0', '0'],
                'Spacing': ['1.95', '1.95'],
                'Origin': ['0.0000', '0.0000'],
                'Direction': [
                    '1.0000000000',
                    '0.0000000000',
                    '0.0000000000',
                    '1.0000000000',
                ],
                'UseDirectionCosines': ['true'],
                'CenterOfRotationPoint': ['6598.8', '7200.375'],
                'ResampleInterpolator': ['FinalNearestNeighborInterpolator'],
                'Resampler': ['DefaultResampler'],
                'DefaultPixelValue': ['0.000000'],
                'ResultImageFormat': ['mha'],
                'ResultImagePixelType': ['float'],
                'CompressResultImage': ['true'],
            },
        ],
        '0': [
            {
                'CenterOfRotationPoint': ['6622.2', '7784.4'],
                'CompressResultImage': ['true'],
                'DefaultPixelValue': ['0'],
                'Direction': ['1', '0', '0', '1'],
                'FixedImageDimension': ['2'],
                'FixedInternalImagePixelType': ['float'],
                'HowToCombineTransforms': ['Compose'],
                'Index': ['0', '0'],
                'InitialTransformParametersFileName': ['NoInitialTransform'],
                'MovingImageDimension': ['2'],
                'MovingInternalImagePixelType': ['float'],
                'NumberOfParameters': ['3'],
                'Origin': ['0', '0'],
                'ResampleInterpolator': ['FinalNearestNeighborInterpolator'],
                'Resampler': ['DefaultResampler'],
                'ResultImageFormat': ['mha'],
                'ResultImagePixelType': ['float'],
                'Size': ['6793', '7985'],
                'Spacing': ['1.95', '1.95'],
                'Transform': ['EulerTransform'],
                'TransformParameters': [
                    '-0.08284214564408873',
                    '-1306.3427228105772',
                    '-991.9182706690468',
                ],
                'UseDirectionCosines': ['true'],
            },
            {
                'BSplineTransformSplineOrder': ['3'],
                'CompressResultImage': ['true'],
                'DefaultPixelValue': ['0'],
                'Direction': ['1', '0', '0', '1'],
                'FixedImageDimension': ['2'],
                'FixedInternalImagePixelType': ['float'],
                'GridDirection': ['1', '0', '0', '1'],
                'GridIndex': ['0', '0'],
                'GridOrigin': ['-2067.5640452749403', '-1636.5330828131607'],
                'GridSize': ['136', '159'],
                'GridSpacing': ['109.38401959206463', '106.69639002714067'],
                'HowToCombineTransforms': ['Compose'],
                'Index': ['0', '0'],
                'InitialTransformParametersFileName': ['0'],
                'MovingImageDimension': ['2'],
                'MovingInternalImagePixelType': ['float'],
                'NumberOfParameters': ['43248'],
                'Origin': ['0', '0'],
                'ResampleInterpolator': ['FinalNearestNeighborInterpolator'],
                'Resampler': ['DefaultResampler'],
                'ResultImageFormat': ['mha'],
                'ResultImagePixelType': ['float'],
                'Size': ['1024', '1024'],
                'Spacing': ['1.95', '1.95'],
                'Transform': ['BSplineTransform'],
                'TransformParameters': np.random.random((43248,)).tolist(),
                'UseCyclicTransform': ['false'],
                'UseDirectionCosines': ['true'],
            },
        ],
        '1': [
            {
                'CenterOfRotationPoint': ['5559', '7609'],
                'CompressResultImage': ['true'],
                'DefaultPixelValue': ['0'],
                'Direction': ['1', '0', '0', '1'],
                'FixedImageDimension': ['2'],
                'FixedInternalImagePixelType': ['float'],
                'HowToCombineTransforms': ['Compose'],
                'Index': ['0', '0'],
                'InitialTransformParametersFileName': ['NoInitialTransform'],
                'MovingImageDimension': ['2'],
                'MovingInternalImagePixelType': ['float'],
                'NumberOfParameters': ['3'],
                'Origin': ['0', '0'],
                'ResampleInterpolator': ['FinalNearestNeighborInterpolator'],
                'Resampler': ['DefaultResampler'],
                'ResultImageFormat': ['mha'],
                'ResultImagePixelType': ['float'],
                'Size': ['1024', '1024'],
                'Spacing': ['2', '2'],
                'Transform': ['EulerTransform'],
                'TransformParameters': [
                    '-0.0042257214326670706',
                    '1485.2882969318628',
                    '1562.9184348320616',
                ],
                'UseDirectionCosines': ['true'],
            },
            {
                'CenterOfRotationPoint': [
                    '7044.288296931862',
                    '9171.918434832063',
                ],
                'CompressResultImage': ['true'],
                'DefaultPixelValue': ['0'],
                'Direction': ['1', '0', '0', '1'],
                'FixedImageDimension': ['2'],
                'FixedInternalImagePixelType': ['float'],
                'HowToCombineTransforms': ['Compose'],
                'Index': ['0', '0'],
                'InitialTransformParametersFileName': ['0'],
                'MovingImageDimension': ['2'],
                'MovingInternalImagePixelType': ['float'],
                'NumberOfParameters': ['6'],
                'Origin': ['0', '0'],
                'ResampleInterpolator': ['FinalNearestNeighborInterpolator'],
                'Resampler': ['DefaultResampler'],
                'ResultImageFormat': ['mha'],
                'ResultImagePixelType': ['float'],
                'Size': ['1024', '1024'],
                'Spacing': ['2', '2'],
                'Transform': ['AffineTransform'],
                'TransformParameters': [
                    '0.9950415227069288',
                    '-0.00010257497254207552',
                    '-0.0011168508123054915',
                    '0.994578583104989',
                    '0.42502362300245433',
                    '-7.2389671174396275',
                ],
                'UseDirectionCosines': ['true'],
            },
        ],
    }
