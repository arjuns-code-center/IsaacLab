# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import DelayedPDActuatorCfg, RemotizedPDActuatorCfg
from omni.isaac.lab.assets.articulation import ArticulationCfg
from omni.isaac.lab.utils.assets import ISAAC_NUCLEUS_DIR

##
# Configuration
##

HUSKY_B_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"/home/siliconsynapse/Desktop/SiliconSynapse_Research/husky_beta/models/huskyb/huskyb.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            retain_accelerations=False,
            linear_damping=0.0,
            angular_damping=0.0,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=1.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=4, solver_velocity_iteration_count=0
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.5),
        joint_pos={
            "[fb]l_hf_joint": 0.0,  # all frontal left hip joints
            "[fb]r_hf_joint": 0.0,  # all frontal right hip joints
            ".*_hs_joint": -0.785398,  # all sagittal hip joints
            ".*_k_joint": 0.0,  # all knee joints
            ".*_a_joint": 0.0,  # all ankle joints
        },
        joint_vel={".*": 0.0},
    ),
    actuators={
        "husky_hip_frontal": DelayedPDActuatorCfg(
            joint_names_expr=[".*_hf_joint"],
            effort_limit=45.0,
            stiffness=60.0,
            damping=1.5,
            min_delay=0,  # physics time steps (min: 2.0*0=0.0ms)
            max_delay=4,  # physics time steps (max: 2.0*4=8.0ms)
        ),
        "husky_hip_sagittal": DelayedPDActuatorCfg(
            joint_names_expr=[".*_hs_joint"],
            effort_limit=45.0,
            stiffness=60.0,
            damping=1.5,
            min_delay=0,  # physics time steps (min: 2.0*0=0.0ms)
            max_delay=4,  # physics time steps (max: 2.0*4=8.0ms)
        ),
        "husky_knee": DelayedPDActuatorCfg(
            joint_names_expr=[".*_k_joint"],
            effort_limit=45.0,
            stiffness=60.0,
            damping=1.5,
            min_delay=0,  # physics time steps (min: 2.0*0=0.0ms)
            max_delay=4,  # physics time steps (max: 2.0*4=8.0ms)
        ),
        "husky_ankle": DelayedPDActuatorCfg(
            joint_names_expr=[".*_a_joint"],
            effort_limit=45.0,
            stiffness=60.0,
            damping=1.5,
            min_delay=0,  # physics time steps (min: 2.0*0=0.0ms)
            max_delay=4,  # physics time steps (max: 2.0*4=8.0ms)
        ),
    },
)
"""Configuration for the Boston Dynamics Spot robot."""
