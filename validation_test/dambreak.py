from validation_test.utils.clip_and_extract import clip_and_extract

def run(vtk_folder):
    clip_and_extract(
        vtk_folder=vtk_folder,
        grid_number=1,
        bounds=[-0.52, -0.48, 0.0, 0.04, -0.84, -0.82],
        data_array_name="pressure"
    )