# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

import omni.isaac.lab.sim as sim_utils
import omni.isaac.lab.actuators as acts
from omni.isaac.lab.assets.articulation import ArticulationCfg

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
            ".*_hf_joint": 0.0,  # all frontal hip joints
            "[fb]l_hs_joint": -0.785398,  # all sagittal hip joints
            "[fb]r_hs_joint": 0.785398,  # all sagittal hip joints"
            ".*_k_joint": 0.0,  # all knee joints
            ".*_a_joint": 0.0,  # all ankle joints
        },
        joint_vel={".*": 0.0},
    ),
    actuators={
        "legs": acts.DelayedPDActuatorCfg(
            joint_names_expr=[".*_joint"],
            effort_limit=45.0,
            stiffness=60.0,
            damping=1.5,
            velocity_limit=10.0,
            min_delay=0,
            max_delay=4
        ),
    },
)
"""Configuration for the Husky Beta robot."""
