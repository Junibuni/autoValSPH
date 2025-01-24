from validation_test.utils.clip_and_extract import clip_and_extract

def run(vtk_folder, save_log_pth, grid_number, bounds, data_array_name):
    assert len(bounds) == 6
    times, mean_values = clip_and_extract(
        vtk_folder=vtk_folder,
        grid_number=grid_number,
        bounds=bounds,
        data_array_name=data_array_name
    )
    
    # 후처리 이후 save_log_pth에 결과 저장 (csv)