from solver.problem_solver import load_problems_csv, read_and_preprocess_csv

def main():

    #problems_file = "problems/example-problems.csv"
    #mini_schedule_file = "data/mini-schedule.csv"
    schedule_file = "data/schedule.csv"         # File containing schedule data

    # Load and preprocess the problem
    #problems_df = load_problems_csv(problems_file)
    #mini_schedule_df = read_and_preprocess_csv(mini_schedule_file)
    schedule_df = read_and_preprocess_csv(schedule_file)
    
    rslt_df = schedule_df.loc[(schedule_df['Train No.'] == '18312') | 
                              (schedule_df['Train No.'] == '18628') | 
                              (schedule_df['Train No.'] == '13050') |
                              (schedule_df['Train No.'] == '13418') |
                              (schedule_df['Train No.'] == '12376') |
                              (schedule_df['Train No.'] == '18437')]
    #rslt_df.sort_values(by=['Train No.'], inplace=True)
    rslt_df.to_csv('tmp/query.csv', index=False)
    
if __name__ == "__main__":
    main()
    
