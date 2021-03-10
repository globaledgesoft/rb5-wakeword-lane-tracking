import rclpy

from src.lane_tracker import LaneTracking


def main(args=None):
    rclpy.init(args=args)
    tracker = LaneTracking()
    rclpy.spin(tracker)

    tracker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
