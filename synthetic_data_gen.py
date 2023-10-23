import random
import pandas as pd


def data_gen():
    # operators = ['user1', 'user2', 'user3']
    # features = ['Feature1', 'Feature2', 'Feature3']
    # months = ['Jan', 'Feb', 'March', 'April', 'May']
    # user_subject_ids = ['SubjectA', 'SubjectB', 'SubjectC', 'SubjectD', 'SubjectE']
    #
    # data = {
    #     'Operator': [],
    #     'Feature name': [],
    #     'Month': [],
    #     'user subject id': []
    # }
    #
    # for operator in operators:
    #     num_runs = random.randint(1, 20)  # Random number of runs for each operator
    #     for _ in range(num_runs):
    #         feature = random.choice(features)
    #         month = random.choice(months)
    #         num_subjects = random.randint(1, 20)  # Random number of subject IDs for each run
    #
    #         for _ in range(num_subjects):
    #             subject_id = random.choice(user_subject_ids)
    #
    #             data['Operator'].append(operator)
    #             data['Feature name'].append(feature)
    #             data['Month'].append(month)
    #             data['user subject id'].append(subject_id)
    #
    # main_df = pd.DataFrame(data)
    # main_df.to_csv('synth_data.csv', index=False)  # Added index=False to not write row numbers
    # Generate 100 unique random subject IDs
    subject_ids = [f"Subject_{i}" for i in range(100)]

    operators = ['user1', 'user2', 'user3']
    features = ['Feature1', 'Feature2', 'Feature3']
    months = ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01']

    # Create random dataset
    rows = []
    for _ in range(200):  # Number of rows
        row = {
            'Operator': random.choice(operators),
            'Feature name': random.choice(features),
            'Month': random.choice(months),
            'user subject id': random.choice(subject_ids)
        }
        rows.append(row)

    # Convert to DataFrame
    df = pd.DataFrame(rows)

    # Save as CSV
    df.to_csv('synth_data.csv', index=False)
