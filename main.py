import config.folder_and_file_names as fname
from discretization.get_discretization import DisData
from primarkov.build_markov_model import ModelBuilder
from generator.state_trajectory_generation import StateGeneration
from generator.to_real_translator import RealLocationTranslator
# from tools.object_store import ObjectStore
from config.parameter_carrier import ParameterCarrier
from config.parameter_setter import ParSetter
from tools.data_writer import DataWriter
from data_preparation.data_preparer import DataPreparer
import os

if __name__ == "__main__":
    writer = DataWriter()
    par = ParSetter().set_up_args()
    pc = ParameterCarrier(par)
    data_preparer = DataPreparer(par)
    trajectory_set = data_preparer.get_trajectory_set()
    disdata1 = DisData(pc)
    grid = disdata1.get_discrete_data(trajectory_set)
    discrete_trajectories = [trajectory.usable_sequence for trajectory in trajectory_set.trajectory_list]
    output_filename = f"discretized_{pc.dataset_file_name}"
    output_file = os.path.join("outputs", output_filename)
    writer.save_discrete_trajectory_data(discrete_trajectories, output_file)
    