from ROAR_simulation.carla_client.settings import CarlaSettings
from ROAR_simulation.carla_client.carla_runner import CarlaRunner
import logging
from ROAR_simulation.roar_autonomous_system.agent_module.waypoint_following_agent import WaypointFollowingAgent
from ROAR_simulation.roar_autonomous_system.agent_module.purpursuit_agent import PurePursuitAgent
from pathlib import Path
import numpy as np

def main():
    log_level = logging.DEBUG
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=log_level)
    logging.getLogger("matplotlib").setLevel(logging.WARNING)
    settings = CarlaSettings()
    np.set_printoptions(suppress=True)

    try:
        carla_runner = CarlaRunner(carla_settings=settings)
        my_vehicle = carla_runner.set_carla_world()
        # agent = PurePursuitAgent(vehicle=my_vehicle, route_file_path=Path(settings.waypoint_file_path))

        # agent = SemanticSegmentationAgent(
        #     vehicle=my_vehicle,
        #     front_depth_camera=settings.front_depth_cam,
        # )
        #agent获取车辆要跟踪的路径，只是沿预定轨迹运行，不包含与来往车辆的交互
        agent = WaypointFollowingAgent(vehicle=my_vehicle,
                                       front_depth_camera=settings.front_depth_cam,
                                       front_rgb_camera=settings.front_rgb_cam,
                                       rear_rgb_camera=settings.rear_rgb_cam,
                                       route_file_path=Path(settings.waypoint_file_path),
                                       target_speed=100)
        #use_manual_control= True就可以手动控制车辆左右移动
        carla_runner.start_game_loop(agent=agent, use_manual_control=False)
    except Exception as e:
        print(f"ERROR: Something bad happened. Safely exiting. Error:{e}")


if __name__ == '__main__':
    main()


