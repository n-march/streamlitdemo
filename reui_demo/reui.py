import datetime
import os
import pandas as pd
import plotly.express as px
from dateutil.relativedelta import relativedelta
import streamlit as st

import synthetic_data_gen as synth

# Check if the file already exists, and generate it if not
if not os.path.exists('synth_data.csv'):
    synth.data_gen()

# Read the data
df = pd.read_csv('synth_data.csv')
# Convert 'Month' to period (year-month)
df['Month'] = pd.to_datetime(df['Month'], format='%Y-%m-%d')


def main():

    # Input for metrics at the top of the page:
    # Total number of unique user subject ids
    total_unique_users = df['user subject id'].nunique()

    # Get the current date
    # current_date = datetime.datetime.now()
    current_date = pd.Timestamp('2022-04-02')

    # Calculate the start and end months of the last 3 months (rolling)
    last_quarter_end_month = current_date - relativedelta(days=1)  # Last day of the previous month
    last_quarter_start_month = current_date - relativedelta(months=3)  # Go 3 months back from current date

    # Calculate the start and end months of the 3 months before the last
    quarter_before_last_end_month = last_quarter_start_month - relativedelta(
        days=1)  # One day before the last 3-month period starts
    quarter_before_last_start_month = last_quarter_start_month - relativedelta(
        months=3)  # Go 3 months back from the start of the last 3-month period

    # Number of unique users over the last quarter
    last_quarter_unique_users = df[df['Month'].between(last_quarter_start_month, last_quarter_end_month)][
        'user subject id'].nunique()

    # Number of unique users over the quarter before last
    quarter_before_last_unique_users = \
        df[df['Month'].between(quarter_before_last_start_month, quarter_before_last_end_month)]['user subject id'].nunique()

    # Calculate the delta between the last quarter and the quarter before that
    delta_last_two_quarters = last_quarter_unique_users - quarter_before_last_unique_users

    # Monthly unique users for the last month
    latest_month_unique_users = df[df['Month'] == last_quarter_end_month]['user subject id'].nunique()

    # Monthly unique users for the month before last
    month_before_latest = datetime.datetime(current_date.year, current_date.month - 2, 1)
    month_before_latest_unique_users = df[df['Month'] == month_before_latest]['user subject id'].nunique()

    # Calculate the delta between the last month and the month before that
    delta_last_two_months = latest_month_unique_users - month_before_latest_unique_users

    # Preprocess the data to get unique counts of "user subject id" for each month
    unique_counts = df.groupby('Month')['user subject id'].nunique().reset_index()
    unique_counts.columns = ['Month', 'Unique Subject IDs']

    # Display the Plotly chart
    fig = px.bar(unique_counts, x='Month', y='Unique Subject IDs', title='Unique "user subject id" Per Month')
    st.plotly_chart(fig)


if __name__ == '__main__':
    st.title('User Subject ID Engagement Report')
    # Create columns for metrics
    col1, col2, col3 = st.columns(3)

    # Display metrics
    col1.metric("Total Unique Users", total_unique_users)
    col2.metric("Users Over Last 3 Months (Rolling)", last_quarter_unique_users, delta_last_two_quarters)
    col3.metric("Users This Month", latest_month_unique_users, delta_last_two_months)
