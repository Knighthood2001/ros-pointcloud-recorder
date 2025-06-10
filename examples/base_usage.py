# import sys
# sys.path.append('/home/wu/code/pythonDemo/ros_pointcloud_recorder')  # 添加项目根目录到Python路径
from ros_pointcloud_recorder import PointCloudRecorder

# 配置要录制的话题
topics = ['/points_raw1', '/points_raw2']

# 创建录制器实例
recorder = PointCloudRecorder(
    topics=topics,
    output_dir='./recordings',  # bag文件保存路径
    bag_file='my_recording.bag',  # 自定义bag文件名
    recording_duration=3.0,
    cleanup=True
)

# 执行录制并导出
try:
    pcd_paths = recorder.record_and_export()
    print("录制导出完成:")
    for topic, path in pcd_paths.items():
        print(f"  {topic} -> {path}")
except Exception as e:
    print(f"录制失败: {str(e)}")