
**2. Mathematical Formalization of Robotics Braining**

```markdown
# Document: GPGM-ROBO-0524-001-A - Robotics Braining: AI Control and Action Execution

**Version:** 1.0
**Date:** 2025-02-17
**Author:** Amedeo Pelliccia & AI Collaboration
**Status:** Draft
**Classification:** Internal / Restricted

## 1. Introduction

### 1.1 Purpose

This document formalizes the Robotics Braining (RB) module, responsible for controlling robotic systems within the GAIA AIR project, specifically for the AMPEL360XWLRGA aircraft. RB translates high-level commands from the Heuritmática framework into executable actions, ensuring precise and efficient robotic execution.

### 1.2 Scope

This document defines:

*   The observation space of the robot.
*   The robot's state space, defining its pose, position, and other relevant parameters.
*   The action space, defining the set of all possible actions the robot can perform.
*   The transition function, which dictates the dynamics of the robot in response to actions.
*   The reward function, that guides the policy.
*   The policy used to determine actions.

This document *does not* describe the specifics of the robot hardware, low-level control loops, or the integration with the Heuritmática framework (covered in a separate document: GPGM-HEUR-0524-001-A).

## 2. System Definition: RB as a Markov Decision Process (MDP)

The core of the RB system will operate as a Markov Decision Process (MDP):

```
RB = (O, S, A, P, R, γ, π)
```

Where:

*   **O:** Observation Space (See 2.1)
*   **S:** State Space (See 2.2)
*   **A:** Action Space (See 2.3)
*   **P:** Transition Function (See 2.4)
*   **R:** Reward Function (See 2.5)
*   **γ (gamma):** Discount Factor: A value between 0 and 1 that determines the importance of future rewards. Used to weight the immediate rewards vs long-term rewards.
*   **π (pi):** Policy: A function `π(s) -> a` that determines the action `a` to take in a given state `s`.  The policy *is learned* through a Reinforcement Learning Algorithm (see 3.).

## 3. Implementation with Reinforcement Learning (RL)

### 3.1 Algorithm Choice

We will utilize a model-free reinforcement learning algorithm to learn the optimal policy, adapting to the specific dynamics of the robot and its environment, which may not be easily or completely modeled.

Specifically, will implement a *Deep Q-Network (DQN)*.

### 3.2 DQN Formulation

*   **Q-Function:**  The DQN learns a Q-function, `Q(s, a)`, which estimates the expected cumulative reward of taking action `a` in state `s` and following the optimal policy thereafter. The Q-function will be approximated by a deep neural network (NN), where parameters `θ` are optimized to approximate the action-value function (`Q(s,a; θ)`).
*   **Bellman Equation:**
    *   The goal is to find the action-value function that satisfies the Bellman Equation
    ```
    Q^*(s, a) = E[r + γ * max_a' Q^*(s', a') | s, a]
    ```

    *   Where:
        *   `Q*(s, a)` is the optimal Q-function.
        *   `E[]` is the expected value operator.
        *   `r` is the immediate reward received after taking action `a` in state `s`.
        *   `γ` is the discount factor (0 <= γ <= 1).
        *   `s'` is the next state.
        *   `a'` is an action taken from the next state.
*   **Learning Process:** The learning process involves iterative updates to the neural network's weights (θ) based on experience tuples.
    *   **Experience Replay:**  Use an experience replay buffer `D = {(s_i, a_i, r_i, s'_i)}` to store experience tuples. This helps to break correlations in the training data and improve stability.
    *   **Target Network:** A separate, "target" Q-network (with parameters `θ-`) will be updated periodically with the weights from the *online* Q-network (with parameters `θ`) to stabilize the training process.
    *   **Q-Value Update Rule:** The target is calculated according to:
        ```
        y_i = r_i + γ * max_a' Q(s'_i, a'; θ-)
        ```

        *   Where `y_i` is the target value for the i-th sample in the batch.
    *   The weights of the online network are updated by minimizing the loss function:
        ```
        L(θ) = E[ (y_i - Q(s_i, a_i; θ))^2 ]
        ```
    *   **Exploration/Exploitation:** The agent uses ε-greedy exploration strategy, which involves randomly selecting an action with probability ε, or exploiting the current estimate of Q values, selecting the action that gives the highest possible reward.

## 4. Components and Functionality

### 4.1 Observation Space (O)

The observation space encompasses data received from the robot's sensors. The choice of sensors is specific to the task, where the robot will either:
- Navigate and interact with its environment, or
- Move and interact with the aircraft.

The observation space will contain the following types of data:

*   **Vision Sensors**: *Describe the Camera(s) and what data they offer:*
    *   **Example**: `o_vision = (image_width, image_height, color_code)` (pixel data: location (x, y) location and a color code).
    *   *Preprocessing:* Image data will undergo:
        *   *Object Detection:* CNNs and pre-trained model weights, trained on the dataset.
        *   *Pose Estimation:* Algorithms to determine the position and orientation of the robots with respect to components.
*   **Force/Torque Sensors:** Data from force/torque sensors:
    *   **Example:** `o_ft = (Fx, Fy, Fz, Tx, Ty, Tz)`
    *   *Preprocessing:* Raw force/torque data will undergo:
        *   *Filtering:* Kalman filter to reduce noise.
        *   *Normalization:* Scaling the force/torque values.
*   **Proximity Sensors:** Information about the distance to surrounding objects:
    *   **Example:** `o_proximity = {d1, d2, d3}` where d1, d2, d3 is the distance to the robot from other objects detected by the sensors.
    *   *Preprocessing:* Distance readings will be:
        *   *Filtered:* Median filter will be applied.
*   **IMU (Inertial Measurement Unit):** Data about the robot's orientation and acceleration:
    *   **Example:**  `o_imu = (roll, pitch, yaw, linear_acceleration, angular_velocity)`.
    *   *Preprocessing:* IMU data will be used to update the robot's position and orientation.
*   **Data Fusion:** Data from multiple sensors will be fused using Kalman filtering or other techniques to create a more comprehensive and robust understanding of the robot's state and environment.

### 4.2 State Space (S)

*   The state space `S` describes all relevant aspects of the environment and the robot's internal state. This definition needs to incorporate the observation space, but also maintain an understanding of the previous steps.

*   **State Space Definition:**

    *   **Example:** The state space for the robot arm is defined as:
        ```
        S = {x, y, z, θ1, θ2, ..., θn, vx, vy, vz, vθ1, vθ2, ..., vθn}
        ```

        where:
        *   `(x, y, z)` is the position of the end-effector.
        *   `(θ1, θ2, ..., θn)` are the angles of the *n* joints.
        *   `(vx, vy, vz)` is the velocity of the end-effector.
        *   `(vθ1, vθ2, ..., vθn)` are the angular velocities of the joints.
*   **Dimension:** *2n + 6 dimensions, where n is the number of joints*.

### 4.3 Action Space (A)

The action space defines the possible actions the robot can take.

*   **Definition:**  The action space `A` defines all possible motor commands.
    *   This can be *discrete* or *continuous*, depending on the nature of the robot's control.
    *   **Example 1 (Discrete):** If the robot has limited number of actions (e.g., `A = {move_forward, turn_left, turn_right, grasp, release}`), the action space is *discrete.*.
        ```
        A = { move_forward, move_backward, turn_left, turn_right, stop, grasp_object, release_object}
        ```
        *   The action space can be structured into motor controls (e.g. individual joint controls)
        *   Action is selected based on the Heuritmática decision function.
        *   **Structure of Actions in this case**
            *   *Motion control:* The actions are related to the movement of the robot in the 3D space.
            *   *Interaction control:* The actions are related to the interaction of the robot with an object in the 3D space.
    *   **Example 2 (Continuous):** If the actions involve setting motor speeds, it's *continuous*.
        ```
        a_t = (v1, v2, ..., vn)
        ```
        *   Where:
            *   `a_t`: the vector of motor speeds at time *t*
            *   `v1` to `vn`:  motor speeds (e.g., for a 6-DOF robot arm, the target speeds for each of the six joints)
        *   Each `v_i` will usually be bounded within some minimum and maximum value.

### 4.4 Transition Function (P)

The transition function defines how the robot's state changes in response to its actions.

*   **Formulation:** `P(s' | s, a)` represents the probability of transitioning to state `s'` given the current state `s` and action `a`.  This captures the robot's dynamics.

*   **Simplified example (Discrete Actions):**

    *   If the robot's state is a 2D position (x, y), and the action is "move forward" (`a = forward`), and the robot can only move on a grid, then:
        ```
        P((x+1, y) | (x, y), forward) = 0.8  # 80% chance to move one step forward
        P((x, y) | (x, y), forward) = 0.1    # 10% chance to stay in the same place
        P((x, y+1) | (x, y), forward) = 0.1  # 10% chance to deviate by one step
        P(s' | (x, y), forward) = 0            # for all other s'
        ```
*   **More realistic** A robot is a complex system.

    *   **Control System:** The robot's control system takes an action and actuates the motors.
    *   **Forward Kinematics:** The forward kinematic model will update the robot's position.
    *   **Inverse Dynamics:** Compute the torques for a given motion.
    *   **Uncertainty:** Include a noise model to incorporate sensor and actuator noise.

    *   **Formulation** `P(s' | s, a)` needs to model the continuous nature of the robot:

        ```
        s' = f(s, a, noise)
        ```

        *   Where `f` represents the robot's dynamics (physical model of the robot arm), and `noise` models uncertainties in the system (motor performance, sensor noise). This function is *model-based* and relies on the kinematics/dynamics of the robot.

### 4.5 Reward Function (R)

The reward function quantifies the desirability of a state transition.

*   **Formulation:** `R(s, a, s') -> ℝ`
*   **Examples:**
    *   **Reaching a Target:**  `R(s, a, s') = - ||s' - s_target||` (negative of the distance to the target location).
    *   **Avoiding Obstacles:** `R(s, a, s') = - C * distance_to_obstacle` (where `C` is a penalty).
    *   **Grasping an Object:** `R(s, a, s') = 10` if the robot successfully grasps the object, `-1` if it collides, 0 otherwise.
    *   **Maintaining Stability:** `R(s, a, s') = - k * orientation_error` (where k is a factor).

*   **Considerations:**
    *   Designing a good reward function is *crucial* for RL.  It must guide the robot towards the desired behavior.
    *   The reward function can be designed to incorporate environmental data, feedback from sensors, etc.

### 4.6 Policy (π)

The policy defines how the robot chooses actions.

*   **DQN Policy:**  With DQN, the policy is to select the action that maximizes the Q-value in the current state:

    ```
    π(s) = argmax_a ∈ A Q(s, a; θ)
    ```

    *   Where:
        *   `π(s)` the action that the agent should take in state *s*.
        *   `Q(s, a; θ)` is the Q-value function, parameterized by `θ`, which is the output of the DQN neural network
        *   The action is given by a function that returns the index.

*   **Exploration/Exploitation (ε-greedy):**
    *   Use the ε-greedy exploration strategy which balances exploration and exploitation.
    *   Select an action with a high probability of exploiting the model.
    *   Select a random action with a small probability (ε) to explore the action space.

## 5. Next Steps

1.  **Detailed Specification of Specific Components:**  Refine the details of the vision system, force/torque sensors, joint encoders, etc. (This could be split into a separate IN).
2.  **Formalization of Algorithms:** Expand this document to incorporate the code snippets.
3.  **Create a Simulation Environment:** Implement a simulation environment to test and validate the Robotics Braining framework.

```

This is a substantial and highly detailed section of the document, covering a lot of important aspects. It's a very strong foundation. The key here is to include as much detail as possible for clarity, including the equations. Well done!

