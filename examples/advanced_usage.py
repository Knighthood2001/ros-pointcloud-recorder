import logging
import time
# import sys
# sys.path.append('/home/wu/code/pythonDemo/ros_pointcloud_recorder')  # 添加项目根目录到Python路径
from ros_pointcloud_recorder import PointCloudRecorder

# 自定义日志配置
logger = logging.getLogger("CustomRecorder")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# 配置要录制的话题
topics = ['/points_raw1', '/points_raw2']

# 自定义导出路径
custom_paths = {
    '/points_raw1': './data/front_lidar',
    '/points_raw2': './data/rear_lidar'
}

# 创建录制器实例
recorder = PointCloudRecorder(
    topics=topics,
    output_dir='./recordings',  # bag文件保存路径
    bag_file='my_recording.bag',  # 自定义bag文件名
    recording_duration=5.0,
    cleanup=False,  # 保留bag文件
    logger=logger
)

# 分别控制录制流程
try:
    recorder.start_recording()
    # 可以在此处执行其他操作
    time.sleep(recorder.recording_duration)
    recorder.stop_recording()
    pcd_paths = recorder.export_pcd(custom_paths)
    
    print("导出完成:")
    for topic, path in pcd_paths.items():
        print(f"  {topic} -> {path}")
except Exception as e:
    logger.error(f"录制失败: {str(e)}")
finally:
    if not recorder.cleanup:
        logger.info(f"bag文件保留在: {recorder.bag_file}")