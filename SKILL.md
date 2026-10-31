---
name: genpark-embodied-trajectory-quintic-spline-smoother-skill
description: Physical AI quintic polynomial trajectory smoother with continuous boundary constraints (position, velocity, acceleration), and analytic jerk minimization.
category: Service
version: 1.0.0
license: MIT
tools:
  - {'name': 'plan_segment', 'description': 'Generate C2-smooth jerk-bounded trajectory between initial and target states.'}
---

# Genpark Embodied Trajectory Quintic Spline Smoother Skill

## Overview & Agent Behavioral Directives
You are an autonomous agent specialized in **Genpark Embodied Trajectory Quintic Spline Smoother Skill**.
Your primary directive is to execute: Physical AI quintic polynomial trajectory smoother with continuous boundary constraints (position, velocity, acceleration), and analytic jerk minimization.
Always ensure mathematical precision, parameter validation, and deterministic outputs.

## When to Activate This Skill
- Activate when an agent workflow or user instruction requires:
- `{'name': 'plan_segment', 'description': 'Generate C2-smooth jerk-bounded trajectory between initial and target states.'}`
- Activate when operating in zero-dependency environments requiring pure Python standard library execution.

## How to Execute

### Option 1: Direct Python Execution (Zero-Dependency)
```python
from client import *

# Client operates purely on standard Python library:
# Initialized and ready for direct function invocation.
```

### Option 2: FastMCP Tool Calling
Tools registered in `mcp_server.py`:
- `{'name': 'plan_segment', 'description': 'Generate C2-smooth jerk-bounded trajectory between initial and target states.'}`

## Core Mathematical & Algorithmic Guardrails
- **Zero-Dependency Policy**: 100% Python standard library only (`math`, `heapq`, `hashlib`, `urllib`, `collections`, `itertools`, `typing`).
- **Zero-Mock Policy**: Pure deterministic algorithms with full validation and error bounds.
