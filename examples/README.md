
# 示例代码
ros_pointcloud_recorder/examples/base_usage.py运行后的结果如下：
```shell
wu@wu:~/code/pythonDemo$ /usr/bin/python3 /home/wu/code/pythonDemo/ros_pointcloud_recorder/examples/base_usage.py
2025-06-10 13:36:10,804 - PointCloudRecorder - INFO - 初始化录制器: 输出目录=./recordings, 录制时长=3.0s
2025-06-10 13:36:10,804 - PointCloudRecorder - INFO - 开始录制话题: /points_raw1, /points_raw2
2025-06-10 13:36:11,305 - PointCloudRecorder - INFO - 录制中... (时长: 3.0s)
2025-06-10 13:36:14,723 - PointCloudRecorder - INFO - 录制已停止
2025-06-10 13:36:15,223 - PointCloudRecorder - INFO - 导出话题 /points_raw1 到 ./recordings/points_raw1
2025-06-10 13:36:15,766 - PointCloudRecorder - INFO - 导出话题 /points_raw2 到 ./recordings/points_raw2
2025-06-10 13:36:16,291 - PointCloudRecorder - INFO - 已清理临时文件: ./recordings/recorded_point_clouds.bag
录制导出完成:
  /points_raw1 -> ./recordings/points_raw1
  /points_raw2 -> ./recordings/points_raw2
```

ros_pointcloud_recorder/examples/advanced_usage.py运行后的结果如下：
```shell
wu@wu:~/code/pythonDemo$ /usr/bin/python3 /home/wu/code/pythonDemo/ros_pointcloud_recorder/examples/advanced_usage.py
INFO: 初始化录制器: 输出目录=./recordings, 录制时长=5.0s
INFO: 开始录制话题: /points_raw1, /points_raw2
INFO: 录制已停止
INFO: 导出话题 /points_raw1 到 ./data/front_lidar
INFO: 导出话题 /points_raw2 到 ./data/rear_lidar
导出完成:
  /points_raw1 -> ./data/front_lidar
  /points_raw2 -> ./data/rear_lidar
INFO: Bag文件保留在: ./recordings/recorded_point_clouds.bag
```
这里的话，你可以自定义去实现log