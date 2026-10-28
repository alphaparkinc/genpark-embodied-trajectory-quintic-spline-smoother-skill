# -*- coding: utf-8 -*-
"""
GenPark Physical AI Quintic Polynomial Trajectory Smoother
Standard Library only: math, typing.
Computes C2-continuous quintic trajectories satisfying (p0, v0, a0) -> (p1, v1, a1),
with analytic jerk minimization and multi-waypoint chaining.
"""

import math
from typing import Dict, List, Tuple, Any

class GenParkEmbodiedTrajectoryQuinticSplineSmoother:
    def __init__(self, default_samples: int = 50):
        self.default_samples = default_samples

    def compute_coefficients(self, p0: float, v0: float, a0: float,
                             p1: float, v1: float, a1: float, T: float) -> Tuple[float, float, float, float, float, float]:
        """
        Solves quintic polynomial s(t) = a0 + a1*t + a2*t^2 + a3*t^3 + a4*t^4 + a5*t^5
        over boundary [0, T].
        """
        if T <= 1e-6:
            raise ValueError("Trajectory segment duration T must be > 0")

        c0 = p0
        c1 = v0
        c2 = 0.5 * a0

        h = p1 - p0
        T2 = T * T
        T3 = T2 * T
        T4 = T3 * T
        T5 = T4 * T

        c3 = (20.0 * h - (8.0 * v1 + 12.0 * v0) * T - (3.0 * a0 - a1) * T2) / (2.0 * T3)
        c4 = (-30.0 * h + (14.0 * v1 + 16.0 * v0) * T + (3.0 * a0 - 2.0 * a1) * T2) / (2.0 * T4)
        c5 = (12.0 * h - 6.0 * (v1 + v0) * T + (a1 - a0) * T2) / (2.0 * T5)

        return (c0, c1, c2, c3, c4, c5)

    def evaluate_polynomial(self, coeffs: Tuple[float, float, float, float, float, float], t: float) -> Dict[str, float]:
        c0, c1, c2, c3, c4, c5 = coeffs
        t2 = t * t
        t3 = t2 * t
        t4 = t3 * t
        t5 = t4 * t

        pos = c0 + c1*t + c2*t2 + c3*t3 + c4*t4 + c5*t5
        vel = c1 + 2.0*c2*t + 3.0*c3*t2 + 4.0*c4*t3 + 5.0*c5*t4
        acc = 2.0*c2 + 6.0*c3*t + 12.0*c4*t2 + 20.0*c5*t3
        jerk = 6.0*c3 + 24.0*c4*t + 60.0*c5*t2

        return {"t": round(t, 4), "pos": round(pos, 5), "vel": round(vel, 5), "acc": round(acc, 5), "jerk": round(jerk, 5)}

    def plan_segment(self, p0: float, v0: float, a0: float,
                     p1: float, v1: float, a1: float, T: float, num_samples: int = None) -> Dict[str, Any]:
        n = num_samples or self.default_samples
        coeffs = self.compute_coefficients(p0, v0, a0, p1, v1, a1, T)

        trajectory = []
        max_vel = 0.0
        max_acc = 0.0
        max_jerk = 0.0
        jerk_squared_integral = 0.0

        dt = T / (n - 1)
        for i in range(n):
            t = min(T, i * dt)
            state = self.evaluate_polynomial(coeffs, t)
            trajectory.append(state)

            if abs(state["vel"]) > max_vel: max_vel = abs(state["vel"])
            if abs(state["acc"]) > max_acc: max_acc = abs(state["acc"])
            if abs(state["jerk"]) > max_jerk: max_jerk = abs(state["jerk"])
            jerk_squared_integral += (state["jerk"] ** 2) * dt

        return {
            "duration": T,
            "coefficients": [round(c, 6) for c in coeffs],
            "max_velocity": round(max_vel, 4),
            "max_acceleration": round(max_acc, 4),
            "max_jerk": round(max_jerk, 4),
            "total_jerk_cost": round(jerk_squared_integral, 4),
            "trajectory": trajectory
        }
