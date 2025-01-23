from validation_test.utils.clip_and_extract import clip_and_extract

def run(vtk_folder):
    clip_and_extract(
        vtk_folder=vtk_folder,
        grid_number=1,
        bounds=[-0.5, 0.5, 0.0, 0.02, -0.5, 0.5],
        data_array_name="pressure"
    )
