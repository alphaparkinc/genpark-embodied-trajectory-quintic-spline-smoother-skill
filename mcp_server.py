# -*- coding: utf-8 -*-
import sys, json, math
from client import GenParkEmbodiedTrajectoryQuinticSplineSmoother

smoother = GenParkEmbodiedTrajectoryQuinticSplineSmoother()

def run_tool(name, args):
    if name == "plan_segment":
        p0 = float(args.get("p0", 0.0))
        v0 = float(args.get("v0", 0.0))
        a0 = float(args.get("a0", 0.0))
        p1 = float(args.get("p1", 1.0))
        v1 = float(args.get("v1", 0.0))
        a1 = float(args.get("a1", 0.0))
        duration = float(args.get("duration", 2.0))
        num_samples = int(args.get("num_samples", 20))
        return smoother.plan_segment(p0, v0, a0, p1, v1, a1, duration, num_samples)
    else:
        raise ValueError(f"Unknown tool: {name}")

def main():
    if "--test" in sys.argv:
        print("[TEST] Running GenPark Trajectory Quintic Spline Smoother Self-Test...")
        res = smoother.plan_segment(0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 2.0, 10)
        assert len(res["trajectory"]) == 10
        assert math.isclose(res["trajectory"][-1]["pos"], 1.0, abs_tol=1e-3)
        assert math.isclose(res["trajectory"][-1]["vel"], 0.0, abs_tol=1e-3)
        print("[TEST] All tests passed successfully!")
        return

    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = run_tool(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"jsonrpc": "2.0", "id": req.get("id"), "result": res}))
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32603, "message": str(e)}}))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
