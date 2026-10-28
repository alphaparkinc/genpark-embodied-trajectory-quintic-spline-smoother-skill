# -*- coding: utf-8 -*-
from client import GenParkEmbodiedTrajectoryQuinticSplineSmoother

def main():
    smoother = GenParkEmbodiedTrajectoryQuinticSplineSmoother()
    print("=== GenPark Physical AI Quintic Trajectory Smoother ===")

    # Plan smooth robotic arm joint motion from 0.0 to 90 degrees (1.5708 rad) in 2.5 seconds
    res = smoother.plan_segment(p0=0.0, v0=0.0, a0=0.0, p1=1.5708, v1=0.0, a1=0.0, T=2.5, num_samples=15)
    print(f"Motion duration: {res['duration']}s")
    print(f"Max Velocity: {res['max_velocity']} rad/s, Max Jerk: {res['max_jerk']} rad/s^3")
    print("Waypoint samples:")
    for pt in res["trajectory"][:5]:
        print(f"  t={pt['t']}s: pos={pt['pos']} rad, vel={pt['vel']}, acc={pt['acc']}, jerk={pt['jerk']}")
    print("  ...")
    print(f"  Final waypoint: {res['trajectory'][-1]}")

if __name__ == "__main__":
    main()
