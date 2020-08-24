"""Toolbox for python code.

Content:
    File IO:
        import_yuv: 读取8bit yuv420p video.
    Conversion: 
        img2float32 / ndarray2img: float32或uint8输入, 自动判断类型
        rgb2ycbcr / ycbcr2rgb: 输入(..., 3)图像.
        rgb2gray / gray2rgb
        bgr2rgb / rgb2bgr
    Metrics:
        calculate_psnr
        calculate_ssim
        calculate_mse

To-do:
    yuv2rgb: 8 bit yuv 420p
    yuv2ycbcr: 8 bit yuv 420p
    ycbcr2yuv: 8 bit yuv 420p

Ref:
    xingql@buaa.edu.cn
    scikit-image: https://scikit-image.org/docs/
    mmcv
    opencv
    opencv-python

集成常用函数, 统一调用所需包, 统一命名格式.

不要重复造轮子! 了解原理即可.
"""
import numpy as np
import math
import cv2
import skimage.metrics as skm
import skimage.color as skc

# ================ File IO =============== #

def import_yuv(seq_path, h, w, tot_frm, start_frm=0, only_y=True):
    """Load Y, U, and V channels separately from a 8bit yuv420p video.
    
    Args:
        seq_path (str): .yuv (imgs) path.
        h (int): Height.
        w (int): Width.
        tot_frm (int): Total frames to be imported.
        start_frm (int): The first frame to be imported. Default 0.
        only_y (bool): Only import Y channels.

    Return:
        y_seq, u_seq, v_seq (3 channels in 3 ndarrays): Y channels, U channels, 
        V channels.

    Note:
        YUV传统上是模拟信号格式, 而YCbCr才是数字信号格式.YUV格式通常实指YCbCr文件.
        参见: https://en.wikipedia.org/wiki/YUV
    """
    # setup params
    hh, ww = h // 2, w // 2
    y_size, u_size, v_size = h * w, hh * ww, hh * ww
    blk_size = y_size + u_size + v_size
    
    # init
    y_seq = np.zeros((tot_frm, h, w), dtype=np.uint8)
    if not only_y:
        u_seq = np.zeros((tot_frm, hh, ww), dtype=np.uint8)
        v_seq = np.zeros((tot_frm, hh, ww), dtype=np.uint8)

    # read data
    with open(seq_path, 'rb') as fp:
        fp.seek(int(blk_size * start_frm), 0)  # skip frames

        for i in range(tot_frm):
            y_frm = np.fromfile(fp, dtype=np.uint8, count=y_size).reshape(h, w)
            if only_y:
                np.fromfile(fp, count=u_size)
                np.fromfile(fp, count=v_size)
            else:
                u_frm = np.fromfile(fp, dtype=np.uint8, \
                    count=u_size).reshape(hh, ww)
                v_frm = np.fromfile(fp, dtype=np.uint8, \
                    count=v_size).reshape(hh, ww)

            if only_y:
                y_seq[i, ...] = y_frm
            else:
                y_seq[i, ...], u_seq[i, ...], v_seq[i, ...] = y_frm, u_frm, v_frm

    if only_y:
        return y_seq
    else:
        return y_seq, u_seq, v_seq

# =============== Conversion =============== #

def img2float32(img):
    """Convert the type and range of the input image into np.float32 and [0, 1].

    Args:
        img (img in ndarray):
            1. np.uint8 type (of course with range [0, 255]).
            2. np.float32 type, with unknown range.

    Return:
        img (ndarray): The converted image with type of np.float32 and 
        range of [0, 1].
    """
    img_type = img.dtype
    assert img_type in (np.uint8, np.float32), (
        f'The image type should be np.float32 or np.uint8, but got {img_type}')
    
    if img_type == np.uint8:  # the range must be [0, 255]
        img = img.astype(np.float32)
        img /= 255.
    else:  # np.float32, may excess the range [0, 1]
        img = img.clip(0, 1)

    return img


def ndarray2img(ndarray):
    """Convert the type and range of the input ndarray into np.uint8 and 
    [0, 255].

    Args:
        ndarray (ndarray):
            1. np.uint8 type (of course with range [0, 255]).
            2. np.float32 type with unknown range.

    Return:
        img (img in ndarray): The converted image with type of np.uint8 and 
        range of [0, 255].
    
    
    对float32类型分情况讨论: 
        1. 如果最大值超过阈值, 则视为较黑的图像, 直接clip处理；
        2. 否则, 视为[0, 1]图像处理后的结果, 乘以255.再clip.
    
    不能直接astype, 该操作会删除小数, 不精确. 应先round, 再clip, 再转换格式.
    
    image -> img2float32 -> ndarray2img 应能准确还原.
    """
    data_type = ndarray.dtype
    assert data_type in (np.uint8, np.float32), (
        f'The data type should be np.float32 or np.uint8, but got {data_type}')

    if data_type == np.float32:
        detection_threshold = 2
        if max(ndarray) < detection_threshold:  # just excess [0, 1] slightly
            ndarray *= 255.
        else:  # almost a black picture
            pass
        img = ndarray.round()  # first round. directly astype will cut decimals
        img = img.clip(0, 255)  # or, -1 -> 255, -2 -> 254!
        img = img.astype(np.uint8)
    else:
        img = ndarray

    return img


def rgb2ycbcr(rgb_img):
    """RGB to YCbCr color space conversion.

    Args:
        rgb_img (img in ndarray): (..., 3) format.

    Return:
        ycbcr_img (img in ndarray): (..., 3) format.

    Error:
        rgb_img is not in (..., 3) format.

    Input image, not float array!

    Y is between 16 and 235.
    
    YCbCr image has the same dimensions as input RGB image.
    
    This function produces the same results as Matlab's `rgb2ycbcr` function.
    It implements the ITU-R BT.601 conversion for standard-definition
    television. See more details in
    https://en.wikipedia.org/wiki/YCbCr#ITU-R_BT.601_conversion.

    It differs from a similar function in cv2.cvtColor: `RGB <-> YCrCb`.
    In OpenCV, it implements a JPEG conversion. See more details in
    https://en.wikipedia.org/wiki/YCbCr#JPEG_conversion.
    """
    ycbcr_img = skc.rgb2ycbcr(rgb_img)
    return ycbcr_img


def ycbcr2rgb(ycbcr_img):
    """YCbCr to RGB color space conversion.

    Args:
        ycbcr_img (img in ndarray): (..., 3) format.

    Return:
        rgb_img (img in ndarray): (..., 3) format.

    Error:
        ycbcr_img is not in (..., 3) format.

    Input image, not float array!

    Y is between 16 and 235.
    
    YCbCr image has the same dimensions as input RGB image.
    
    This function produces the same results as Matlab's `ycbcr2rgb` function.
    It implements the ITU-R BT.601 conversion for standard-definition
    television. See more details in
    https://en.wikipedia.org/wiki/YCbCr#ITU-R_BT.601_conversion.

    It differs from a similar function in cv2.cvtColor: `RGB <-> YCrCb`.
    In OpenCV, it implements a JPEG conversion. See more details in
    https://en.wikipedia.org/wiki/YCbCr#JPEG_conversion.
    """
    rgb_img = skc.rgb2ycbcr(ycbcr_img)
    return rgb_img


def rgb2gray(rgb_img):
    """Compute luminance of an RGB image.

    Args:
        rgb_img (img in ndarray): (..., 3) format.

    Return:
        gray_img (single channel img in array)

    Error:
        rgb_img is not in (..., 3) format.

    Input image, not float array!

    alpha通道会被忽略.
    """
    gray_img = skc.rgb2gray(rgb_img)
    return gray_img


def gray2rgb(gray_img):
    """Create an RGB representation of a gray-level image.

    Args:
        gray_img (img in ndarray): (..., 1) or (... , ) format.

    Return:
        rgb_img (img in ndarray)
    
    Input image, not float array!

    其实还有一个alpha通道参数, 但不常用. 参见: 
    https://scikit-image.org/docs/dev/api/skimage.color.html#skimage.color.gray2rgb
    """
    rgb_img = skc.gray2rgb(gray_img, alpha=None)
    return rgb_img


def bgr2rgb(img):
    img = cv2.cvtColor(img, 'COLOR_BGR2RGB')
    return img


def rgb2bgr(img):
    img = cv2.cvtColor(img, 'COLOR_RGB2BGR')
    return img

# =============== Metrics =============== #

def calculate_psnr(img0, img1, data_range=None):
    """Calculate PSNR (Peak Signal-to-Noise Ratio).
    
    Args:
        img0 (ndarray)
        img1 (ndarray)
        data_range (int, optional): Distance between minimum and maximum 
            possible values). By default, this is estimated from the image 
            data-type.
    
    Return:
        psnr (float)
    """
    psnr = skm.peak_signal_noise_ratio(img0, img1, data_range=data_range) 
    return psnr


def calculate_ssim(img0, img1, data_range=None):
    """Calculate SSIM (Structural SIMilarity).

    Args:
        img0 (ndarray)
        img1 (ndarray)
        data_range (int, optional): Distance between minimum and maximum 
            possible values). By default, this is estimated from the image 
            data-type.
    
    Return:
        ssim (float)
    """
    ssim = skm.structural_similarity(img0, img1, data_range=data_range)
    return ssim


def calculate_mse(img0, img1):
    """Calculate MSE (Mean Square Error).

    Args:
        img0 (ndarray)
        img1 (ndarray)

    Return:
        mse (float)
    """
    mse = skm.mean_squared_error(img0, img1)
    return mse

# =============== Wasted =============== #

def import_yuv_v1(video_path, startfrm, nfs, height_frame=0,
        width_frame=0, opt_bar=False, opt_clear=False):
    """Import Y U V channels from a yuv video.

    nfs: num of frames that you need.
    startfrm: start from 0.

    return: Y, U, V, each with (nfs, height, width), [0, 255], uint8
        if startfrm excesses the file len, return [] & no error.
    """
    fp = open(video_path, 'rb')  # 0101...bytes

    # retrieve resolution info from video path
    if height_frame == 0:
        res = video_path.split("-")[2].split("_")[0]
        width_frame = int(res.split("x")[0])
        height_frame = int(res.split("x")[1])

    d0 = height_frame // 2
    d1 = width_frame // 2
    y_size = height_frame * width_frame
    u_size = d0 * d1
    v_size = d0 * d1

    # target at startfrm
    blk_size = y_size + u_size + v_size
    fp.seek(blk_size * startfrm, 0)

    # init
    y_batch = []
    u_batch = []
    v_batch = []

    # extract
    for ite_frame in range(nfs):

        if ite_frame == 0:
            tmp_c = fp.read(1)
            if tmp_c == b'':  # startfrm > the last frame
                return [], [], []
            fp.seek(-1, 1)  # offset=-1, start from the present position

        y_frame = [ord(fp.read(1)) for i in range(y_size)]  # bytes -> ascii
        y_frame = np.array(y_frame, dtype=np.uint8).reshape((height_frame, \
            width_frame))
        y_batch.append(y_frame)

        u_frame = [ord(fp.read(1)) for i in range(u_size)]
        u_frame = np.array(u_frame, dtype=np.uint8).reshape((d0, d1))
        u_batch.append(u_frame)

        v_frame = [ord(fp.read(1)) for i in range(v_size)]
        v_frame = np.array(v_frame, dtype=np.uint8).reshape((d0, d1))
        v_batch.append(v_frame)

        if opt_bar:
            print("\r<%d, %d>" % (ite_frame, nfs - 1), end="", flush=True)
    if opt_clear:
        print("\r" + 20 * " ", end="\r", flush=True)
        
    fp.close()

    y_batch = np.array(y_batch)
    u_batch = np.array(u_batch)
    v_batch = np.array(v_batch)
    return y_batch, u_batch, v_batch


def import_y_v1(video_path, height_frame, width_frame, nfs,
        startfrm, opt_bar=False, opt_clear=False):
    """Import Y channel from a yuv 420p video.
    startfrm: start from 0
    return: y_batch, (nfs * height * width), dtype=uint8
    """
    fp_data = open(video_path, 'rb')

    y_size = height_frame * width_frame
    u_size = height_frame // 2 * (width_frame // 2)
    v_size = u_size

    # target at startfrm
    blk_size = y_size + u_size + v_size
    fp_data.seek(blk_size * startfrm, 0)

    # extract
    y_batch = []
    for ite_frame in range(nfs):
        
        y_frame = [ord(fp_data.read(1)) for k in range(y_size)]
        y_frame = np.array(y_frame, dtype=np.uint8).reshape((height_frame, \
            width_frame))
        fp_data.read(u_size + v_size)  # skip u and v
        y_batch.append(y_frame)

        if opt_bar:
            print("\r<%d, %d>" % (ite_frame, nfs - 1), end="", flush=True)
    if opt_clear:
        print("\r" + 20 * " ", end="\r", flush=True)

    fp_data.close()
    
    y_batch = np.array(y_batch)
    return y_batch


def calculate_psnr_v1(img1, img2, data_range=1.):
    """Calculate PSNR (Peak Signal-to-Noise Ratio).

    Args:
        img1 (ndarray): Input image 1/2 with type of np.float32 and range of 
            [0, data_range]. No matter HWC or CHW.
        img2 (ndarray): Input image 2/2 with type of np.float32 and range of 
            [0, data_range]
    
    Return:
        float: The PSNR result (ave over all channels).

    Hint:
        If calculate PSNR between two uint8 images, first .astype(np.uint8),
            and set data_range=255..
        10 * log_10 (A / mse_ave) = 10 * [log_10 (A) - log_10 (mse_ave)]
            = 10 * log_10 (A) - 10 * log_10 [(mse_c1 + mse_c2 + mse_c3) / 3]
            = C - 10 * log_10 (mse_c1 + mse_c2 + mse_c3)
            != PSNR_ave
    """
    assert img1.shape == img2.shape, (
        f"Image shapes are different: {img1.shape} vs. {img2.shape}.")
    assert img1.dtype == np.float32, (
        f"Image 1's type {img1.dtype} != np.float32.")
    assert img2.dtype == np.float32, (
        f"Image 2's type {img2.dtype} != np.float32.")

    mse = np.mean((img1 - img2)**2, dtype=np.float32)
    if mse == 0:
        return float('inf')
    psnr = 10 * np.log10(float(data_range**2) / mse)
    return psnr


def calculate_mse_v1(img1, img2):
    """Calculate MSE (Mean Square Error).
    
    Args:
        img1 (ndarray): Input image 1/2 with type of np.float32.
        img2 (ndarray): Input image 2/2 with type of np.float32.
    
    Return:
        (float): The MSE result.
    """
    assert img1.shape == img2.shape, (
        f"Image shapes are different: {img1.shape} vs. {img2.shape}.")
    assert img1.dtype == np.float32, (
        f"Image 1's type {img1.dtype} != np.float32.")
    assert img2.dtype == np.float32, (
        f"Image 2's type {img2.dtype} != np.float32.")

    # default to average flattened array. no need to first reshape into 1D array
    return np.mean((img1 - img2)**2, dtype=np.float32)
