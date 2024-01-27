from gui import get_user_input
from data_processing import fetch_stock_data_and_save


if __name__ == '__main__':
    user_inputs = get_user_input()
    fetch_stock_data_and_save(user_inputs['csv_path'], user_inputs['start_date'], 
                              user_inputs['end_date'], user_inputs['period'], 
                              user_inputs['skip_first_row'], user_inputs['output_file'])