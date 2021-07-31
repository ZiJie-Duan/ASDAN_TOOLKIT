
class ASDAN_ANALYZER():

    def __init__(self):
        self.memo = None # here import the class "memorizer" to access the moemory.
        self.set = None # here import the calss "setting" to access the basic setting.


    def asdan_normal_table_ana(self):
        # this function is used to build data structure whitch wirtes in the rusult table.

        data = self.memo.original_data[self.memo.period]

        result_data = []
        vertical_locating_sign = {} # vertical locating sign
        horizontal_locating_sign = {} # horizontal locating sign

        # --------- the program prepares to create vertical locating sign -------------
        row = 4
        col = 0

        vertical_locating_sign["city_background_information"] = 3

        for _, city_data in data.items():
            for team_name, _ in city_data["teams_imformation"].items():

                if team_name in vertical_locating_sign:
                    pass
                else:
                    vertical_locating_sign[team_name] = row # (x,y)
                    result_data.append([row,0,str(team_name)])
                    row += 1

        # ------ the program prepares to create horizontal header and fill data. --------
        row = 0
        col = 1
        for city_name, city_data in data.items():
            horizontal_locating_sign[city_name] = {"self":col}
            result_data.append([0,col,str(city_name)])

            # here program create locating sign of second line city background information.
            col_temporary = col
            for header, _ in city_data["city_background_information"].items():
                horizontal_locating_sign[city_name][header] = col_temporary
                result_data.append([1,col_temporary,str(header)])
                col_temporary += 1

            col_temporary = col
            for _, team_ditails in city_data["teams_imformation"].items():
                for header, _ in team_ditails.items(): # this circulation only use one time.
                    horizontal_locating_sign[city_name][header] = col_temporary
                    result_data.append([3,col_temporary,str(header)])
                    col_temporary += 1
                break
            col = col_temporary

        for city_name, city_data in data.items():
            for header, value in city_data["city_background_information"].items():
                result_col = horizontal_locating_sign[city_name][header]
                result_data.append([2,result_col,value])
            
            for team_name, team_ditails in city_data["teams_imformation"].items():
                for header, value in team_ditails.items():
                    result_row = vertical_locating_sign[team_name]
                    result_col = horizontal_locating_sign[city_name][header]
                    result_data.append([result_row,result_col,value])
        
        self.memo.temporary_data = result_data

