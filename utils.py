#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 20:31:06 2023

@author: zxc703
Modified to conform to Linter and Typing standards
"""

from typing import Any
import numpy as np
import numpy.typing as npt

# The simulator type is a runtime defined class, thus not really capable of type hinting it
Simulator = type[Any]
Handle = type[Any]


class GridMap:
    """
    Class to handle the Grid of the World. Handles obstacles and coordinates throughout the world.
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(
        self,
        sim: Simulator,
        world_size: float,
        name: str = "/world_camera",
        robot_name: str = "/PioneerP3DX",
    ):
        """
        Parameters
        ----------
        sim : TYPE
            DESCRIPTION.
        world_size : TYPE
            DESCRIPTION.
        name : TYPE, optional
            DESCRIPTION. The default is "/world_camera".
        robot_name : TYPE, optional
            DESCRIPTION. The default is "/PioneerP3DX".

        Returns
        -------
        None.

        """

        self.handle = sim.getObjectHandle(name)
        robot_handle = sim.getObjectHandle(robot_name)
        robot_pos = sim.getObjectPosition(robot_handle, -1)
        sim.setObjectPosition(robot_handle, -1, (100, 100, 100))
        self.image, self.resolution = sim.getVisionSensorImg(self.handle, 1)
        sim.setObjectPosition(robot_handle, -1, robot_pos)
        self.gridmap = np.array(bytearray(self.image), dtype="uint8").reshape(
            self.resolution[0], self.resolution[1]
        )

        self.world_size = world_size
        self.scaling = world_size / self.resolution[0]
        self.offset = np.array([self.resolution[0] / 2, self.resolution[1] / 2, 0])
        self.norm_map: npt.NDArray[Any] = np.array([])

    def inflate_obstacles(
        self, num_iter: int = 1, obs_thresh: int = 100, infl_val: int = 99
    ) -> npt.NDArray[Any]:
        """
        Parameters
        ----------
        num_iter : int, optional
        obs_thresh : int, optional
        infl_val : int, optional

        Returns
        ----------
        numpy.ndarray
        """

        rows = self.gridmap.shape[0]
        cols = self.gridmap.shape[1]
        inflated_grid = np.copy(self.gridmap)

        # Define the possible movements (up, down, left, right, and diagonals)
        movements = [
            (0, -1),  # Up
            (0, 1),  # Down
            (-1, 0),  # Left
            (1, 0),  # Right
            (-1, -1),  # Diagonal: Up-Left
            (-1, 1),  # Diagonal: Up-Right
            (1, -1),  # Diagonal: Down-Left
            (1, 1),  # Diagonal: Down-Right
        ]

        # pylint: disable=too-many-nested-blocks
        # Iterate through the grid
        for _ in range(num_iter):
            inflated_temp = np.copy(inflated_grid)
            for row in range(rows):
                for col in range(cols):
                    if inflated_grid[row][col] < obs_thresh:  # Found an obstacle
                        for move in movements:  # Inflate the obstacle
                            new_row = row + move[0]
                            new_col = col + move[1]
                            if (
                                0 <= new_row < rows
                                and 0 <= new_col < cols
                                and inflated_grid[new_row][new_col] > 200
                            ):
                                inflated_temp[new_row][new_col] = infl_val
            inflated_grid = np.copy(inflated_temp)
            self.gridmap = np.copy(inflated_grid)

        return self.gridmap

    def get_grid_coords(self, point_xyz: list[float]) -> Any:
        """
        Parameters
        ----------
        point_xyz : TYPE
        """
        try:
            pos = np.round(np.array(point_xyz) / self.scaling + self.offset).astype(
                int
            )[:, 0:2]
        # pylint: disable=bare-except
        except:
            pos = np.round(np.array(point_xyz) / self.scaling + self.offset).astype(
                int
            )[0:2]

        return pos

    def get_world_coords(self, point_xyz: npt.NDArray[Any]) -> npt.NDArray[Any]:
        """
        Parameters
        ----------
        point_xyz : TYPE
        """
        pos: npt.NDArray[Any] = (np.array(point_xyz) - self.offset) * self.scaling

        return pos

    def normalize_map(self) -> None:
        """
        Parameters
        ----------
        None
        """
        gridmap_temp = np.copy(self.gridmap)
        gridmap_temp[gridmap_temp > 99] = 255
        self.norm_map = (gridmap_temp / 255).astype(int)
        self.norm_map[self.norm_map == 0] = 3  # temporarily assign obstacles as 3
        self.norm_map[self.norm_map == 1] = 0  # set free space to 0s
        self.norm_map[self.norm_map == 3] = 1  # convert obstacle back into 1s


def generate_path_from_trace(
    sim: Simulator, trace_path: npt.NDArray[Any], num_smoothing_points: int = 100
) -> npt.NDArray[Any]:
    """
    Generates a simulation path from a given trace path.

    Parameters
    ----------
    sim : Simulator
        Handle to the simulation object.
    trace_path : numpy.ndarray
        The trace path in world coordinates. It must be of shape Nx3.
    num_smoothing_points : int, optional
        The number of points used for smoothing the generated path. Default is 100.

    Returns
    -------
    numpy.ndarray
        An array representing the generated path in the simulation environment. The array
        has shape (M, 7), where M is the total number of points and each row contains
        [x, y, z, vx, vy, vz, t], representing position (x, y, z), velocity (vx, vy, vz),
        and time (t) information.

    """

    n, _ = trace_path.shape

    trace_path = np.hstack((trace_path, np.zeros((n, 3)), np.ones((n, 1))))

    path = np.array(trace_path).astype(float)
    path_handle = sim.createPath(
        list(path.reshape(-1)), 16, num_smoothing_points, 1.0, 0, [1.0, 0.0, 0.0]
    )
    path_data = sim.unpackDoubleTable(sim.readCustomDataBlock(path_handle, "PATH"))
    path_data_array = np.array(path_data).reshape((-1, 7))

    return path_data_array


def execute_path(
    path_data_array: npt.NDArray[Any],
    sim: Simulator,
    trackpoint_handle: Handle,
    robot_handle: Handle,
    thresh: float = 0.1,
) -> None:
    """
    Parameters
    ----------
    path_data_array : TYPE
        The array of positions that the robot should travel.
    sim : TYPE
        Handle to the sim object.
    trackpoint_handle  : TYPE, optional
        Handle to the trackpoint for the P3DX to travel to.
    robot_handle : TYPE
        Handle to the actual P3DX
    thresh : float, optional
        How close the robot should be to the trackpoint before
        continuing to the next trackpoint.

    Returns
    -------
    None.
    """
    path_index = 1
    while path_index <= path_data_array.shape[0]:
        # set the track point pos
        target_point = path_data_array[-path_index, :]
        if any(np.isnan(target_point)):
            target_point[3:] = [0.0, 0.0, 0.0, 1.0]
        sim.setObjectPose(
            trackpoint_handle, sim.handle_world, list(path_data_array[-path_index, :])
        )
        # get the current robot position
        robot_pos = sim.getObjectPosition(robot_handle, sim.handle_world)
        trackpt_pos = sim.getObjectPosition(trackpoint_handle, sim.handle_world)
        # compute the distance between the trackpt position and the robot
        rob_trackpt_dist = np.linalg.norm(np.array(robot_pos) - np.array(trackpt_pos))
        print(rob_trackpt_dist)
        if rob_trackpt_dist < thresh:
            path_index = path_index + 1
            print("next_point")
